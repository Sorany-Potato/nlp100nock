"""
行列W∈Rd×Lは単層ニューラルネットワークの重み行列で，
ここではランダムな値で初期化すればよい
（問題73以降で学習して求める）．
"""

import numpy as np
import torch.nn as nn
import torch

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer=nn.Linear(300,4,bias=False)
        #参考：https://www.atmarkit.co.jp/ait/articles/2002/06/news025.html

    def forward(self,x):
        #breakpoint()
        output=self.layer(x)
        return output

model=NeuralNetwork()
train=np.loadtxt('x_train.txt')
#delimiterは区切り文字の指定
x_train=torch.tensor(train, dtype=torch.float32)
#上が無いと発生 AttributeError: 'numpy.ndarray' object has no attribute 'dim'
x_one=model(x_train[:1])
print(nn.Softmax(x_one))
x_four=model(x_train[:4])
print(nn.Softmax(x_four))

"""
Softmax(dim=tensor([[ 0.0107,  0.0271,  0.0059, -0.0134]], grad_fn=<MmBackward>))
Softmax(
    dim=tensor([[ 0.0107,  0.0271,  0.0059, -0.0134],
            [-0.0246,  0.0353, -0.0040, -0.0291],
            [-0.0431, -0.0621, -0.0148, -0.0319],
            [-0.0143, -0.0468,  0.0492,  0.0335]], grad_fn=<MmBackward>)
)
"""