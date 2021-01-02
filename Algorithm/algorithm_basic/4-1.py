N=int(input())
plans=input().split()
x,y=1,1

dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_types=['L','R','U','D']

for plan in plans:
  for i in range(0,4):
    if(move_types[i]==plan):
      nx=x+dx[i]
      ny=y+dy[i]
      break
  if(nx<1 or nx>N or ny<1 or ny>N):
    continue
  x,y=nx,ny
print(x,y)
