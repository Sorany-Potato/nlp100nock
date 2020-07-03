'''
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
'''
# coding: utf-8
#python3 nock21.py
import re
import gzip
import json
def UKtxt():
    with gzip.open('jawiki-country.json.gz','r') as f:
        #gzipで圧縮されてるのでgzipであける
        for line in f:
            prin = json.loads(line)
            if prin['title'] =='イギリス':
                return prin['text']
pattern = re.compile('\[\[Category:.*\]\]')
result=pattern.findall(UKtxt())
for x in result:
    print(x)