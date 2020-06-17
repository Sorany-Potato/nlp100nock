'''
20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，
「イギリス」に関する記事本文を表示せよ．
問題21-29では，ここで抽出した記事本文に対して実行せよ．
'''
# coding: utf-8
import gzip
#gzipで圧縮されているため使用
import json
#json形式なので使用
with gzip.open('jawiki-country.json.gz','r') as f:
    #gzipで圧縮されてるのでgzipであける
    with open('nock20w.txt','w') as f2:
        for line in f:
            prin = json.loads(line)
            if prin['title'] =='イギリス':
                f2.write(prin['text'])
                print(prin['text'])

