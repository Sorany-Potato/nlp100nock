"""
56. 適合率，再現率，F1スコアの計測
52で学習したロジスティック回帰モデルの適合率，
再現率，F1スコアを，評価データ上で計測せよ．
カテゴリごとに適合率，再現率，F1スコアを求め，
カテゴリごとの性能をマイクロ平均
（micro-average）とマクロ平均（macro-average）で統合せよ．
"""                         #適合率           再現率        F1スコア
from sklearn.metrics import precision_score, recall_score, f1_score
import ai_def
import numpy as np
import pandas as pd

log=ai_def.Lg()
clf=ai_def.load_model()
test_score=ai_def.estimation(clf,log['test_feature'])
precision = precision_score(log['test_category'],test_score,average=None, labels=['b','e','t','m'])
precision = np.append(precision,precision_score(log['test_category'],test_score,average='micro'))
precision = np.append(precision,precision_score(log['test_category'],test_score,average='micro'))

recall = recall_score(log['test_category'],test_score,average=None,labels=['b','e','t','m'])
recall = np.append(recall,recall_score(log['test_category'],test_score,average='micro'))
recall = np.append(recall,recall_score(log['test_category'],test_score,average='macro'))

f1 = f1_score(log['test_category'],test_score,average=None,labels=['b','e','t','m'])
f1 = np.append(f1,f1_score(log['test_category'],test_score,average='micro'))
f1 = np.append(f1,f1_score(log['test_category'],test_score,average='macro'))

scores= pd.DataFrame({'適合率': precision,'再現率': recall,'F1スコア': f1},
                    index=['b','e','t','m','マイクロ平均','ミクロ平均'])
print(scores)