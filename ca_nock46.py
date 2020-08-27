'''
46. 動詞の格フレーム情報の抽出
45のプログラムを改変し，述語と格パターンに続けて
項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．
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
        self.counter=0
        self.morphs=[]
        self.dst=-1
        self.srcs=[]
        self.judge2=0   #動詞

morph=[]
count=0
chunks=dict()
chunks[count]=Chunk()
judge=True
josies=[]
dousies=[]
dousi_count=0
with open('ai.ja.txt.parsed',encoding='utf-8')as f:
    for line in f:
        surface=line.split('\t')
        chunks[count+1]=Chunk()
        if len(surface)>1:
            other=surface[1].split(',')
            Base=other[6]
            Pos=other[0]
            Pos1=other[1]
            morph.append(Morph(surface[0],Base,Pos,Pos1))
            
            if Pos=='動詞':
                if judge==True:
                    chunks[count].judge2=True
                    judge=False
                    dousies.append(Base)
                chunks[count].morphs.append(Base)
            elif Pos!='記号':
                chunks[count].morphs.append(surface[0])#chunk.morphs
            if Pos=='助詞':
                if surface[0] not in josies:
                    josies.append(surface[0])
            if Pos1 == '句点':
                judge=True

        elif 'EOS' not in line:
            kakari=line.split(' ')
            count=int(kakari[1])
            dst=kakari[2].replace('D','')
            chunks[count].dst=int(dst)                    #chunk.dst
            chunks[count].counter=count
        else:
            for number in range(count):
                if chunks[number].dst != -1:
                    chunks[chunks[number].dst].srcs.append(number)
            for result in range(count+1):
                x="{0}\t{1}{2}"
                #if chunks[result].dst == -1:
                    #saki=''
                if chunks[result].judge2:
                    bunsetsu=''
                    sakies=[]
                    saki=''
                    for josi in chunks[result].srcs:
                        if chunks[josi].morphs[-1] in josies:
                            sakies.append(chunks[josi].morphs[-1])
                            bunsetsu=bunsetsu+'\t'+''.join(chunks[josi].morphs)
                    for saki_tab in sakies:
                        saki=saki+'\t'+saki_tab
                    print(x.format(
                        #chunks[result].counter,
                        dousies[dousi_count],
                        saki,bunsetsu))
                    dousi_count+=1
            for ketu in range(count+1):
                chunks[ketu].morphs=[]
                chunks[ketu].srcs=[]
            count=0