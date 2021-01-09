import sys
n,c=map(int,input().split())
data = []
for _ in range(n):
    data.append(int(input()))
data.sort()
start = 0
end = data[-1]-data[0]

while start<=end:
    mid = (start+end)//2
    count = 1
    value = data[0]
    for i in range(1,n):
        if data[i]>=value+mid:
            value = data[i]
            count+=1
    if count >=c: # distance 가 커져야 하거나 distance가 답일때 -> 답일 때 마지막으로 조건을 만족하기 때문에 이런식으로 코드를 짤 수 있음
        result = mid
        start = mid+1
    else:
        end =mid-1
print(result)