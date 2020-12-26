"""
55. 混同行列の作成
52で学習したロジスティック回帰モデルの混同行列
（confusion matrix）を，
学習データおよび評価データ上で作成せよ
"""
from sklearn.metrics import confusion_matrix
import ai_def

log=ai_def.Lg()
clf=ai_def.load_model()
train_score=ai_def.estimation(clf,log['train_feature'])
train_matrix = confusion_matrix(log['train_category'],train_score)
print(train_matrix)
test_score=ai_def.estimation(clf,log['test_feature'])
test_matrix = confusion_matrix(log['test_category'],test_score)
print(test_matrix)
