"""
64. アナロジーデータでの実験
単語アナロジーの評価データをダウンロードし，
vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算し
そのベクトルと類似度が最も高い単語と，その類似度を求めよ．
求めた単語と類似度は，各事例の末尾に追記せよ．
"""
import gensim
model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
result=[]
with open('questions-words.txt') as f:
    for line in f:
        word=line.split()
        if len(word)>=3:
            word_sim=model.most_similar(positive=[word[1],word[2]],negative=[word[0]],topn=1)
            result.append([line,word_sim])
print(result)
