'''
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，
2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
確認にはcutコマンドを用いよ
'''
#python3 nock12.py popular-names.txt
#コマンド：cut -f 1 popular-names.txt
#コマンド：cut -f 2 popular-names.txt
#diff <(cut -f 1 popular-names.txt) col1.txt
import sys
filename=sys.argv
with open(filename[1]) as f,open('col1.txt', 'w') as f1,open('col2.txt', mode="w") as f2:

    for line in f:
        #1行づつ読み取る
        txt=line.split('\t')
        #今回はtabで分けられているのでそれを利用        
        f1.write(txt[0]+'\n')
        #col1にはtabで分けられた1単語目を        
        f2.write(txt[1]+'\n')
        #col2には2単語目を追記
        #教科書にはmdoe=?のほうで書いてあるがネットでは'?'で書かれていた
        #一応どちらも試しただけ,どっちでもできる





