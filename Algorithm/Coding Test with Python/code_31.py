t = int(input())
for _ in range(t):
    n,m=map(int,input().split())
    data = list(map(int,input().split()))
    board = [[] for _ in range(n)]
    for i in range(n):
        for _ in range(m):
            board[i].append(data.pop(0))
    