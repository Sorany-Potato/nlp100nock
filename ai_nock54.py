"""
54. 正解率の計測
52で学習したロジスティック回帰モデルの正解率を，
学習データおよび評価データ上で計測せよ．
"""
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import ai_def
import numpy as np

log=ai_def.Lg()
clf=ai_def.load_model()
train_score=ai_def.estimation(clf,log['train_feature'])
test_score=ai_def.estimation(clf,log['test_feature'])
train_accuracy = accuracy_score(log['train_category'],train_score)
test_accuracy = accuracy_score(log['test_category'],test_score)

print('train',train_accuracy)
print('test',test_accuracy)