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
        self.judge=0  #名詞

def morphline(data):
    return len(data)==2

def root(chunk, chunks):#chunkの根までのルートを返す
    path=[chunk]
    dst = chunk.dst
    if dst == -1:
        return path
    else:
        return path + root(chunks[dst], chunks)

def in_j(i_root,j_chunk):#kのない場合の条件
    #i_rootにj_chunkがあるかどうか
    return j_chunk in i_root

def connect(i_root,j_chunk):#iの根上にあるjまでの係り受けパスを抽出
    cresult=[]
    for ci_chunk in i_root:
        cresult.append(ci_chunk)
        if ci_chunk.morphs==j_chunk.morphs:    #一致まで
            cresult.append(ci_chunk)
            return cresult

def k_chunk(i_path, j_path):    #kがある場合の抽出
    k=[]
    i_k=[]
    j_k=[]
    for i in i_path:
        j_k=[]
        for j in j_path:
            if k==[]:
                if i==j:        #一致するk
                    k += [j]
                    break
                j_k += [j]#jからkの直前
        if k==[]:
            i_k += [i]       #iからkの直前
        else:
            break
    return i_k,j_k,k

def arrow(wordlist,abc):
    x=''
    for co,word in enumerate(wordlist):
        if abc==3 and word==wordlist[-1]:#最後尾の名詞をyにして文字列に
            x +='y'+''.join(word.morphs[word.judge:])
        elif abc>1 and co==0:#先頭の名詞をxにして文字列に
            x +='x'+''.join(word.morphs[word.judge:])
        elif abc==1 and co==0:#先頭の名詞をyにして文字列に
            x +='y'+''.join(word.morphs[word.judge:])
        else:
            x += ''.join(word.morphs)  #リストを文字列に
        if word==wordlist[-1]:#矢印が最後に入らないように
            break;
        x += '→'
    return x

#def exist(i_path, j_path):
chunks=dict()
chunk=[]
document=[]
with open('brain.cabocha.parset.txt',encoding='utf-8')as f:
    #with open('mini.parsed.txt',encoding='utf-8')as f:
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
                chunks[chunk_id].judge +=1     #名詞判定

        elif chunks:                                       #EOS
            #chunk.append(chunks[chunk_id])  #文節ごとに追加するEOS手前のまとまり
            document.append(chunk)         #まとめられたchunkが一文節づつはいる
            
            for chunk_id in range(len(chunks)):
                if chunks[chunk_id].dst != -1:
                    chunks[chunks[chunk_id].dst].srcs.append(chunk_id)#係り受けの追加
            chunk = []

            for doc in document:    #ひとつづつ文節確認
                for i,i_chunk in enumerate(doc):#doc=chunksの一つ
                    for j_chunk in doc[i+1:]:#i以降の文節
                        if i_chunk.judge==0 or j_chunk.judge==0:#両方名詞じゃない
                            continue
                        if i_chunk.dst==-1 or j_chunk.dst==-1:         #最初からdst-1ならスキップ
                            continue
                        i_path=root(i_chunk, chunks)#i_chunkのroot
                        
                        if in_j(i_path,j_chunk):        #根までにある場合
                            result=connect(i_path,j_chunk)#根にあるjまでのリスト
                            print(arrow(result,3))#矢印でつなぐ
                        else:
                            j_path=root(j_chunk, chunks)#j_chunkのroot
                            i,j,k=k_chunk(i_path,j_path)#i,j,kそれぞれの抽出
                            
                            #print(arrow(j,1))
                            print(arrow(i,2),'|',arrow(j,1),'|',arrow(k,0))#矢印でつなぎながらそれぞれ｜でつなぐ
            document=[]