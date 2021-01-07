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

log=ai_def.Lg()

def over(C,solver,class_weight):
    clf = LogisticRegression(C=C, solver=solver, class_weight=class_weight)
    clf.fit(log['train_feature'], log['train_category'])
    train_sc=ai_def.estimation(clf, log['train_feature'])
    valid_sc=ai_def.estimation(clf, log['valid_feature'])
    test_sc=ai_def.estimation(clf, log['test_feature'])
    train_accuracy = accuracy_score(log['train_category'],train_sc)
    valid_accuracy = accuracy_score(log['valid_category'],valid_sc)
    test_accuracy = accuracy_score(log['test_category'],test_sc)
    result=[]
    result.append([C,train_accuracy, valid_accuracy, test_accuracy])
    return result

C=np.logspace(-5,4,10,base=10)
class_weight=[None, 'balanced']
solver=['newton-cg','lbfgs','liblinear','sag','saga']
best_parameter=None
best_score=None
max_score=0

for c in C:
    for solve in solver:
        for weight in class_weight:
            print(c, solve, weight)
            result=over(c,solve,weight)
            if result[0][1] > max_score:
                max_score=result[0][1]
                best_parameter=[c,solve,weight]
                best_score=result
                ai_def.plot(result[0])
print(best_parameter)
print(best_score)
print(best_score[0][2])
