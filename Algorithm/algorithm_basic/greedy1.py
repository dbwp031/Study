n=int(input())
data=list(map(int,input().split()))
data.sort()
re=list(data)
re.reverse()
target=data[0]
focus=0
result=0
extranum=0
pop=len(data)
while(target<pop or focus<n):
  target=data[focus]
  num=(n-1)-re.index(target)-focus +1 +extranum
  result+=num//target
  extranum=num%target
  pop-=result
  focus+=(n-1)-re.index(target)-focus +1
print(result)
