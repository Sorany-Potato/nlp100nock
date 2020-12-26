"""
58. 正則化パラメータの変更
ロジスティック回帰モデルを学習するとき，
正則化パラメータを調整することで，
学習時の過学習（overfitting）の度合いを制御できる．
異なる正則化パラメータでロジスティック回帰モデルを学習し，
学習データ，検証データ，および評価データ上の正解率を求めよ．
実験の結果は，正則化パラメータを横軸，
正解率を縦軸としたグラフにまとめよ．
"""
import ai_def
import numpy as np
from tqdm import tqdm
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt

log=ai_def.Lg()
result=[]

for C in tqdm(np.logspace(-5,4,10,base=10)):
    lg=LogisticRegression(random_state=123, max_iter=10000, C=C)
    clf=lg.fit(log['train_feature'], log['train_category'])

    train_sc=ai_def.estimation(clf, log['train_feature'])
    valid_sc=ai_def.estimation(clf, log['valid_feature'])
    test_sc=ai_def.estimation(clf, log['test_feature'])

    train_accuracy = accuracy_score(log['train_category'],train_sc)
    valid_accuracy = accuracy_score(log['valid_category'],valid_sc)
    test_accuracy = accuracy_score(log['test_category'],test_sc)

    result.append([C,train_accuracy, valid_accuracy, test_accuracy])

result=np.array(result).T
plt.plot(result[0],result[1], label='train')
plt.plot(result[0],result[2], label='valid')
plt.plot(result[0],result[3], label='test')
plt.ylim(0,1.1)
plt.ylabel('Accuracy')
plt.xscale('log')
plt.xlabel('C')
plt.legend()
plt.savefig('img.png')
