from __future__ import print_function
import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.autograd import Variable

batch_size=64

train_dataset=datasets.MNIST(root='./data2/',
                            train=True,
                            transform=transforms.ToTensor(),
                            download=True)

test_dataset= datasets.MNIST(root='./data2/',
                            train=False,
                            transform=transforms.ToTensor())

train_loader=torch.utils.data.DataLoader(dataset=train_dataset,
                                        batch_size=batch_size,
                                        shuffle=True)

test_loader=torch.utils.data.DataLoader(dataset=test_dataset,
                                        batch_size=batch_size,
                                        shuffle=False)


class Net(nn.Module):
    def __init__(self):
        super(Net,self).__init__()
        self.conv1=nn.Conv2d(1,10,kernel_size=5)##in_channels,out_channels -> depth
        #28*28-*1>24*24*10->12*12*10 max pooling 은 아래에서 되는데 아래에 적어도 다 적용이 되는건가?
        #forward에서 mp(conv1) 하고 mp(conv2) 를 하기 때문에 그런것이다. 즉 위 질문에 대한 대답은 false.
        #결국 init에는 함수만 만들어주고 실제 사용하는것은 forward 부분이다.
        self.conv2=nn.Conv2d(10,20,kernel_size=5)
        #12*12*10->8*8*20->4*4*20=320
        self.mp=nn.MaxPool2d(2)
        self.fc=nn.Linear(320,10)    
    def forward(self,x):
        in_size=x.size(0)
        x=F.relu(self.mp(self.conv1(x)))
        x=F.relu(self.mp(self.conv2(x)))
        x=x.view(in_size,-1)
        x=self.fc(x)
        return F.log_softmax(x)##softmax를 해서 주는 이유가 뭐지? 그냥 CNN 써버리면 되는거아닌가?

model=Net()
optimizer=optim.SGD(model.parameters(),lr=0.01,momentum=0.5)

def train(epoch):
    model.train()
    for batch_idx, (data,target) in enumerate(train_loader):
        data,target=Variable(data),Variable(target)
        optimizer.zero_grad()
        output=model(data)
        loss=F.nll_loss(output,target)
        loss.backward()
        optimizer.step()
        if batch_idx%10 ==0:
            print('Train Epoch:{} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch,batch_idx*len(data),len(train_loader.dataset),
                100.*batch_idx/len(train_loader),loss.item()))
def test():
    model.eval()
    test_loss=0
    correct = 0
    for data,target in test_loader:
        data, target = Variable(data, volatile=True),Variable(target)
        output=model(data)
        test_loss=F.nll_loss(output,target,size_average=False).data
        pred=output.data.max(1,keepdim=True)[1]
        correct+=pred.eq(target.data.view_as(pred)).cpu().sum()

    test_loss/=len(test_loader.dataset)

    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f})%\n'.format(
            test_loss,correct,len(test_loader.dataset),100.*correct/len(test_loader.dataset)
        ))

for epoch in range(1,10):
    train(epoch)
    test()