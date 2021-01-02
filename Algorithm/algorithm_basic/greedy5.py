#first code
N,M=map(int,input().split())
data=(list(map(int,input().split())))
cnt=0
for i in range(0,len(data)-1):
  for j in range(i+1,len(data)):
    if(data[i]!=data[j]):
      cnt+=1
print(cnt)

#second code
N,M=map(int,input().split())
data=(list(map(int,input().split())))
result = 0

array=[0]*11
for i in range(N):
  array[data[i]]+=1
print(array)
for i in range(N):
  if(i!=10):
    if(array[i]>0):
      result+=array[i]*sum(array[i+1:])
print(result)

