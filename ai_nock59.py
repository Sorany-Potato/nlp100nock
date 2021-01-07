"""
59. ハイパーパラメータの探索Permalink
学習アルゴリズムや学習パラメータを変えながら，
カテゴリ分類モデルを学習せよ．
検証データ上の正解率が最も高くなる
学習アルゴリズム・パラメータを求めよ．
また，その学習アルゴリズム・パラメータを用いたときの
評価データ上の正解率を求めよ．
"""
import ai_def
import numpy as np
from tqdm import tqdm
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt

log=ai_def.Lg()

def over(C,class_weight):
    clf = LogisticRegression(C=C, solver=solver, class_weight=class_weight)
    clf.fit(log['train_feature'], log['train_category'])
    train_sc=ai_def.estimation(clf, log['train_feature'])
    valid_sc=ai_def.estimation(clf, log['valid_feature'])
    test_sc=ai_def.estimation(clf, log['test_feature'])
    result=[]
    result.append(accuracy_score(log['train_category'],train_sc))
    result.append(accuracy_score(log['valid_category'],valid_sc))
    result.append(accuracy_score(log['test_category'],test_sc))
    return result

C=np.longspace(-5,4,10,base=10)
class_weight=[None, 'balanced']
best_parameter=None
best_scores=None
max_valid_score=0