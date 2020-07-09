'''
28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値から
MediaWikiマークアップを可能な限り除去し，
国の基本情報を整形せよ．
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
link=[]
kiso_pattern =re.compile(r'^\{\{基礎情報.*?$(.*)^\}\}$',re.MULTILINE + re.VERBOSE + re.DOTALL)
sample_pattern =re.compile(r'^\|(.+?)\s*=\s?(?:(?:(.+?)(?=\n\||\n$))|(\n.+?)+?)',re.MULTILINE + re.VERBOSE + re.DOTALL)
mark_pattern =re.compile('\'{2,5}')
link_pattern_kari =re.compile(r'\{\{(?:[^|]*?\|)*?([^|]*?)\}\}')
link_pattern_sin =re.compile(r'(?:\[\[(?:[^|]*?\|)*?([^|]*?)\]\])|\[.*?\]')
link_pattern_last=re.compile(r'\<([^>]*?)\>')

kiso=kiso_pattern.findall(UKtxt())
sample=sample_pattern.findall(kiso[0])
for count,saline in enumerate(sample):
    if saline:
        result_kari=link_pattern_kari.sub(r'\1',saline[1])
        result_sin=link_pattern_sin.sub(r'\1',result_kari)
        result=link_pattern_last.sub('',result_sin)
        tmp[saline[0]]=mark_pattern.sub('',result)
        
for key,value in tmp.items():
    print(key,value)


#内部リンク
#[[記事名]]
#[[記事名|表示文字]]
#[[記事名#節名|表示文字]]