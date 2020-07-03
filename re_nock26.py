'''
26. 強調マークアップの除去
25の処理時に，テンプレートの値から
MediaWikiの強調マークアップ
（弱い強調，強調，強い強調のすべて）
を除去してテキストに変換せよ
'''
#python re_nock26.py
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
key_pattern =re.compile(r'^\|(.+?) = (?:(?:(.+?)(?=\n\||\n$))|(\n.+?)+?)',re.MULTILINE + re.VERBOSE + re.DOTALL)
mark_pattern =re.compile('\'{2,5}')

kiso=kiso_pattern.findall(UKtxt())
sample=key_pattern.findall(kiso[0])
for saline in sample:
    if saline:
        tmp[saline[0]]=mark_pattern.sub('',saline[1])
        
for key,value in tmp.items():
    #print(key,value)
    print(key.replace(' ','')+':'+value)
