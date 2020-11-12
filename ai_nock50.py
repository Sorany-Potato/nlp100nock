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

a_train, a_test = train_test_split(dataframe,test_size=0.2,shuffle=False)
print(dataframe)