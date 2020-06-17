'''
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，
入力のファイルを行単位でN分割せよ．
同様の処理をsplitコマンドで実現せよ．
'''
#python3 nock16.py popular-names.txt 3
#コマンド：split -l 927 -d popular-names.txt nock16u  (3分割の場合)
#diff nock16u00 nock16w0.txt
#diff nock16u01 nock16w1.txt
#diff nock16u02 nock16w2.txt
import sys
#コマンドライン引数を使用するため
try:
    cmd = sys.argv
    #引数をcmdにいれる
    if cmd[2].isdigit():
        #引数が数字か判定
        count=0
        loop=0
        #行数カウントのための変数
        with open(cmd[1]) as f:
            for check in f:
                loop+=1
                #別で先に行数を確認
        
        amari=loop%int(cmd[2])
        #あまり
        kai=(loop-amari)/int(cmd[2])
        #分割したときに表示する行
        with open(cmd[1]) as f1:
            #開きなおす
            txt=f1.read()
            #txtに読み込んだものを入れる
            ctxt=txt.split('\n')
            #改行で分けたものをctxtに入れる
        #print(kai,amari)
        #確認用のprint
        count=0
        #countするもの
        for prin in range(int(cmd[2])):
            #分割数だけ繰り返す
            filename = 'nock16w'+str(prin)+'.txt'
            #ファイル名を変えていくためのもの
            #今回はnock16w[数].txtという形
            with open(filename,'w') as f2:
                #連番のファイルを新規で作成
                for x in range(int(kai)):
                    #kaiの回数分繰り返し
                    f2.write(ctxt[int(count+x)]+'\n')
                    #1行づつ書いていく
                count+=kai
                if amari>0:
                    f2.write(ctxt[int(count)]+'\n')
                    count+=1
                    amari-=1
                
                    
    else:
        #数字じゃなかった場合
        print('自然数でお願いします')

except IndexError:
    print('コマンド引数を指定してください')