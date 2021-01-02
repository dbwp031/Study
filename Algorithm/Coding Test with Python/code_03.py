data = list(map(int,input()))
num0,num1 = 0,0

pre = data[0]
if pre == 0:
    num0+=1
else:
    num1 +=1

for item in data[1:]:
    if pre==0 and item ==1:
        pre = 1
        num1 +=1
    elif pre==1 and item == 0:
        pre = 0
        num0 +=1

print(min(num0,num1))