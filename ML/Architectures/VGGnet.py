#container 1
from keras.datasets import cifar10
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable
from torchvision import datasets, transforms

transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

trainset = datasets.CIFAR10(root='./data', train=True,
                                        download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,
                                          shuffle=True, num_workers=0)

testset = datasets.CIFAR10(root='./data', train=False,
                                       download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=4,
                                         shuffle=False, num_workers=0)

classes = ('plane', 'car', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

batch_size=64


##container 2

#image size: 32*32*3

class Net(nn.Module):
    
    def __init__(self):
        super(Net,self).__init__()
        self.conv1= nn.Conv2d(3,64,kernel_size=3,padding=1,padding_mode='zeros')
        self.conv2= nn.Conv2d(64,128,kernel_size=3,padding=1,padding_mode='zeros')
        self.conv3= nn.Conv2d(128,256,kernel_size=3,padding=1,padding_mode='zeros')
        self.conv4= nn.Conv2d(256,256,kernel_size=3,padding=1,padding_mode='zeros')
        self.conv5= nn.Conv2d(256,512,kernel_size=3,padding=1,padding_mode='zeros')
        self.conv6= nn.Conv2d(512,512,kernel_size=3,padding=1,padding_mode='zeros')

        self.fc1=nn.Linear(512,84)
        self.fc2=nn.Linear(84,84)
        self.fc3=nn.Linear(84,10)

        self.mp=nn.MaxPool2d(kernel_size=2,stride=2)
    
    def forward(self,x):
        in_size=x.size(0)
        #32*32*3
        x=F.relu(self.mp(self.conv1(x)))
        #16*16*64
        x=F.relu(self.mp(self.conv2(x)))
        #8*8*128
        x=self.conv3(x)
        #8*8*256
        x=F.relu(self.mp(self.conv4(x)))
        #4*4*512
        x=self.conv5(x)
        #4*4*512
        x=F.relu(self.mp(self.conv6(x)))
        #2*2*512
        x=self.conv6(x)
        #2*2*512
        x=F.relu(self.mp(self.conv6(x)))
        #1*1*512
        x=x.view(in_size,-1)
        x=F.relu(self.fc1(x))
        x=F.relu(self.fc2(x))
        x=F.relu(self.fc3(x))
        x=F.log_softmax(x)

        return x

model=Net()
optimizer= optim.SGD(model.parameters(),momentum=0.9,lr=0.01)

def train(epoch):
    model.train()
    for batch_idx,(data,target) in enumerate(trainloader):
        data, target=Variable(data),Variable(target)
        optimizer.zero_grad()
        output=model(data)
        loss=F.nll_loss(output,target)
        loss.backward()
        optimizer.step()
        if batch_idx % 10 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(trainloader.dataset),
                100. * batch_idx / len(trainloader), loss.data))
        torch.optim.lr_scheduler.ReduceLROnPlateau(patience=10)

def test():
    model.eval()
    test_loss = 0
    correct = 0
    for data, target in testloader:
        data, target = Variable(data, volatile=True), Variable(target)
        output = model(data)
        # sum up batch loss
        test_loss += F.nll_loss(output, target, size_average=False).data
        # get the index of the max log-probability
        pred = output.data.max(1, keepdim=True)[1]
        correct += pred.eq(target.data.view_as(pred)).cpu().sum()

    test_loss /= len(testloader.dataset)
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(testloader.dataset),
        100. * correct / len(testloader.dataset)))

for epoch in range(1, 10):
    train(epoch)
    test()

        