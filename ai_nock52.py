"""
52. 学習
51で構築した学習データを用いて，
ロジスティック回帰モデルを学習せよ．
"""
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
def Lg():
    data_set=[]
    file_pass=['./train.txt','./valid.txt','./test.txt']
    feature_pass=['./train.feature.txt','./valid.feature.txt','./test.feature.txt']

    for category,feature in zip(file_pass,feature_pass):
        fe_table=pd.read_table(feature)
        ca_table=pd.read_table(category)['category']
        data=(fe_table,ca_table)
        data_set.append(data)
    re_data={
        'train_feature':data_set[0][0],
        'train_category':data_set[0][1],
        'valid_feature':data_set[1][0],
        'valid_category':data_set[1][1],
        'test_feature':data_set[2][0],
        'test_category':data_set[2][1]
    }#岡氏の便利そうなんで拝借
    return re_data

def save_model(clf):
    pickle.dump(model, open('./TF_model.sav','wb'))

log=Lg()
clf=LogisticRegression(random_state=123,max_iter=10000)
clf.fit(log['train_feature'],log['train_category'])
print(clf)
save_model(clf)