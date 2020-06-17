'''
19. 各行の1コラム目の文字列の出現頻度を求め，
出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，
その高い順に並べて表示せよ．
確認にはcut, uniq, sortコマンドを用いよ．
'''
#python3 nock19.py col1.txt
#cut -f 1 popular-names.txt | sort -u
import sys
filename=sys.argv
with open(filename[1]) as f:
    txt=[]
    #nock12でcol1に分けたのでそれを使う
    for line in f:
        txt.append(line.replace('\n',''))
    #読み込んだものをtxtに,改行は必要ないので消して1単語づつみる
    counter={}
    #辞書型のもの用意
    for ws in txt:
        #txtの文字列で繰り返し
        if ws in counter:
            counter[ws]+=1
            #すでにあるものは+1
        else:
            counter[ws]=1 
            #初めてのものは追加
    #print(counter.items())
    counter=sorted(counter.items(), key=lambda x:x[1], reverse=True)
    #これで辞書型の2個目の要素でsortできる
    
    with open('nock19w.txt','w') as f2:
        #新規ファイル作成
        #f2.write(str(counter))
        #型を指定しないとできないので指定
        for prin in counter:
            f2.write(str(prin)+'\n')
            
            print(str(prin[1]).rjust(7),prin[0])
