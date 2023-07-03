def solution(n, m, section):
    temp=0
    answer=0
    for i in section:
        if temp<=i:
            temp=i+m
            answer+=1
    
    return answer