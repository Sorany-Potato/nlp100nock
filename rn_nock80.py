"""
問題51で構築した学習データ中の単語にユニークなID番号を付与したい．
学習データ中で最も頻出する単語に1，2番目に頻出する単語に2，……といった方法で，
学習データ中で2回以上出現する単語にID番号を付与せよ．
そして，与えられた単語列に対して，ID番号の列を返す関数を実装せよ．
ただし，出現頻度が2回未満の単語のID番号はすべて0とせよ．
"""
import torch
import numpy as np
import pandas as pd
import re
import sys

def idx(text):
    result=[]
    title = re.sub(r'\s+', ' ', text)
    for word in title.split():
        if word in rank:
            result.append(rank[word])
        else:
            result.append(0)
    return result

cmd = sys.argv
filename='./'+cmd[1] #'./train.txt'
dataset=[]
cate=[]
train = pd.read_csv(filename,header=0,sep='\t')
#train[title=0,category=1][行数]
words = {}# 単語を数える辞書を作成
for line in train['title']:
    title = re.sub(r'\s+', ' ', line)
    dataset.append(title)
    # split()でスペースと改行で分割したリストから単語を取り出す
    for word in title.split():
        # 単語をキーとして値に1を足していく。
        # 辞書に単語がない、すなわち初めて辞書に登録するときは0+1になる。
        words[word] = words.get(word, 0) + 1  

for line in train['category']:
    cate.append(line)

d = [(v, k) for k, v in words.items()]
d.sort()
d.reverse()
rank = {}
id=0
for count, word in d:
    id+=1
    if count > 1:
        rank[word] = id
    else:
        rank[word] = 0  #辞書id完了
train_t=[]
for line in train['title']:
    #print(idx(line))
    #train_t.append(torch.tensor(idx(line),dtype=torch.long))
    train_t.append(idx(line))
    #print(line)
breakpoint()


