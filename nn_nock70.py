import pandas as pd
import nn_def
from sklearn.model_selection import train_test_split

def X_data(data):#Xの取得
    result=[]
    for title,cate in zip(data['title'],data['category']):
        vec=[]
        ng=0
        words=title.split()
        for word in words:
            try:
                vec.append(model[word])
            except:
                ng+=1
        if vec:
            result.append(sum(vec)/(len(vec)))
    return result

model=nn_def.vec_model()
target=['b', 't', 'e','m']
L={'b':0, 't':1, 'e':2,'m':3}
dataset=pd.read_csv('../100nock_chapter6/tes.csv',header=None,sep='\t',names=['ID','title','url','publisher','category','story','hostname','timestamp'])

data = dataset['category'].isin(target), ['title', 'category']
dataframe = dataset.loc[data]
#    8    :     2
train_data, valid_test_data = train_test_split(dataframe,test_size=0.2,shuffle=True,random_state=123,stratify=dataframe['category'])
#    5    :     5   (20%のものから10％づつに分ける)
valid_data, test_data = train_test_split(valid_test_data,test_size=0.5,shuffle=True,random_state=123,stratify=valid_test_data['category'])

y_train=train_data.iloc[:,1].replace(L)
y_train.to_csv('y_train.txt',header=False, index=False)
y_valid=valid_data.iloc[:,1].replace(L)
y_valid.to_csv('y_valid.txt',header=False, index=False)
y_test=test_data.iloc[:,1].replace(L)
y_test.to_csv('y_test.txt',header=False, index=False)

x_train=X_data(train_data)
#print(x_train)

x_valid=X_data(valid_data)
#print(x_valid)

x_test=X_data(test_data)
#print(x_test)
