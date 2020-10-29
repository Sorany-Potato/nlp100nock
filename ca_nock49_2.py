'''
49. 名詞間の係り受けパスの抽出
文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．
ただし，名詞句ペアの文節番号がiとj（i<j）のとき，
係り受けパスは以下の仕様を満たすものとする．
文節iとjに含まれる名詞句はそれぞれ，XとYに置換する
'''
class Morph:
    def __init__(self,surface,base,pos,pos1):
        self.surface=surface
        self.base=base
        self.pos=pos
        self.pos1=pos1

    def __str__(self):
        x="surface:{0}\tbase:{1}\tpos:{2}\tpos1:{3}"
        return x.format(self.surface,self.base,self.pos,self.pos1)

class Chunk:
    def __init__(self):
        self.chunk_id=0
        self.morphs=[]
        self.dst=-1
        self.srcs=[]
        self.judge=False   #名詞

def morphline(data):
    return len(data)==2

def root(chunk, chunks):
    path=[]
    path.append(chunk.morphs)
    """
    dst = chunk.dst
    if dst == -1:
        return path
    else:
        root(chunks[dst], chunks)
    """
    while True:
        path.append(chunks[chunk.dst].morphs)
        if chunks[chunk.dst].dst == -1:
            break;
        chunk=chunks[chunk.dst]
    return path

def in_j(i_root,j_chunk):#kのない場合の条件
    for x in i_root:
        if x == j_chunk.morphs:
            break;
    return x == j_chunk.morphs

def connect(i_root,j_chunk):#iの根上にあるjまでの係り受けパスを抽出
    cresult=[]
    for ci_chunk in i_root:
        cresult.append(ci_chunk)
        if ci_chunk==j_chunk.morphs:    #一致まで
            cresult.append(ci_chunk)
            return cresult

def k_chunk(i_path, j_path):    #kがある場合の抽出
    k=[]
    i_k=[]
    j_k=[]
    judge=False
    for i in i_path:
        for j in j_path:
            if judge==False:
                if i==j:        #一致するk
                    judge=True
                    k.append(j)         
                j_k.append(j)#jからkの直前
        if judge==False:
            i_k.append(i)       #iからkの直前
    return i_k,j_k,k

def next(wordlist):
    x=''
    for word in wordlist:
        x += ''.join(word)  #リストを文字列に
        if word==wordlist[-1]:#矢印が最後に入らないように
            break;
        x += '→'
    return x

#def exist(i_path, j_path):
chunks=dict()
chunk=[]
document=[]
with open('brain.cabocha.parset.txt',encoding='utf-8')as f:
    for line in f:
        surface=line.split('\t')
        if line[0] == "*":
            kakari=line.split(' ')
            chunk_id=int(kakari[1])            #kakari[1]=chunk_id=文節番号
            dst=kakari[2].replace('D','')       #dst=係り先文節番号
            chunks[chunk_id]=Chunk()            #枠組み
            chunks[chunk_id].dst=int(dst)                    #chunk.dst
            chunks[chunk_id].chunk_id=chunk_id                #文節番号
            chunk.append(chunks[chunk_id])      #文節ごとのまとまりを追加

        elif morphline(surface):
            other=surface[1].split(',')
            Base=other[6]
            Pos=other[0]
            Pos1=other[1]
            morph = Morph(surface[0],Base,Pos,Pos1)
            if Pos!='記号':
                chunks[chunk_id].morphs.append(morph.surface)#chunk.morphs
            if Pos=='名詞':
                chunks[chunk_id].judge=True     #名詞判定

        elif chunks:                                       #EOS
            chunk.append(chunks[chunk_id])  #文節ごとに追加するEOS手前のまとまり
            document.append(chunk)         #まとめられたchunkが一文節づつはいる
            
            for chunk_id in range(len(chunks)):
                if chunks[chunk_id].dst != -1:
                    chunks[chunks[chunk_id].dst].srcs.append(chunk_id)#係り受けの追加

            for doc in document:    #ひとつづつ文節確認
                for i,i_chunk in enumerate(doc):#doc=chunksの一つ
                    for j_chunk in doc[i+1:]:#i以降の文節
                        if i_chunk.judge==False or j_chunk.judge==False:#両方名詞じゃない
                            continue
                        if i_chunk.dst==-1 or j_chunk.dst==-1:         #最初からdst-1ならスキップ
                            continue
                        i_path=root(i_chunk, chunks)#i_chunkのroot
                        
                        if in_j(i_path,j_chunk):        #根までにある場合
                            result=connect(i_path,j_chunk)#根にあるjまでのリスト
                            print(next(result))#矢印でつなぐ
                        else:
                            j_path=root(j_chunk, chunks)#j_chunkのroot
                            i,j,k=k_chunk(i_path,j_path)#i,j,kそれぞれの抽出
                            print(next(i),'|',next(j),'|',next(k))#矢印でつなぎながらそれぞれ｜でつなぐ
            chunk = []
            document=[]