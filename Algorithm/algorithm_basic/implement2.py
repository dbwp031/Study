data=input()
result=[]
sum=0
for i in data:
  if i.isdigit():
    sum+=int(i)
  else:
    result.append(i)
result.sort()
a=''
for i in result:
  a+=i
print(a+str(sum))
