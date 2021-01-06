import sys
input = sys.stdin.readline
n,m,k,x = map(int,input().split())
city = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    city[a].append(b)
visited = [False]* (n+1)
q = []
q.append(x)
visited[x]= True
for _ in range(k):
    for _ in range(len(q)):
        node = q.pop(0)
        for c in city[node]:
            if visited[c] == False:
                visited[c]=True
                q.append(c)
if not q: print(-1)
else:
    q.sort()
    for item in q:
        print(item)