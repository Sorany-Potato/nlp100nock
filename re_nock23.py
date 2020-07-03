'''
23. セクション構造
記事中に含まれるセクション名とそのレベル
（例えば”== セクション名 ==”なら1）を表示せよ．
'''
# coding: utf-8
#python3 nock23.py
import re

pattern = re.compile('^(=*) ?(.*?) ?=*$')
#^=* 文頭に=1つ以上の連なり
#^=* 文末に=1つ以上の連なり
#間の文字をグループで取得
#文頭の=を全部取得

#==がある文

#resultにセクション名を
#文頭の=の数を
with open('nock20w.txt') as f:
    for line in f:
        if '==' in line:
            #==がある文
            result = pattern.match(line)
            #resultにセクション名を
            #文頭の=の数を
            if result: #none以外
                prin=('{0}:{1}')
                wprin=prin.format(result.group(2),len(result.group(1))-1)
                print(wprin) 
                #f2.write(str(wprin)+'\n')


