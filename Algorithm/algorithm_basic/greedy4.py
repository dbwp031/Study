#my code
num=int(input())
data=list(map(int,input().split()))
data.sort(reverse=True)
money=1

while(True):
  i=0
  key=money
  while(money>0 and i<len(data)):
    if(data[i]<=money):
      money-=data[i]
    i+=1
  if(money!=0): break
  money=key+1
print(key)

#book code

num=int(input())
data=list(map(int,input().split()))
data.sort()

target=1
for x in data:
  if target < x:
    break
  target+=x
  print(target)
