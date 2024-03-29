import numpy as np
import torch.nn as nn
import torch
import torch.optim as optim
from torch.utils.data import DataLoader
import nn_def
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

class DataSet:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __len__(self):
        return len(self.x)

    def __getitem__(self,index):
        return self.x[index],self.y[index]

def graph(left,x,filename):
    plt.plot(left,x)
    plt.savefig(filename)


model=nn_def.NeuralNetwork()
x_train=np.loadtxt('x_train.txt')
#delimiterは区切り文字の指定
x_data=torch.tensor(x_train, dtype=torch.float32)
#上が無いと発生 AttributeError: 'numpy.ndarray' object has no attribute 'dim'

y_train = np.loadtxt('y_train.txt')
y_data = torch.tensor(y_train, dtype=torch.int64)
loss = nn.CrossEntropyLoss()

dataset=DataSet(x_data,y_data)
dataloader=DataLoader(dataset, batch_size=1)
#勾配降下法
op=optim.SGD(model.parameters(), lr=1e-1)
n_epoch=10
score=[]
lost=[]
for epoch in range(n_epoch):
    for xx,yy in dataloader:
        pred=model(xx)
        quad = loss(pred,yy)
        op.zero_grad()
        quad.backward()
        op.step()
    x_result=model(x_data)
    lost.append(loss(x_result,y_data))
    x=np.argmax(x_result.data.numpy(),axis=1)
    score.append(accuracy_score(x,y_data))
left =np.array(range(n_epoch))

#graph(left,lost,'lost.png')
graph(left,score,'score.png')
"""
plt.plot(left,score)
plt.savefig('score_img.png')
"""
