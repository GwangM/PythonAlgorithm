def solution(targets):
    answer = 0
    targets.sort()
    temp=float('inf')
    for i in range(len(targets)-1,-1,-1):
        if targets[i][1]>temp:
            continue
        else:
            temp=targets[i][0]
            answer+=1
            
    return answer