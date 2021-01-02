n,m=map(int,input().split())
data=[]
for i in range( n):
  data.append(list(map(int,input().split())))
a=[]
for i in range(len(data)):
  a.append(min(sorted(data[i])))
print(max(a))
