from copy import deepcopy

def flip(key):
  n=len(key)
  new=[[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      new[i][j]=key[i][n-1-j]
  return new

def turn(key):
  n=len(key)
  new=[[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      new[i][j]=key[j][2-i]
  return new

def solution(key,lock):
  result=False
  flag=False
  n,m=len(key),len(lock)
  data=[[0]*(m+2*n-2) for _ in range(m+2*n-2)]

  for i in range(m):
    for j in range(m):
      data[n-1+i][n-1+j]=lock[i][j]

  s=deepcopy(data)
  
  for _ in range(4):
    for i in range(m+n-1):
      for j in range(m+n-1):
        for a in range(n):
          for b in range(n):
            if s[i+a][j+b]==0 and key[a][b]==1:
              s[i+a][j+b]=key[a][b]
            else:
              continue
        check=0
        for lst in s[n-1:n+m]:
          check+=sum(lst[n-1:n+m])
        if check == m*m:
          result=True
          flag=True

          for lst in s[n-1:n+m]:
            print(lst[n-1:n+m])
          break
        else:
          s=deepcopy(data)
          check=0
      if(flag):
        break
    if(flag):
      break
    key=turn(key)
  return result


print(solution([[0,0,0],[1,0,0],[0,1,1]],[[1,1,1],[1,1,0],[1,0,1]]))
key=[[0,0,0],[1,0,0],[0,1,1]]
key=flip(key)
print(key)
key=turn(key)
print(key)
key=turn(key)
print(key)
key=turn(key)
print(key)
key=turn(key)
print(key)
