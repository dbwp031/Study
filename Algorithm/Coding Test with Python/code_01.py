n = int(input())
 
data = list(map(int,input().split()))
data = sorted(data)
ans = 0
memNum = 0

for item in data:
    if item<=memNum:
        ans+=1
        memNum = 0
    else:
        memNum+=1
print(memNum)