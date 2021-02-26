import numpy as np
import torch.nn as nn
import torch
import torch.optim as optim
from torch.utils.data import DataLoader
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import time

class DataSet:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __len__(self):
        return len(self.x)

    def __getitem__(self,index):
        return self.x[index],self.y[index]

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer=nn.Linear(300,32)
        #参考：https://www.atmarkit.co.jp/ait/articles/2002/06/news025.html
        #self.layer=nn.ReLU()
        self.layer2=nn.Linear(32,4)


    def forward(self,x):
        #breakpoint()
        out1=self.layer(x)
        out2=self.layer2(out1)
        return out2

def graph(left,x,filename):
    plt.plot(left,x)
    plt.savefig(filename)

model=NeuralNetwork()
x_train=np.loadtxt('x_train.txt')
#delimiterは区切り文字の指定
x_data=torch.tensor(x_train, dtype=torch.float32)
#上が無いと発生 AttributeError: 'numpy.ndarray' object has no attribute 'dim'

y_train = np.loadtxt('y_train.txt')
y_data = torch.tensor(y_train, dtype=torch.int64)
loss = nn.CrossEntropyLoss()

#device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
#model = model.to(device)

#勾配降下法
#dataset=DataSet(x_data.to(device),y_data.to(device))
dataset=DataSet(x_data,y_data)
op=optim.SGD(model.parameters(), lr=1e-1)
n_epoch=10
lost=[]
score=[]
score_time=[]
Bs=15
for B in range(Bs):
    B_size=2**B
    dataloader=DataLoader(dataset, batch_size=B_size)
    for epoch in range(n_epoch):
        start = time.time()
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
        score_time.append(time.time()-start)
left =np.array(range(n_epoch*Bs))

graph(left,lost,'lost.png')
graph(left,score,'score.png')
print(score_time)
"""
[
    314.1580193042755, 167.4874439239502,
    85.75188279151917, 42.10090374946594, 
    22.806607723236084, 12.258671522140503, 
    7.745054721832275, 4.5765039920806885, 
    3.181704521179199, 2.4923923015594482, 
    2.2653071880340576, 2.1441218852996826, 
    2.15779185295105, 2.195951461791992, 
    2.306753396987915
    ]
"""