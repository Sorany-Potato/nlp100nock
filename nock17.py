'''
17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．
確認にはcut, sort, uniqコマンドを用いよ．
要は使われた文字はどれだけあるかということかな
ではなく文字列でセット
'''
#python3 nock17.py col1.txt
#コマンド；sort -u col1.txt
#diff <(sort -u col1.txt) nock17w.txt
import sys
#コマンドライン引数を使用するため
filename=str(sys.argv[1])
with open(filename) as f:
    txt=[]
    #nock12でcol1に分けたのでそれを使う
    for line in f:
        txt.append(line.replace('\n',''))
    #読み込んだものをtxtに
    ctxt=sorted(set(txt))
    #setで重複文字はまとめてsortでアルファベット順に
    with open('nock17w.txt','w') as f2:
        #新規ファイル作成
        #f2.write(str(ctxt))
        #print(ctxt)
        #型を指定しないできないので指定
        for prin in ctxt:
            f2.write(str(prin)+'\n')