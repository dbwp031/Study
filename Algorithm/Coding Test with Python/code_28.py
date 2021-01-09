import sys
n=int(input())
data = list(map(int,sys.stdin.readline().split()))
start,end = 0,n-1
target = -1
while start<=end:
    mid = (start+end)//2
    if mid == data[mid]:
        target = mid
        break
    elif mid>data[mid]:
        start=mid+1
    else:
        end=mid-1
print(target)