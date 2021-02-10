#勾配とは傾きのこと

import numpy as np
import torch.nn as nn
import torch
import nn_def

model=nn_def.NeuralNetwork()
train=np.loadtxt('x_train.txt')
#delimiterは区切り文字の指定
x_train=torch.tensor(train, dtype=torch.float32)
#上が無いと発生 AttributeError: 'numpy.ndarray' object has no attribute 'dim'
x_one=model(x_train[:1])
x_four=model(x_train[:4])

y_train = np.loadtxt('y_train.txt')
y_train = torch.tensor(y_train, dtype=torch.int64)
loss = nn.CrossEntropyLoss()

print(loss(x_one,y_train[:1]))
#tensor(1.3833, grad_fn=<NllLossBackward>)
print(loss(x_four,y_train[:4]))
#tensor(1.3720, grad_fn=<NllLossBackward>)
