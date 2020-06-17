'''
18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ
（注意: 各行の内容は変更せずに並び替えよ）
確認にはsortコマンドを用いよ
（この問題はコマンドで実行した時の結果と合わなくてもよい）
'''
#python nock18.py popular-names.txt
#コマンド：sort -k 3nr,3 popular-names.txt
#diff <(sort -k 3nr,3 popular-names.txt) nock18w.txt
import sys
#コマンドライン引数を使用するため
filename=str(sys.argv[1])
with open(filename) as f:
    name=[]
    gender=[]
    year=[]
    pop={}
    for count,line in enumerate(f):
        #1行づつ読み取る
        txt=line.split('\t')
        #tabで分けられているのでそれを利用        
        name.append(txt[0])
        #1単語目        
        gender.append(txt[1])
        #2単語目
        pop[count]=int(txt[2])
        #3単語目
        year.append(txt[3])
        #4単語目
    #pops=sorted(pop)
    pops=sorted(pop.items(), key=lambda x:x[1], reverse=True)
    pop.clear()
    pop.update(pops)
    #print(pop)
    

with open('nock18w.txt','w') as f1:
    for value,keyw in zip (pop.keys(),pop.values()):
        w='{0}\t{1}\t{2}\t{3}'
        wtxt=w.format(name[value],gender[value],keyw,year[value])
        f1.write(wtxt)

