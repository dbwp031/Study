from collections import deque
def solution(p):
    # 1
    if p == "": return ''
    # 2
    bal = 0
    length = 0
    while True:
        if(p[length] == '('): bal +=1
        else: bal -=1
        length +=1
        if bal == 0: break
    # 3 q를 stack으로 사용함
    isCorrect = True
    q = deque()
    if p[0]=='(': q.append(p[0])
    else: isCorrect = False
    if isCorrect:
        for i in range(1,length):
            if not q:
                isCorrect = False
                break
            if p[i]=='(': q.append('(')
            else: q.pop()
        if  q: isCorrect = False
    
    if isCorrect:
        return p[:length]+solution(p[length:])
    else:
        temp = '('
        temp += solution(p[length:])
        temp +=')'
        print(temp)
        u = ""
        for item in p[1:length-1]:
            if item == '(': u+=')'
            else: u+='('
        return temp + u
