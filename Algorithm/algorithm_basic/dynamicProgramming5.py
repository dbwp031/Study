#my code
n,m=list(map(int,input().split()))
data=[]
for i in range(n):
  data.append(int(input()))
d=[0]*10001

check=list(data)
cnt=1
for x in check:
  d[x]=cnt
start=0
end=len(check)
while(True):
  cnt+=1
  for i in data:
    for j in range(start,end):
      f=i+check[j]
      if d[f]==0:
        d[f]=cnt
        check.append(f)

  if d[m]!=0:
    print(d[m])
    break
  if (data[0]+check[end])>m:
    print(-1)
    break
  start=end
  end=len(check)

#book code
n,m=map(int,input().split())
array=[]
for i in range(n):
  array.append(int(input()))

  d=[10001]*(m+1)

d[0]=0
for i in range(n):
  for j in range(array[i],m+1):
    d[j]=min(d[j],d[j-array[i]]+1)

if d[m]== 10001:
  print(-1)
else:
  print(d[m])
