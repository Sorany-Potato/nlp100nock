'''
25. テンプレートの抽出
記事中に含まれる「基礎情報」
テンプレートのフィールド名と値を抽出し，
辞書オブジェクトとして格納せよ．
'''
#python re_nock25.py
import re
# coding: utf-8
import gzip
#gzipで圧縮されているため使用
import json
#json形式なので使用
def UKtxt():
    with gzip.open('jawiki-country.json.gz','r') as f:
        #gzipで圧縮されてるのでgzipであける
        for line in f:
            prin = json.loads(line)
            if prin['title'] =='イギリス':
                return prin['text']


tmp={}
kiso_pattern=re.compile(r'^\{\{基礎情報.*?$(.*)^\}\}$',re.MULTILINE + re.VERBOSE + re.DOTALL)
key_pattern =re.compile(r'^\|(.+?)\s*=\s*(?:(?:(.+?)(?=\n\||\n$))|(\n.+?)+?)',re.MULTILINE + re.VERBOSE + re.DOTALL)

kiso=kiso_pattern.findall(UKtxt())
sample=key_pattern.findall(kiso[0])
for saline in sample:
    if saline:
        tmp[saline[0]]=saline[1]
        
for key,value in tmp.items():
    #prin=('{0}: {1}')
    #wprin=prin.format(key,value)

    print(key+':'+value)
