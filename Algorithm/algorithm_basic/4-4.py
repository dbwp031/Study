#My code can't load
N,M=map(int,input().split())
x,y,d=map(int,input().split())
data=[]
for i in range(0,N):
  data.append(list(map(int,input().split())))

dx=[0,1,0,-1]
dy=[1,0,-1,0]
turnCnt=0
result=0
while(True):

  ##check finish Time
  if(turnCnt==4):
    #get back pow
    if d==0:b=2
    elif d==1:b=3
    elif d==2:b=0
    else:     b=1
    nx,ny=x+dx[b],y+dy[b]
    if(data[nx][ny]==1):
      break
    result+=1
    data[x][y]=2
    x,y=nx,ny
  ###Turn start
  d+=1
  if(d==4):d=0
  ###Turn finish/check start
  nx,ny=x+dx[d],y+dy[d]
  if(data[nx][ny]==1 or data[nx][ny]==2):
    turnCnt+=1
    continue
  ###check finish/move start
  data[x][y]=2
  result+=1
  x,y=nx,ny
  turnCnt=0
  ###move finish
  
print(result)

#book code
n,m=map(int,input().split())
d=[[0]*m for _ in range(n)]
x,y,direction = map(int,input().split())
d[x][y]=1
array=[]
for i in range(n):
  array.append(list(map(int,input().split())))
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def turn_left():
  global direction
  direction -=1
  if direction == -1:
    direction=3
count =1
turn_time=0
while True:
  turn_left()
  nx=x+dx[direction]
  ny=y+dy[direction]
  if d[nx][ny]== 0 and array[nx][ny]==0:
    d[nx][ny]=1
    x=nx
    y=ny
    count+=1
    turn_time=0
    continue
  else:
    turn_time +=1
  if turn_time == 4:
    nx= x-dx[direction]
    ny= y-dy[direction]
    if array[nx][ny] == 0:
      x=nx
      y=ny
    else:
      break
    turn_time=0
print(count)
