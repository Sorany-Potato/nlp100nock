"""
63. 加法構成性によるアナロジー
“Spain”の単語ベクトルから”Madrid”のベクトルを引き，
”Athens”のベクトルを足したベクトルを計算し，
そのベクトルと類似度の高い10語とその類似度を出力せよ．
"""
import gensim
model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
print(model.most_similar(positive=['Spain','Athens'],negative=['Madrid'],topn=10))