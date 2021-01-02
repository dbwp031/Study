N,M,K=map(int,input().split())
data=list(map(int,input().split()))
data.sort()
first=data[N-1]
second=data[N-2]
sum=M//(K+1)*(K*first+1*second)+M%(K+1)*first
print(sum)
