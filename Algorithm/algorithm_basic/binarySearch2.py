import sys

n = int(input())
data = list(map(int,sys.stdin.readline().split()))
m = int(input())
offer = list(map(int,sys.stdin.readline().split()))

def recursive(start,end,target):
    mid = (start+end)//2
    if start>end: return -1
    if data[mid] == target:
        return mid
    elif data[mid]<target:
        return recursive(mid+1,end,target)
    elif data[mid]>target:
        return recursive(start,mid-1,target)

def loop(start,end,target):
    while start<=end:
        mid = (start+end)//2
        if data[mid]==target:
            return mid
        elif data[mid]<target:
            start=mid+1
        elif data[mid]>target:
            end=mid-1
    return -1


for item in offer:
    if loop(0,n-1,item) == -1:
        print('no',end=' ')
    else:
        print('yes',end=' ')
    