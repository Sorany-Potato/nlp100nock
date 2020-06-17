'''
10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
'''
#python3 nock10.py popular-names.txt
#コマンド：wc -l < popular-names.txt
#diff <(python3 nock10.py popular-names.txt) <(wc -l < popular-names.txt)
import sys
try:
    filename=sys.argv

    with open(filename[1]) as f:
        #fでファイルを開けるように設定
        line_count=0
        #line_countは行数をカウントする変数
        for line in f:
            #with open内でfor line in 開くファイルで1行づつ読み取りになるらしい
            line_count+=1

    print(line_count)

except IndexError:
    print('コマンド引数を指定してください')