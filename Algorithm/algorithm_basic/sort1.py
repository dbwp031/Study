import sys

def binary_search(array,target,start,end):
  if start>end:
    return None
  else:
    mid=(start+end)//2
    if array[mid]==target:
      return mid
    elif array[mid]<target:
      return binary_search(array,target,mid+1,end)
    else:
      return binary_search(array,target,start,mid-1)


n=int(input())
data=list(map(int, sys.stdin.readline().rstrip().split()))
data.sort()
m=int(input())
need=list(map(int,sys.stdin.readline().rstrip().split()))
for i in range(m):
  result=binary_search(data,need[i],0,n-1)
  if result== None:
    print('no',end=' ')
  else:
    print('yes',end=' ')
