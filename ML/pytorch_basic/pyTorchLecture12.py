import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable
#inputs=(batch_size*seq_len*input_size)
#hidden=(num_layers*batch_size*hidden_size)



#input-dimension(input size==4) helo라는 네 개의 원 핫 데이터가 한 input으로 들어가기 때문에
#hidden size=2라고 해놓으면 output은 2개의 숫자를 뱉어낸다.

#input-> shape(1,5,4): [[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]](hello) 1개의 데이터,5개의 sequence length, 4개의 알파벳 종류
#output-> shape(1,5,2)

#input이 hihell ->output을 ihello로 만들려고 한다.

device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')

num_classes=5
input_size=5 #one-hot size
hidden_size=5 #output from the cell. 바로 결과 예측을 위해서 5로 설정
batch_size=1 #sentence의 개수(단어 개수)
sequence_length=1 #이번에는 한번에 하나씩 해본다
num_layers=1 # one layer rnn이다.(아직 안 다룬 개념)

idx2char=['h','i','e','l','o']
x_data=[0,1,0,2,3,3]# hihell
one_hot_lookup=[[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]
x_one_hot = [one_hot_lookup[x] for x in x_data]

y_data=[1,0,2,3,3,4]#ihello

inputs=Variable(torch.Tensor(x_one_hot))
labels=Variable(torch.LongTensor(y_data))


class Model(nn.Module):
    def __init__(self):
        super(Model,self).__init__()
        self.rnn=nn.RNN(input_size=input_size,hidden_size=hidden_size,batch_first=True)

    def forward(self,x,hidden):
        #input x 를 (batch_size,sequence_length,input_size)로 reshape함
        #just for make sure
        x=x.view(batch_size,sequence_length,input_size)

        #Propagate input through RNN
        #Input:(batch,seq_len,input_size)
        out,hidden=self.rnn(x,hidden)
        #for make sure, output이 N*5 shape을 따르게 하기 위해서
        out=out.view(-1,num_classes)
        return hidden,out

    def init_hidden(self):
        #initialize hidden and cell states
        return Variable(torch.zeros(num_layers,batch_size,hidden_size).to(device))

model=Model().to(device)
print(model)

criterion=nn.CrossEntropyLoss()
optimizer=torch.optim.Adam(model.parameters(),lr=0.1)

for epoch in range(100):
    optimizer.zero_grad()
    loss=0
    hidden=model.init_hidden()

    print("predicted string : ",end="")
    
    for input_,label in zip(inputs,labels):
        inputs= inputs.to(device)

        hidden,output=model(hidden,input_)
        val,idx=output.max(1)

        print(idx2char[idx.data[0]],end="")
        loss+=criterion(output,torch.LongTensor([label]))

    print(", epoch: %d, loss: %1.3f" %(epoch+1,loss.data))
    loss.backward()
    optimizer.step()

print("Learning finished!")