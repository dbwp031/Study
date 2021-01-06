n = int(input())
fruit = int(input())
board = [['#']*n for _ in range(n)]
dr = [0,1,0,-1]
dc = [1,0,-1,0]

for _ in range(fruit):
    r,c = map(int,input().split())
    board[r][c]='A'
body = [[0,0]]
#move
turn_time = int(input())
time = 0
d = 0
for i in range(turn_time):
    s,turn_type = input().split()
    s= int(s)
    while(time<s):
        print(body)
        head = [body[-1][0]+dr[d],body[-1][1]+dc[d]]
        if head[0]<0 or head[0]>=n or head[1]<0 or head[1]>=n: 
            print(time)
            break
        elif board[head[0]][head[1]] == 'A': 
            body.append(head)
            time +=1

        else:
            for b in body[:-1]:
                if b == head:
                    print(time)
                    break
            body.pop(0)
            body.append(head)
            time+=1
    if turn_type == 'L': d = (d-1)%4
    else: d = (d+1)%4
while(True):
    if head[0]<0 or head[0]>=n or head[1]<0 or head[1]>=n: 
        print(time)
        break
    else:
        head = [body[-1][0]+dr[d],body[-1][1]+dc[d]]
        body.pop(0)
        body.append(head)
        time+=1