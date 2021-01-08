# #3개 통과 나머지 시간 초과-> visited 처리 못했는데(구현 어려워서) set으로 하면 쉽게 해결되는 듯 
# tr = [1,-1,-1,1]
# tc = [-1,-1,1,1] 

# def solution(board):
#     n = len(board)
#     q = [[(0,0),(0,1)]]
#     count = 0    
#     while q:
#         for _ in range(len(q)):
#             l,r=q.pop(0)
#             # ㅁㅁ
#             if l[1]>r[1]: l,r=r,l
#             if l[0]==r[0]:
#                 if 0<=l[0]-1 and board[l[0]-1][l[1]] != 1 and board[r[0]-1][r[1]]!=1:
#                     q.append([(l[0]-1,l[1]),(r[0]-1,r[1])])
#                     q.append([(l[0],l[1]),(l[0]-1,l[1])])
#                     q.append([(r[0]-1,r[1]),(r[0],r[1])])
#                 if l[0]+1<n and board[l[0]+1][l[1]] != 1 and board[r[0]+1][r[1]]!=1:
#                     q.append([(l[0]+1,l[1]),(r[0]+1,r[1])])
#                     q.append([(l[0],l[1]),(l[0]+1,l[1])])
#                     q.append([(r[0]+1,r[1]),(r[0],r[1])])
#                 if 0<=l[1]-1 and board[l[0]][l[1]-1] !=1:
#                     q.append([(l[0],l[1]-1),(l[0],l[1])])
#                 if r[1]+1<n and board[r[0]][r[1]+1]!=1:
#                     q.append([(r[0],r[1]),(r[0],r[1]+1)])
#         #ㅁ
#         #ㅁ
#             else:
#                 u,d = l,r
#                 if u[0]>d[0]: u,d = d,u
#                 if 0<= u[1]-1 and board[u[0]][u[1]-1] != 1 and board[d[0]][d[1]-1] != 1:
#                     q.append([(u[0],u[1]-1),(d[0],d[1]-1)])
#                     q.append([(u[0],u[1]),(u[0],u[1]-1)])
#                     q.append([(d[0],d[1]),(d[0],d[1]-1)])
#                 if u[1]+1<n and board[u[0]][u[1]+1] != 1 and board[d[0]][d[1]+1] != 1:
#                     q.append([(u[0],u[1]+1),(d[0],d[1]+1)])
#                     q.append([(u[0],u[1]),(u[0],u[1]+1)])
#                     q.append([(d[0],d[1]),(d[0],d[1]+1)])
#                 if 0<=u[0]-1 and board[u[0]-1][u[0]+1] != 1:
#                     q.append([(u[0],u[1]),(u[0]-1,u[1])])
#                 if d[0]+1<n and board[d[0]+1][d[1]] != 1:
#                     q.append([(d[0],d[1]),(d[0]+1,d[1])])
#             if l == (n-1,n-1) or r == (n-1,n-1):
#                 return count
#         count+=1
# print(solution(	[[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
from collections import deque

def get_next_pos(pos, board):
    next_pos = [] # 반환 결과 (이동 가능한 위치들)
    pos = list(pos) # 현재 위치 정보를 리스트로 변환 (집합 → 리스트)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    # (상, 하, 좌, 우)로 이동하는 경우에 대해서 처리
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
        # 이동하고자 하는 두 칸이 모두 비어 있다면
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
    # 현재 로봇이 가로로 놓여 있는 경우
    if pos1_x == pos2_x:
        for i in [-1, 1]: # 위쪽으로 회전하거나, 아래쪽으로 회전
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0: # 위쪽 혹은 아래쪽 두 칸이 모두 비어 있다면
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    # 현재 로봇이 세로로 놓여 있는 경우
    elif pos1_y == pos2_y:
        for i in [-1, 1]: # 왼쪽으로 회전하거나, 오른쪽으로 회전
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0: # 왼쪽 혹은 오른쪽 두 칸이 모두 비어 있다면
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
    # 현재 위치에서 이동할 수 있는 위치를 반환
    return next_pos

def solution(board):
    # 맵의 외곽에 벽을 두는 형태로 맵 변형
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    # 너비 우선 탐색(BFS) 수행
    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)} # 시작 위치 설정
    q.append((pos, 0)) # 큐에 삽입한 뒤에
    visited.append(pos) # 방문 처리
    # 큐가 빌 때까지 반복
    while q:
        pos, cost = q.popleft()
        # (n, n) 위치에 로봇이 도달했다면, 최단 거리이므로 반환
        if (n, n) in pos:
            return cost
        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board):
            # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문 처리
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0
