#myCode
data=input()

result=0
i=0
while(result<=1):
  result+=int(data[i])
  i+=1
for j in range(i,len(data)):
  num=int(data[j])
  if(num<=1):
    result+=num
  else:
    result*=num
print(result)

#bookCode
data=input()
result=int(data[0])
for i in range(1,len(data)):
  num=int(data[i])
  if(num<=1 or result <=1):
    result+=num
  else:
    result+=num
print(result)
