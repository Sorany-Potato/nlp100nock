'''
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，
入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
'''
#コマンド：head -n 10 popular-names.txt
#python3 nock14.py popular-names.txt 5
#diff <(head -n 10 popular-names.txt) <(python3 nock14.py popular-names.txt 10)
import sys
#コマンドライン引数を使用するため
try:
    cmd = sys.argv
    #引数をcmdにいれる
    if cmd[2].isdigit():
        #引数が数字か判定
        count=0
        #行数カウントのための変数
        with open(cmd[1]) as f:
            #ファイルを開く
            for line in f:
                line=line.strip("\n")
                #行数分繰り返し
                count+=1
                #カウント+1
                if count>int(cmd[2]):
                    break;
                    #カウントが引数より大きくなったら繰り返しを終了
                #with open('nock14w.txt','a') as f1:
                    #f1.write(line)
                print(line)
                    
    else:
        #数字じゃなかった場合
        print('自然数でお願いします')
        
except IndexError:
    print('コマンド引数を指定してください')