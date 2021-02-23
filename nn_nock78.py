import numpy as np
import torch.nn as nn
import torch
import torch.optim as optim
from torch.utils.data import DataLoader
import nn_def
import time

class DataSet:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __len__(self):
        return len(self.x)

    def __getitem__(self,index):
        return self.x[index],self.y[index]

model=nn_def.NeuralNetwork()
x_train=np.loadtxt('x_train.txt')
#delimiterは区切り文字の指定
x_data=torch.tensor(x_train, dtype=torch.float32)
#上が無いと発生 AttributeError: 'numpy.ndarray' object has no attribute 'dim'

y_train = np.loadtxt('y_train.txt')
y_data = torch.tensor(y_train, dtype=torch.int64)
loss = nn.CrossEntropyLoss()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

#勾配降下法
dataset=DataSet(x_data.to(device),y_data.to(device))
op=optim.SGD(model.parameters(), lr=1e-1)
n_epoch=1
score=[]
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
    score.append(time.time()-start)
print(score)
