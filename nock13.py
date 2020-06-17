'''
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，
元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
確認にはpasteコマンドを用いよ．
'''
#python3 nock13.py col1.txt col2.txt
#コマンド：paste col1.txt col2.txt
#diff nock13w.txt <(paste col1.txt col2.txt)
import sys
filename=sys.argv
with open(filename[1]) as f1:
    with open(filename[2]) as f2:
        #使用するファイルを開ける状態に
        with open('nock13w.txt','w') as f3:
            #今回の結果を出すファイル
            for line1,line2 in zip(f1,f2):
                #zipで2つまとめてfor
                line1=line1.replace("\n","")
                line2=line2.replace("\n","")
                #何度か試したけどどうやら文頭に\nがある？
                #面倒なので\nを全部排除
                v="{a}\t{b}\n"
                f3.write(v.format(a=line1,b=line2))
                #formatで問題文通りの形に出力

