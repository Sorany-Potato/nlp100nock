"""
情報源（publisher）が”Reuters”, “Huffington Post”, “Businessweek”,
“Contactmusic.com”, “Daily Mail”の事例（記事）のみを抽出する．
※Reuterのみをとる※
抽出された事例をランダムに並び替える．
抽出された事例の80%を学習データ，残りの10%ずつを検証データと評価データに分割し，それぞれtrain.txt，valid.txt，test.txtというファイル名で保存する．ファイルには，１行に１事例を書き出すこととし，カテゴリ名と記事見出しのタブ区切り形式とせよ（このファイルは後に問題70で再利用する）．
学習データと評価データを作成したら，各カテゴリの事例数を確認せよ．
"""
import pandas as pd
from sklearn.model_selection import train_test_split

target=['Reuters', 'Huffington Post', 'Businessweek',
'Contactmusic.com', 'Daily Mail']
dataset=pd.read_csv('NewsAggregatorDataset/newsCorpora.csv',header=None,sep='\t',names=['ID','title','url','publisher','category','story','hostname','timestamp'])
# dataset['publisher']

data = dataset['publisher'].isin(['Reuters', 'Huffington Post', 'Businessweek','Contactmusic.com', 'Daily Mail']), ['title', 'category']
dataframe = dataset.loc[data]
#    8    :     2
train_data, valid_test_data = train_test_split(dataframe,test_size=0.2,shuffle=True,random_state=123,stratify=dataframe['category'])
#    5    :     5   (20%のものから10％づつに分ける)
valid_data, test_data = train_test_split(valid_test_data,test_size=0.5,shuffle=True,random_state=123,stratify=valid_test_data['category'])
train_data.to_csv('./train.txt',sep='\t',index=False)
valid_data.to_csv('./valid.txt',sep='\t',index=False)
test_data.to_csv('./test.txt',sep='\t',index=False)
print('【学習データ】')
print(train_data['category'].value_counts())
print('【検証データ】')
print(valid_data['category'].value_counts())
print('【評価データ】')
print(test_data['category'].value_counts())