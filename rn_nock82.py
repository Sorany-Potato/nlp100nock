import numpy as np
import pickle
import torch
import torch.optim as optim
from torch.utils.data import DataLoader
import rn_def
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt

def save_model(clf):
    pickle.dump(clf, open('./TF_model.sav','wb'))
    #毎回学習しては時間がかかるのでモデルを保存

def load_model():
    file_path='TF_model.sav'
    return pickle.load(open(file_path,'rb'))

class RNN(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.emb = torch.nn.Embedding(len(vocab)+1,300)
        self.rnn = torch.nn.RNN(300,50,batch_first=True)
        self.linear = torch.nn.Linear(50,4)
        self.softmax = torch.nn.Softmax()
    def forward(self, x, h=None):
        x = self.emb(x)
        y, h = self.rnn(x, h)
        y = y[:,-1,:] # 最後のステップdime
        y = self.linear(y)
        #y = self.softmax(y)
        return y

def category_id(categorys):# ラベルベクトルの作成
    category_dict = {'b': 0, 't': 1, 'e':2, 'm':3}
    y_train = []
    for word in categorys:
        y_train.append(category_dict[word])
    return y_train


train_data=rn_def.star('./train.txt')
vocab=rn_def.vocab_dict()
categorys=train_data[1]
train_title=train_data[2]
data_id=train_data[0]

valid_data=rn_def.star('./valid.txt')
valid_categorys=valid_data[1]
valid_title=valid_data[2]
valid_data_id=valid_data[0]

test_data=rn_def.star('./test.txt')
test_categorys=test_data[1]
test_title=test_data[2]
test_data_id=test_data[0]


# Datasetの作成
dataset_train = rn_def.CreateDataset(train_title, category_id(categorys), rn_def.idx)
dataset_valid = rn_def.CreateDataset(valid_title, category_id(valid_categorys), rn_def.idx)
dataset_test = rn_def.CreateDataset(test_title, category_id(test_categorys), rn_def.idx)
model=RNN()


















# DataLoaderを作成
loader = DataLoader(dataset_train, batch_size=1, shuffle=True)

loss_fn = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)
y_data=torch.tensor(category_id(categorys)[0],dtype=torch.int64)   
lost=[]
score=[]
x_result=[]
for epoch in range(5):
    count=0
    for datas in loader:
        count+=1
        print(count)
        xx=datas['inputs']
        yy=datas['labels']
        y_pred = model(xx)
        loss = loss_fn(y_pred, yy)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        break;
    for i in range(len(dataset_train)):    
        x_result=model(dataset_train[i]['inputs'].unsqueeze(0))
        count+=100000
        print(count)
        break;
    breakpoint()
    lost.append(loss_fn(x_result,y_data))
    x=np.argmax(x_result.data.numpy(),axis=1)
    score.append(accuracy_score(x,category_id(categorys)))
left =np.array(range(n_epoch))
plt.plot(left,score)
plt.savefig('score_img.png')
#save_model(clf)