def solution(s):
    answer = 1001
    for i in range(1,len(s)//2+1):
        data = ""
        pre = s[0:i]
        count = 1
        for j in range(i,len(s),i):
            now = s[j:j+i]
            if pre == now:
                count+=1
            else:
                if count != 1:
                    data += pre + str(count)
                    count = 1
                else:
                    data += pre
                pre = now
        if count != 1:
            data += pre + str(count)
        else:
            data += pre

        answer=min(answer,len(data))
                    
    return answer