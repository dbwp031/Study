data=input()

cnt0=0
cnt1=0
if(data[0]=="0"):
  cnt0+=1
else:
  cnt1+=1

for i in range(0,len(data)-1):
  if(data[i]!=data[i+1]):
    if(data[i]=="0"):
      cnt0+=1
    else:
      cnt1+=1
print(min(cnt0,cnt1))
