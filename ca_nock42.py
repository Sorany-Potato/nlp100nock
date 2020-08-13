'''
42. 係り元と係り先の文節の表示
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
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

morph=[]
count=0
chunks=dict()
chunks[count]=Chunk()
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
            if Pos!='記号':
                chunks[count].morphs.append(surface[0])#chunk.morphs
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
                x="{0}{1}\t{2}{3}"
                if chunks[result].dst == -1:
                    saki=''
                else:
                    saki=''.join(chunks[chunks[result].dst].morphs)
                print(x.format(
                    chunks[result].counter,
                    ''.join(chunks[result].morphs),
                    chunks[result].dst,
                    saki))
            for ketu in range(count+1):
                chunks[ketu].morphs=[]
                chunks[ketu].srcs=[]
            count=0