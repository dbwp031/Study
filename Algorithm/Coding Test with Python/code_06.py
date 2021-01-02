# 정확도 모두 통과 효율성 모두 실패
def solution(food_times, k):
    q = [i for i in range(k)] # queue 로 사용
    
    for _ in range(k+1):
        if not q: return -1
        target = q.pop(0)
        food_times[target]-=1
        if food_times[target]!=0:
            q.append(target)
    return target+1
