#20통과 18 시간초과
import copy
def rotate(key):
    rotated_key = [[0]*len(key) for _ in range(len(key[0]))]
    maxCol = len(rotated_key[0])-1
    for i in range(len(key)):
        for j in range(len(key[0])):
            rotated_key[j][maxCol-i]=key[i][j]
    return rotated_key


def solution(key, lock):
    length = len(lock)+ (len(key)-1)**2
    for _ in range(4):
        empty = [[0]*length for _ in range(length)]

        for row in range(len(lock)):
            for col in range(len(lock)):
                empty[len(key)-1+row][len(key)-1+col]= lock[row][col]
        for row in range(0,length - len(key)+1):
            for col in range(0,length - len(key)+1):
                board = copy.deepcopy(empty)
                for i in range(0,len(key)):
                    for j in range(0,len(key)):
                        board[row+i][col+j]+=key[i][j]
                check = True
                for a in range(len(key)-1,len(key)-1+len(lock)):
                    for b in range(len(key)-1,len(key)-1+len(lock)):
                        if board[a][b] != 1:
                            check = False
                if check: return True
        key = rotate(key)
    return False
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))