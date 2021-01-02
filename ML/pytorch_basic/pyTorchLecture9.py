import torch
#Cross entropy example
import numpy as np
#One hot
#0: 100
#1: 010
#2: 001

Y=np.array([1,0,0])

Y_pred1=np.array([0.7,0.2,0.1])
Y_pred2=np.array([0.1,0.3,0.6])

print("loss1= ",np.sum(-Y*np.log(Y_pred1)))
print("loss2= ",np.sum(-Y*np.log(Y_pred2)))

#---------------------------------------------
#Softmax + CrossEntropy (logSoftmax +NLLLoss)
loss=nn.CrossEntropyLoss()
#loss(logit,class ==(Variable(~~~)))
