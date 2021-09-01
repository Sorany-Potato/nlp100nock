import torch
import rn_def

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
        y = y[:,-1,:] # 最後のステップ
        y = self.linear(y)
        y = self.softmax(y)
        return y

from torch.utils.data import Dataset

class CreateDataset(Dataset):
    def __init__(self, X, y, tokenizer):
        self.X = X
        self.y = y
        self.tokenizer = tokenizer

    def __len__(self): 
        return len(self.y)

    def __getitem__(self, index): 
        text = self.X[index]
        inputs = self.tokenizer(text)

        return {
        'inputs': torch.tensor(inputs, dtype=torch.int64),
        'labels': torch.tensor(self.y[index], dtype=torch.int64)
        }



train_data=rn_def.star('./train.txt')
vocab=rn_def.vocab_dict()
categorys=train_data[1]
train_title=train_data[2]
data_id=train_data[0]

category_dict = {'b': 0, 't': 1, 'e':2, 'm':3}
y_train = []
for word in categorys:
    y_train.append(category_dict[word])

dataset_train = CreateDataset(train_title, y_train, rn_def.idx)

print(f'len(Dataset)の出力: {len(dataset_train)}')
print('Dataset[index]の出力:')
for var in dataset_train[1]:
    print(f'  {var}: {dataset_train[1][var]}')

model=RNN()

for i in range(5):
    X=dataset_train[i+1]['inputs']
    print(torch.softmax(model(X.unsqueeze(0)),dim=-1))
'''
tensor([[0.2344, 0.2795, 0.2488, 0.2373]], grad_fn=<SoftmaxBackward>)
tensor([[0.2567, 0.2349, 0.2234, 0.2850]], grad_fn=<SoftmaxBackward>)
tensor([[0.2789, 0.2195, 0.2130, 0.2886]], grad_fn=<SoftmaxBackward>)
tensor([[0.2551, 0.2552, 0.2378, 0.2519]], grad_fn=<SoftmaxBackward>)
tensor([[0.2534, 0.2543, 0.2483, 0.2440]], grad_fn=<SoftmaxBackward>)
'''