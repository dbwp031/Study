def solution(words, queries):
    words.sort(key=lambda x: (len(x),x))
    def bs_min(length):
        result = -1
        start ,end = 0,len(words)-1
        while start<=end:
            mid = (start+end)//2
            if len(words[mid]) == length:
                result = mid
                end = mid - 1
            elif len(words[mid])<length:
                start = mid + 1
            else:
                end = mid - 1
        return result
    
    def bs_max(length):
        result = -1
        start ,end = 0,len(words)-1
        while start<=end:
            mid = (start+end)//2
            if len(words[mid]) == length:
                result = mid
                start = mid + 1
            elif len(words[mid])<length:
                start = mid + 1
            else:
                end = mid - 1
        return result
    answer = []
    for q in queries:
        start = bs_min(len(q))
        if start == -1:
            answer.append(0)
            continue
        end = bs_max(len(q))

        
        data = words[start:end+1]
        if q[0]=="?":
            for i in range(len(data)):
                data[i]=data[i][::-1]
            data.sort()
            qe = -1
            q = q[::-1]
            for i in range(len(q)):
                if q[i]=='?':
                    qe = i
                    break
            q_start,q_end = -1,-1
            start,end = 0,len(data)-1
            while(start<=end):
                mid = (start+end)//2
                if data[mid][0:qe] == q[0:qe]:
                    q_start = mid
                    end = mid -1
                elif data[mid][0:qe] < q[0:qe]:
                    start = mid+1
                else:
                    end = mid - 1
            start,end = 0,len(data)-1
            while(start<=end):
                mid = (start+end)//2
                if data[mid][0:qe] == q[0:qe]:
                    q_end = mid
                    start = mid +1
                elif data[mid][0:qe] < q[0:qe]:
                    start = mid+1
                else:
                    end = mid - 1
            answer.append(q_end-q_start+1)     
                
        else:
            qe = -1
            for i in range(len(q)):
                if q[i]=='?':
                    qe = i
                    break
            q_start,q_end = -1,-1
            start,end = 0,len(data)-1
            while(start<=end):
                mid = (start+end)//2
                if data[mid][0:qe] == q[0:qe]:
                    q_start = mid
                    end = mid -1
                elif data[mid][0:qe] < q[0:qe]:
                    start = mid+1
                else:
                    end = mid - 1
            start,end = 0,len(data)-1
            while(start<=end):
                mid = (start+end)//2
                if data[mid][0:qe] == q[0:qe]:
                    q_end = mid
                    start = mid +1
                elif data[mid][0:qe] < q[0:qe]:
                    start = mid+1
                else:
                    end = mid - 1
            answer.append(q_end-q_start+1)   
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]))