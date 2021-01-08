from collections import deque
import copy
n,l,r = list(map(int,input().split()))
data = []
for _ in range(n):
    data.append(list(map(int,input().split())))
baseVisited = [[False]*n for _ in range(n)]

dr = [0,-1,0,1]
dc = [-1,0,1,0]

q_data = deque()
q=deque()
visited = copy.deepcopy(baseVisited)
moreSearch = False
count = 0

while True:
    moreSearch = False
    visited = copy.deepcopy(baseVisited)
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                q.append([i,j])
                q_data.append([i,j])
                visited[i][j]=True
                while q:
                    node = q.popleft()
                    nr,nc = node[0],node[1]
                    for d in range(4):
                        nr,nc = node[0],node[1]
                        nr += dr[d]
                        nc += dc[d]
                        if 0<=nr<n and 0<=nc<n and l<=abs(data[node[0]][node[1]]-data[nr][nc])<=r and visited[nr][nc] == False:
                            moreSearch = True
                            q.append([nr,nc])
                            q_data.append([nr,nc])
                            visited[nr][nc]= True
                sum = 0
                for node in q_data:
                    sum += data[node[0]][node[1]]
                avg = sum //len(q_data)
                for node in q_data:
                    data[node[0]][node[1]] = avg
                q_data.clear()
    if moreSearch == False:
        break
    else:
        count+=1
print(count)