data = input()
length = len(data)
left,right =0,0
for i in range(0,length//2):
    left+=int(data[i])

for i in range(length//2,length):
    right+=int(data[i])

if left == right:
    print('LUCKY')
else:
    print('READY')