inf = 1e9
maxv = -inf
minv =  inf

n = int(input())
data = []
data = list(map(int,input().split()))
cal = list(map(int,input().split())) # + - x //
a = 0
def dfs(result,cnt):
    global maxv,minv
    if cnt == n-1:
        maxv = max(maxv,result)
        minv = min(minv,result)
        return

    if cal[0] != 0:
        cal[0]-=1
        dfs(result+data[cnt+1],cnt+1)
        cal[0]+=1
    if cal[1] != 0:
        cal[1]-=1
        dfs(result-data[cnt+1],cnt+1)
        cal[1]+=1
    if cal[2] != 0:
        cal[2]-=1
        dfs(result*data[cnt+1],cnt+1)
        cal[2]+=1
    if cal[3] != 0:
        cal[3]-=1
        if result <0:
            dfs(-((-result)//data[cnt+1]),cnt+1)
        else:
            dfs(result//data[cnt+1],cnt+1)
        cal[3]+=1

dfs(data[0],0)
print(maxv)
print(minv)
