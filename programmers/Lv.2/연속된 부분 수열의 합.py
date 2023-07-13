def solution(sequence, k):
    answer = [0,10000000]
    j=len(sequence)-1
    result=0
    
    for i in range(len(sequence)-1,-1,-1):
        result+=sequence[i]
        while result>k:
            result-=sequence[j]
            j-=1
        if result==k:
            if j-i<=answer[1]-answer[0]:
                answer=[i,j]
    return answer