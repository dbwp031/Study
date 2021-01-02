n,m = map(int,input().split())
data = list(map(int,input().split()))

num = [0]*(m+1)
for item in data:
    num[item]+=1
ans=0
print(num)

for i in range(1,len(num)):
    for _ in range(num[i]):
        if i<m:
            ans+=sum(num[i+1:])
print(ans)