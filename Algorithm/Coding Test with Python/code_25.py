def solution(N, stages):

    stage_player = [0]*(N+2)
    for i in stages:
        stage_player[i]+=1

    player = len(stages)
    result = {}
    for i in range(len(stage_player)-1):
        if player != 0:
            result[i] = stage_player[i]/player
            player -= stage_player[i]
        else:
            result[i]=0
    del result[0]
    return sorted(result,key= lambda x: result[x],reverse=True)
    

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))