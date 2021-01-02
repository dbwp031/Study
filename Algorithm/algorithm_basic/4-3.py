data=input()
row=[1,2,3,4,5,6,7,8]
col=['a','b','c','d','e','f','g','h']

dx=[2,2,1,-1,-2,-2,1,-1]
dy=[1,-1,2,2,1,-1,-2,-2]

x=col.index(data[0])+1
y=int(data[1])
cnt =0
for i in range(0,8):
  nx,ny=x+dx[i],y+dy[i]
  if(nx<1 or ny<1 or nx>8 or ny>8): continue
  cnt+=1
print(cnt)
