"""
53. 予測
52で学習したロジスティック回帰モデルを用い，
与えられた記事見出しからカテゴリと
その予測確率を計算するプログラムを実装せよ．
"""
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import ai_def

def estimation(clf,feature):
    result=clf.predict(feature)
    return result

def load_model():
    file_path='./TF_model.sav'
    return pickle.load(open(file_path,'rb'))

log=ai_def.Lg()
clf=load_model()
print(estimation(clf,log['train_feature']))