#An=An-2 * 2 + An-1(A1=1,A2=3)


n=int(input())
d=[0]*1001

d[1]=1
d[2]=3
for i in range(3,n+1):
  d[i]=d[i-1]+d[i-2]*2
print(d)
print(d[n]%796796)
