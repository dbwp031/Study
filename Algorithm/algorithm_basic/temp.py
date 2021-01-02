N,M=map(int,input().split())
data=list(map(int,input().split()))
mapp=[]
for i in range(0,N):
  mapp.append(list(map(int,input().split())))

x=data[0]
y=data[1]
d=data[2]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
result=0
while(True):
  cnt=0
  for i in range(0,4):
    if(cnt==4):
      if(d==0): b=2
      elif(d==1): b=3
      elif(d==2): b=0
      else: b=1
      nx=x+dx[b]
      ny=y+dy[b]
      if(mapp[nx][ny]==1):
        break
      else:x,y=nx,ny
    nd=d-1
    if(nd<0):d=3
    else: d=nd
    nx=x+dx[d]
    ny=y+dy[d]
    if(mapp[nx][ny]==1 or mapp[nx][ny]==2):
      cnt+=1
      continue
    mapp[x][y]=2
    result+=1
    x,y=nx,ny

print(result)
