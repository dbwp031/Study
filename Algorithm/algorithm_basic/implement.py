data=input()
left=0
right=0
for i in range(0,len(data)//2):
  left+=int(data[i])
for j in range(len(data)//2,len(data)):
  right+=int(data[j])
if(left==right):
  print("LUCKY")
else:
  print("READY")
