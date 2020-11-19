"""
51. 特徴量抽出
学習データ，検証データ，評価データから特徴量を抽出し，それぞれ
train.feature.txt，
valid.feature.txt，
test.feature.txt
というファイル名で保存せよ． 
なお，カテゴリ分類に有用そうな特徴量は各自で自由に設計せよ．
記事の見出しを単語列に変換したものが
最低限のベースラインとなるであろう．
"""
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def title(filename):
    file_path='./'+str(filename)
    data=pd.read_csv(file_path,header=None,sep='\t',names=['TITLE','CATEGORY'])
    result=data.TITLE
    return result

def tfidf(frame):
    train=frame[0]
    valid=frame[1]
    test=frame[2]
    vectorizer=TfidfVectorizer(ngram_range=(1,2))
    dataframe=pd.concat([train,valid,test])
    vectorizer.fit(dataframe)
    #ベクトル化
    train_result=vectorizer.transform(train)
    valid_result=vectorizer.transform(valid)
    test_result=vectorizer.transform(test)
    #ベクトルをデータフレームに
    train_result=pd.DataFrame(train_result.toarray(),columns=vectorizer.get_feature_names())
    valid_result=pd.DataFrame(valid_result.toarray(),columns=vectorizer.get_feature_names())
    test_result=pd.DataFrame(test_result.toarray(),columns=vectorizer.get_feature_names())
    #保存
    train_result.to_csv('./train.feature.txt',sep='\t',index=False)
    valid_result.to_csv('./valid.feature.txt',sep='\t',index=False)
    test_result.to_csv('./test.feature.txt',sep='\t',index=False)

#main
filenames=['train.txt','valid.txt','test.txt']
title_frame=[]
for name in filenames:
    title_frame.append(title(name))
prin=tfidf(title_frame)
