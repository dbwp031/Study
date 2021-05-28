# 1<n<100000
import sys
def input():
    return sys.stdin.readline().rstrip()
data = []
try:
    while True:
        num = int(input())
        data.append(num)
except:
    pass
for i in data:
    num = 1
    count = 0
    while(True):
        if num % i !=0:
            count +=1
            num+=10**count
        else:
            print(count+1)
            break