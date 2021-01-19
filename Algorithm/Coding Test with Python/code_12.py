# 기둥은 바닥 위에 있거나 보의 한쪽 끝부분 위에 있거나, 또는 다른 기둥 위에 있어야 한다.
# 보는 한쪽 끝부분이 기둥 위에 있거나, 또는 양쪽 끝부분이 다른 보와 동시에 연결되어 있어야 합니다.
# 하나의 기둥 혹은 양쪽의 보              
def solution(n, build_frame):
    pillar = []
    floor = []
    for x,y,a,b in build_frame:
        # 기둥이라면
        if a == 0:
            # 설치라면
            if b == 1:
                # 바닥이라면
                if y == 0 and 0<=x<=n:
                    pillar.append([x,y,a])
                # 바닥이 아니라면
                elif 0<y<=n-1 and 0<=x<=n:
                    canBuild = False
                    for p in pillar:
                        if p[0] == x and p[1]-1 == y:
                            canBuild == True
                            break
                    if canBuild == True:
                        pillar.append([x,y,a])
                    else:
                        for f in floor:
                            if (f[0]==x and f[1]==y) or (f[0]+1 and f[1]==y):
                                pillar.append([x,y,a])
                                break
                        
            #삭제라면
            if b == 0:
                #위에 기둥이 있으면 못 지움
                canBreak = True
                for p in pillar:
                    if p[0]==x and p[1]==y+1:
                        canBreak = False
                        break
                if canBreak == False:
                    continue
                else:
                    canBreak == False
                #위에 보가 있으면
                #위에 있는 보 다른 끝에 기둥이 있거나 / 보의 양 옆에 보가 있던가
                for f in floor:
                    #위에 보의 왼쪽이 있으면
                    if f[0]==x and p[1]==y+1:
                        # 보 다른 끝에 기둥이 있거나
                        for p in pillar:
                            if p[0]==x+1 and p[1]-1 == y:
                                canBreak = True
                                break
                        # 보의 양 옆에 보가 있던가
                        if canBreak == False:
                            left = False
                            right = False
                            for f in floor:
                                if f[0]==x-1 and p[1]==y+1:
                                    left == True
                                elif f[0]==x+1 and p[1]== y+1:
                                    right == True
                            if left and right:
                                canBreak = True
                    #위에 보의 오른쪽이 있으면
                    elif f[0]==x-1 and p[1]==y+1:
                        # 보 다른 끝에 기둥이 있거나
                        for p in pillar:
                            if p[0]==x-1 and p[1]-1 == y:
                                canBreak = True
                                break
                        # 보의 양 옆에 보가 있던가
                        if canBreak == False:
                            left = False
                            right = False
                            for f in floor:
                                if f[0]==x-2 and f[1]==y+1:
                                    left = True
                                elif f[0]==x and f[1]==y+1:
                                    right == True
                            if left and right:
                                canBreak = True
                if canBreak == True:
                    pillar.remove([x,y,a])
        # 보 라면
        else:
            #설치 라면
            if b == 1:
                # 설치 가능 구간인가?
                if not (0<=x<=n-1 and 1<=y<=n):
                    continue
                #보의 한 끝에 기둥이 있다면
                canBuild = False
                for p in pillar:
                    if (p[0]==x and p[1]==y-1) or (p[0]==x+1 and p[1]==y-1):
                        print("x:{} y:{} and pillar:{},{}".format(x,y,p[0],p[1]))
                        canBuild = True
                        break
                #보의 한 끝에 기둥이 없다면
                if canBuild == False:
                    #보의 양 끝에 보가 있나
                    left = False
                    right = False
                    print(x,y)
                    for f in floor:
                        if f[0] == x-1 and f[1] == y:
                            left = True
                        elif f[0] == x+1 and f[1]== y:
                            right = True
                    print(left,right)
                    # for p in pillar:
                    #     if p[0]-1 == x and p[1] == y:
                    #         left = True
                    #     elif p[0]+1 == x and p[1] == y:
                    #         right = True
                    if left and right:
                        canBuild = True
                if canBuild == True:
                    floor.append([x,y,a])
            #삭제라면
            else:
                #삭제하려 하는 보의 양 옆의 보가 해당 보에 의지하여 설치되어 있을 때
                for f in floor:
                    # 왼쪽의 보가 의지하고 있을 때
                    if (f[0]==x-1 and f[1]== y):
                        left = False
                        for p in pillar:
                            if (p[0]==f[0] and p[1]==f[1]-1) or (p[0] == f[0]+1 and p[1]==f[1]-1):
                                left = True
                            else:
                                break
                    # 오른쪽의 보가 의지하고 있을 때
                    if (f[0]==x+1 and f[1]== y):
                        right = False
                        for p in pillar:
                            if (p[0]==f[0] and p[1]==f[1]-1) or (p[0] == f[0]+1 and p[1]==f[1]-1):
                                right = True
                            else:
                                break
                if left and right:
                    floor.remove([x,y,a])
                    # if canBreak == True:
                    #     floor.remove([x,y,a])
        print("기둥")
        print(pillar)
        print("보")
        print(floor)
    answer = []
    answer.extend(floor)
    answer.extend(pillar)
    answer.sort(key=lambda item:(item[0],item[1]))
    return answer



