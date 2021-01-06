from collections import deque
n,k = map(int,input().split())
board = []
# 맵 생성
for _ in range(n):
    board.append(list(map(int,input().split())))
s,x,y = map(int,input().split())

#spread
dr = [0,-1,0,1]
dc = [-1,0,1,0]

#queue[virus,i,j]
#0초 상태 virus 정보 queue 넣음
q = []
for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            q.append([board[i][j],i,j])

q = sorted(q,key = lambda item : item[0])

for _ in range(s):
    for _ in range(len(q)):
        node = q.pop(0)
        for d in range(4):
            nr = node[1]+dr[d]
            nc = node[2]+dc[d]
            if 0<=nr<n and 0<=nc<n and board[nr][nc]==0:
                board[nr][nc]=node[0]
                q.append([node[0],nr,nc])
print(board[x-1][y-1])