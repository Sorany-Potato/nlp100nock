import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
def title(filename):
    file_path='./'+str(filename)
    data=pd.read_csv(file_path,header=None,sep='\t',names=['TITLE','CATEGORY'])
    result=data.TITLE
    return result

def Vect(frame):
    train=frame[0]
    valid=frame[1]
    test=frame[2]
    vectorizer=TfidfVectorizer()
    dataframe=pd.concat([train,valid,test])
    vectorizer.fit(dataframe)
    #ベクトル化
    train_result=vectorizer.transform(train)
    valid_result=vectorizer.transform(valid)
    test_result=vectorizer.transform(test)
    #ベクトルをデータフレームに
    train_frame=pd.DataFrame(train_result.toarray(),columns=vectorizer.get_feature_names())
    valid_frame=pd.DataFrame(valid_result.toarray(),columns=vectorizer.get_feature_names())
    test_frame=pd.DataFrame(test_result.toarray(),columns=vectorizer.get_feature_names())
    #保存
    train_frame.to_csv('./train.feature.txt',sep='\t',index=False)
    valid_frame.to_csv('./valid.feature.txt',sep='\t',index=False)
    test_frame.to_csv('./test.feature.txt',sep='\t',index=False)

def Lg():
    data_set=[]
    file_pass=['./train.txt','./valid.txt','./test.txt']
    feature_pass=['./train.feature.txt','./valid.feature.txt','./test.feature.txt']

    for category,feature in zip(file_pass,feature_pass):
        fe_table=pd.read_table(feature)
        ca_table=pd.read_table(category,header=None,names=['title','category'])['category']
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
    pickle.dump(clf, open('./TF_model.sav','wb'))

def estimation(clf,feature):
    result=clf.predict(feature)
    return result

def load_model():
    file_path='TF_model.sav'
    return pickle.load(open(file_path,'rb'))