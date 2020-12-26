"""
57. 特徴量の重みの確認
52で学習したロジスティック回帰モデルの中で，
重みの高い特徴量トップ10と，
重みの低い特徴量トップ10を確認せよ．
"""
import ai_def
import numpy as np
import pandas as pd
log=ai_def.Lg()
clf=ai_def.load_model()

features=log['train_feature'].columns.values
index=[i for i in range(1,11)]
for clas,coef in zip(clf.classes_, clf.coef_):
    print(f'カテゴリ[{clas}]')
    top=pd.DataFrame(features[np.argsort(coef)[::-1][:10]], columns=['top10'], index=index).T
    worst=pd.DataFrame(features[np.argsort(coef)[:10]], columns=['worst10'], index=index).T
    print(pd.concat([top,worst], axis=0))
    print('\n')
