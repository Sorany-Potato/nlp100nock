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
for i in range(N):
    line=df.iloc[i]
    word_sim.append(model.similarity(line['Word 1'],line['Word 2']))
    human_sim.append(line['Human (mean)'])
list1=np.array(word_sim)
list2=np.array(human_sim)
print(1-(6*sum((list1-list2)**2)/(N*(N**2-1))))

#0.9982972326257297