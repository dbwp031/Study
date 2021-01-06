n = int(input())
data = []
for _ in range(n):
    data.append(list(input().split()))

dr = [0,-1,0,1]
dc = [-1,0,1,0]

answer = False

def check():
    for i in range(n):
        for j in range(n):
            if data[i][j]=='T':
                for d in range(4):
                    nr,nc = i+dr[d],j+dc[d]
                    while(0<=nr<n and 0<=nc<n):

                        if data[nr][nc]=='S': return False
                        elif data[nr][nc]=='O': break
                        nr += dr[d]
                        nc += dc[d]
    return True


def wall(cnt):
    global answer
    if cnt == 3:
        answer = answer or check()
        #확인
        return
    for i in range(n):
        for j in range(n):
            if data[i][j]=='X':
                data[i][j]='O'
                wall(cnt+1)
                data[i][j]='X'

wall(0)
if answer:
    print("YES")
else:
    print("NO")