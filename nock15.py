'''
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，
入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
'''
#python3 nock14.py popular-names.txt 5
#コマンド：tail -n 10 popular-names.txt
#diff <(python3 nock15.py popular-names.txt 10) <(tail -n 10 popular-names.txt)
import sys
#コマンドライン引数を使用するため
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
    with open(cmd[1]) as f:
        #開きなおす
        with open('nock15w.txt','w') as f1:
            #ファイルを開く
            for line in f:
                #行数分繰り返し
                count+=1
                #カウント+1
                if count>loop-int(cmd[2]):
                    #行数-cmdで最後の何行かを表す
                    f1.write(line)
                    line=line.strip("\n")
                    print(line)
                
else:
    #数字じゃなかった場合
    print('自然数でお願いします')
