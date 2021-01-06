"""
board = [[0]*5 for _ in range(5)]
count =0
for i in range(5):
    for j in range(5):
        board[i][j]= 1
        for a in range(5):
            for b in range(5):
                if a>i or(a==i and b>j):
                    board[a][b]=2
                    for c in range(5):
                        for d in range(5):
                            if c>a or (c==a and d>b):
                                board[c][d]=3
                                count+=1
                                print(count)
                                for k in range(5):
                                    print(board[k])
                                print("=============================")
                                board[c][d]=0
                    board[a][b]=0
        board[i][j]=0
"""
"""
from collections import deque
import copy
n,m = map(int,input().split())
board = []
for _ in range(0,n):
    board.append(list(map(int,input().split())))
dr = [0,-1,0,1]
dc = [-1,0,1,0]
safeSpace = -1
#spread
def spread():
    visited = [[False]*m for _ in range(n)]
    b = copy.deepcopy(board)
    q = deque()
    for i in range(n):
        for j in range(m):
            if b[i][j]==2 and visited[i][j]==False:
                q.append([i,j])
                visited[i][j]=True
                while q:
                    node = q.popleft()
                    for d in range(4):
                        temp = [node[0]+dr[d],node[1]+dc[d]]
                        if 0<=temp[0]<n and 0<=temp[1]<m and b[temp[0]][temp[1]] != 1 and visited[temp[0]][temp[1]]==False:
                            b[temp[0]][temp[1]] = 2
                            q.append(temp)
                            visited[temp[0]][temp[1]]=True
    #check
    count = 0
    for i in range(n):
        for j in range(m):
            if b[i][j]==0:
                count +=1
    return count
def wall(cnt:int):
    if cnt == 3:
        # spread
        # check        
        global safeSpace
        global count
        safeSpace = max(safeSpace,spread())
        count+=1
        return
    else:
        for i in range(n):
            for j in range(m):
                if board[i][j]==0:
                    board[i][j]=1
                    wall(cnt+1)
                    board[i][j]=0
wall(0)
print(safeSpace)
"""

n,m= map(int,input().split())
data = []
temp = [[0]*m for _ in range(n)]

for _ in range(n):
    data.append(list(map(int,input().split())))

dr = [0,-1,0,1]
dc = [-1,0,1,0]

result = 0

def virus(r,c):
    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        if 0<=nr<n and 0<=nc<m:
            if temp[nr][nc] == 0:
                temp[nr][nc] = 2
                virus(nr,nc)
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                score+=1
    return score
a=0
def dfs(count):
    global result
    global a
    if count == 3:
        a+=1
        print(a)
        for i in range(n):
            for j in range(m):
                temp[i][j]=data[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
        result = max(result,get_score())
        return
    for i in range(n):
        for j in range(m):
            if data[i][j]==0:
                data[i][j]=1
                dfs(count+1)
                data[i][j]=0
dfs(0)
print(result)