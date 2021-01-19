n = int(input())
data = [(-1,-1)]
for _ in range(n):
    a,b=map(int,input().split())
    data.append((a,b))

d = [0]*17
d[0]=0

for i in range(1,n+1):
    a,b = data[i]
    d[i]= max(d[i],d[i-1])

    if i+a<=n+1:
        d[i+a-1]=max(d[i-1]+b,d[i+a-1])
    
print(d[n])

    
