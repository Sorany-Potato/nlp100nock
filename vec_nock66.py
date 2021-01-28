"""
66. WordSimilarity-353での評価
The WordSimilarity-353 Test Collectionの評価データを
ダウンロードし，単語ベクトルにより計算される類似度のランキングと
人間の類似度判定のランキングの間のスピアマン相関係数を計算せよ．
"""
import pandas as pd
import numpy as np
import gensim

model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
df = pd.read_csv('wordsim353/combined.csv')
N=len(df)
word_sim=[]
human_sim=[]
word_rank=[]
human_rank=[]
for i in range(N):
    line=df.iloc[i]
    word_sim.append(model.similarity(line['Word 1'],line['Word 2']))
    human_sim.append(line['Human (mean)'])

for word in word_sim:
    count=0
    for x in word_sim:
        if word>=x:
            count+=1
    word_rank.append(count)

for human in human_sim:
    count=0
    for x in human_sim:
        if human>=x:
            count+=1
    human_rank.append(count)

list1=np.array(word_rank)
list2=np.array(human_rank)
print(1-(6*sum((list1-list2)**2)/(N*(N**2-1))))

#0.9982972326257297