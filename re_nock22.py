'''
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．．
'''
# coding: utf-8
#python3 nock22.py
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

pattern = re.compile('\[\[Category:(.*?)(?:\|.*?)?\]\]')
#\[\[Category:部分を取り除く(検索一部)
#(.*?)最後に残る文字列を最短でグループ化(最長だと困る)
#(?:\|\*)?ある時ないときがあるから0or1回で指定？(?:...)でグループ化じゃない括弧を使用可
#\]\].*$'文末の部分を取り除く(検索一部)
#つまり [[Category:.....?|*?]]で検索、...を抽出している？
#?|*?は|*がある場合はそれを消して,ない場合そのまま
result = pattern.findall(UKtxt())
#結果にlineのpattern該当部分を入れる

for matchobj in result: 
    print(matchobj) 

#0指定で元の文がでてくる
#[[Category:イギリス|*]]