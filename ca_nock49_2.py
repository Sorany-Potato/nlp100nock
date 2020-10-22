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
    dst = chunk.dst
    if dst == -1:
        return path
    else:
        path += root(chunks[dst], chunks)
    return path

def k_chunk(i_path, j_path):
    k=[]
    matu=[]
    judge=False
    for i in i_path:
        for j in j_path:
            if judge==False:
                k.append(j)
                if i==j:
                    judge=True
            else:
                matu.append(j)
    return k,matu

#def exist(i_path, j_path):
chunks=dict()
chunk=[]
document=[]
with open('ai.ja.txt.parsed',encoding='utf-8')as f:
    for line in f:
        surface=line.split('\t')
        if line[0] == "*":
            kakari=line.split(' ')
            if int(kakari[1])>0:
                chunks[chunk_id].dst=int(dst)                    #chunk.dst
                chunks[chunk_id].chunk_id=chunk_id                #文節番号
                chunk.append(chunks)  
            #chunk = Chunk()
            chunk_id=int(kakari[1])            #kakari[1]=chunk_id=文節番号
            dst=kakari[2].replace('D','')       #dst=係り先文節番号
            chunks[chunk_id]=Chunk()

        elif morphline(surface):
            other=surface[1].split(',')
            Base=other[6]
            Pos=other[0]
            Pos1=other[1]
            morph = Morph(surface[0],Base,Pos,Pos1)
            if Pos!='記号':
                chunks[chunk_id].morphs.append(morph.surface)#chunk.morphs
            if Pos=='名詞':
                chunks[chunk_id].judge=True

        elif chunks:                                       #EOS
            chunks[chunk_id].dst=int(dst)                    #chunk.dst
            chunks[chunk_id].chunk_id=chunk_id                #文節番号
            chunk.append(chunks)

            document.append(chunk)         #まとめられたchunkが一文節づつはいる
            chunk = []
            for chunk_id in range(len(chunks)):
                if chunks[chunk_id].dst != -1:
                    chunks[chunks[chunk_id].dst].srcs.append(chunk_id)

        for doc in document:    #ひとつづつ文節確認
            for i,i_chunk in enumerate(doc):#doc=chunksの一つ
                for j,j_chunk in enumerate(doc[i+1:]):#i以降の文節
                    if i_chunk[i].judge==False or j_chunk[j].judge==False:#両方名詞じゃない
                        continue
                    i_path=root(i_chunk[i], chunks)#i_chunkのroot
                    j_path=root(j_chunk[i], chunks)#j_chunkのroot
                    k_path,end=k_chunk(i_path,j_path)
                    #if 

                    #while chunk_id < :
        chunks.clear


