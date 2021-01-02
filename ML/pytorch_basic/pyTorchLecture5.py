import torch
import torch.nn.functional as F
from torch.autograd import Variable
x_data=Variable(torch.Tensor([[1.0],[2.0],[3.0],[4.0]]))
y_data=Variable(torch.Tensor([[0.0],[0.0],[1.0],[1.0]]))
#3x1

class Model(torch.nn.Module):
    def __init__(self):
        super(Model,self).__init__()
        self.linear=torch.nn.Linear(1,1)#input size,output size 

    def forward(self,x):
        y_pred= F.sigmoid(self.linear(x))
        return y_pred

model=Model()

criterion= torch.nn.BCELoss(size_average=False)
#MSELoss:mean squared error loss
#BCELoss:Binary Cross Entropy loss
optimizer=torch.optim.SGD(model.parameters(),lr=0.01)#stochastic gradient descent
#참고
#전체 데이터:Batch
#일부 데이터:Mini-Batch
#BGD(Batch Gradient Descent)는 하나의 step을 위햏 전체 데이터를 계산 하므로 계산량이 많음
#SGD(Stochastic Gradient Descent)sms Mini-Batch를 사용/계산 속도가 훨씬 빨라 같은 시간에 더 많은 step을 나아갈 수 있음
#Local Minima에 빠지지 않고 Global Minima에 수렴할 가능성이 더 높음.
for epoch in range(1000):
    y_pred=model(x_data)#model(x)

    loss=criterion(y_pred,y_data)#critenrion=torch.nn.MSELoss()
    print(epoch,loss.data)#버전이 높아 data[0]일시 오류. data로 사용해야함.

    optimizer.zero_grad() 
    #모든 매개변수의 변화도 버퍼(gradient buffer)를 0으로 설정
    loss.backward()
    #loss=torch.nn.MsELoss()(y_pred,y_data)
    #오차(error)를 역전파하기 위해 loss.backward() 기존 변화도를 없애는 작업이 필요한데,
    #  그렇지 않으면 변화도가 기존의 것에 누적되기 때문이다.
    optimizer.step()

hour_var=Variable(torch.Tensor([[1.0]]))
#mseloss
#print("predict (after traning)",4,model.forward(hour_var).data[0][0])
print("predict 1 hour", model(hour_var).data.item()>0.5)
hour_var=Variable(torch.Tensor([7.0]))
print("predict 7 hours",7.0,model(hour_var).item()>0.5)