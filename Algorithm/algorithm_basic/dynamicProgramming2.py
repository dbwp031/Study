n=int(input())
data=list(map(int,input().split()))
d=[0]*(n+1)

data.insert(0,0)
d[1]=data[1]
d[2]=max(data[1],data[2])

for i in range(3,n+1):
  d[i]=max(d[i-1],d[i-2]+data[i])

print(max(d))
