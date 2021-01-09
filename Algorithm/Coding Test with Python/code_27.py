import sys
n,x=map(int,input().split())
data = list(map(int,sys.stdin.readline().split()))

start,end = 0,n-1
x_idx = -1
while start<=end:
    mid = (start+end)//2
    if x == data[mid]:
        x_idx = mid
        break
    elif x <data[mid]:
        end = mid-1
    else:
        start = mid+1
if x_idx == -1:
    print(-1)
else:
    x_start ,x_end = x_idx,x_idx
    while(data[x_start]==x):
        x_start-=1
    while(data[x_end]==x):
        x_end+=1
    print(x_end-x_start-1)