#need to fix

def solution(food_times, k):
    answer = 0
    left=len(food_times)
    while(True):
      left-=food_times.count(0)#남은 접시 파악
      for x in food_times:
        if(x!=0):
          x-=1
      k-=left#먹어
      if(k>0 and left==0):
        answer=-1
        return answer
      if(left>k):
        break
    for i in range(len(food_times)):
      if(k==0):
        answer=i
        break
      if(food_times[i]!=0):
        k-=1
    return answer
print(solution([3,1,2],5))
