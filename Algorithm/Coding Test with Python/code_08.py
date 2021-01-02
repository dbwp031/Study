data = input()

num=0
string = []
for s in data:
    if s.isdigit()==True:
        num+=int(s)
    else:
        string.append(s)
string.sort()
answer =""
for s in string:
    answer+=s
if num == 0:
    print(answer)
else:
    print(answer + str(num))