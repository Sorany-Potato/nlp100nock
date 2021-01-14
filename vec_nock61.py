"""
61. 単語の類似度
“United States”と”U.S.”のコサイン類似度を計算せよ．
"""
import gensim
model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
print(model.similarity('United_States','U.S.'))