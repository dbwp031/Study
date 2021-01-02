#my code
def dfs(graph,visited,n,m):
  visited[n][m]=True
  if(0<=n<len(graph) and 0<=m+1<len(graph[0]) and graph[n][m+1]==0 and visited[n][m+1]==False):#오
    dfs(graph,visited,n,m+1)
  if(0<=n+1<len(graph) and 0<=m<len(graph[0]) and graph[n+1][m]==0 and visited[n+1][m]==False):#아래
    dfs(graph,visited,n+1,m)
  if(0<=n<len(graph) and 0<=m-1<len(graph[0]) and graph[n][m-1]==0 and visited[n][m-1]==False):#왼
    dfs(graph,visited,n,m-1)
  if(0<=n-1<len(graph) and 0<=m<len(graph[0]) and graph[n-1][m]==0 and visited[n-1][m]==False):
    dfs(graph,visited,n-1,m)


n,m=map(int,input().split())
data=[]
cnt=0
for i in range(0,n):
  data.append(list(map(int,input())))
visited=[]
for i in range(n):
    visited.append([False]*m)
for i in range(n):
  for j in range(m):
    if(data[i][j]==0 and visited[i][j]==False):
      dfs(data,visited,i,j)
      cnt+=1
print(cnt)

#book code
n,m=map(int,input().split())

graph=[]
for i in range(n):
  graph.append(list(map(int,input())))

def dfs(x,y):
  if x<=-1 or x>=n or y<=-1 or y>=m:
    return False
  if graph[x][y] ==0:
    graph[x][y]=1
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    return True
  return False
result =0
for i in range(n):
  for j in range(m):
    if dfs(i,j)==True:
      result+=1
print(result)