print(solution(5,[[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
#######################################################################################
# 기둥은 바닥 위에 있거나 보의 한쪽 끝부분 위에 있거나, 또는 다른 기둥 위에 있어야 한다.
# 보는 한쪽 끝부분이 기둥 위에 있거나, 또는 양쪽 끝부분이 다른 보와 동시에 연결되어 있어야 합니다.
# 하나의 기둥 혹은 양쪽의 보              
def solutions(n, build_frame):
    pillar = []
    floor = []
    for x,y,a,b in build_frame:
        # 기둥이라면
        if a == 0:
            # 설치라면
            if b == 1:
                # 바닥이라면
                if y == 0 and 0<=x<=n:
                    pillar.append([x,y,a])
                # 바닥이 아니라면
                elif 0<y<=n-1 and 0<=x<=n:
                    canBuild = False
                    for p in pillar:
                        if p[0] == x and p[1]-1 == y:
                            canBuild == True
                            break
                    if canBuild == True:
                        pillar.append([x,y,a])
                    else:
                        for f in floor:
                            if (f[0]==x and f[1]==y) or (f[0]+1 and f[1]==y):
                                pillar.append([x,y,a])
                                break
                        
            #삭제라면
            if b == 0:
                #위에 기둥이 있으면 못 지움
                canBreak = True
                for p in pillar:
                    if p[0]==x and p[1]==y+1:
                        canBreak = False
                        break
                if canBreak == False:
                    continue
                else:
                    canBreak == False
                #위에 보가 있으면
                #위에 있는 보 다른 끝에 기둥이 있거나 / 보의 양 옆에 보가 있던가
                for f in floor:
                    #위에 보의 왼쪽이 있으면
                    if f[0]==x and p[1]==y+1:
                        # 보 다른 끝에 기둥이 있거나
                        for p in pillar:
                            if p[0]==x+1 and p[1]-1 == y:
                                canBreak = True
                                break
                        # 보의 양 옆에 보가 있던가
                        if canBreak == False:
                            left = False
                            right = False
                            for f in floor:
                                if f[0]==x-1 and p[1]==y+1:
                                    left == True
                                elif f[0]==x+1 and p[1]== y+1:
                                    right == True
                            if left and right:
                                canBreak = True
                    #위에 보의 오른쪽이 있으면
                    elif f[0]==x-1 and p[1]==y+1:
                        # 보 다른 끝에 기둥이 있거나
                        for p in pillar:
                            if p[0]==x-1 and p[1]-1 == y:
                                canBreak = True
                                break
                        # 보의 양 옆에 보가 있던가
                        if canBreak == False:
                            left = False
                            right = False
                            for f in floor:
                                if f[0]==x-2 and f[1]==y+1:
                                    left = True
                                elif f[0]==x and f[1]==y+1:
                                    right == True
                            if left and right:
                                canBreak = True
                if canBreak == True:
                    pillar.remove([x,y,a])
        # 보 라면
        else:
            #설치 라면
            if b == 1:
                # 설치 가능 구간인가?
                if not (0<=x<=n-1 and 1<=y<=n):
                    continue
                #보의 한 끝에 기둥이 있다면
                canBuild = False
                for p in pillar:
                    if (p[0]==x and p[1]==y-1) or (p[0]==x+1 and p[1]==y-1):
                        # print("x:{} y:{} and pillar:{},{}".format(x,y,p[0],p[1]))
                        canBuild = True
                        break
                #보의 한 끝에 기둥이 없다면
                if canBuild == False:
                    #보의 양 끝에 보가 있나
                    left = False
                    right = False
                    # print(x,y)
                    for f in floor:
                        if f[0] == x-1 and f[1] == y:
                            left = True
                        elif f[0] == x+1 and f[1]== y:
                            right = True
                    # print(left,right)
                    # for p in pillar:
                    #     if p[0]-1 == x and p[1] == y:
                    #         left = True
                    #     elif p[0]+1 == x and p[1] == y:
                    #         right = True
                    if left and right:
                        canBuild = True
                if canBuild == True:
                    floor.append([x,y,a])
            #삭제라면
            else:
                #삭제하려 하는 보의 양 옆의 보가 해당 보에 의지하여 설치되어 있을 때
                for f in floor:
                    # 왼쪽의 보가 의지하고 있을 때
                    if (f[0]==x-1 and f[1]== y):
                        left = False
                        for p in pillar:
                            if (p[0]==f[0] and p[1]==f[1]-1) or (p[0] == f[0]+1 and p[1]==f[1]-1):
                                left = True
                            else:
                                break
                    # 오른쪽의 보가 의지하고 있을 때
                    if (f[0]==x+1 and f[1]== y):
                        right = False
                        for p in pillar:
                            if (p[0]==f[0] and p[1]==f[1]-1) or (p[0] == f[0]+1 and p[1]==f[1]-1):
                                right = True
                            else:
                                break
                if left and right:
                    floor.remove([x,y,a])
                    # if canBreak == True:
                    #     floor.remove([x,y,a])
        # print("기둥")
        # print(pillar)
        # print("보")
        # print(floor)
    answer = []
    answer.extend(floor)
    answer.extend(pillar)
    answer.sort(key=lambda item:(item[0],item[1]))
    return answer



# print(solution(5,[[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
                        
