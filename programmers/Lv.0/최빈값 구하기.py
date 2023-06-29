from collections import Counter
def solution(array):
    counter=Counter(array)
    temp=max(counter.values())
    count=0
    for k,v in counter.items():
        if v==temp:
            count+=1
            answer=k
            if count>1:
                break
    
    if count==2:
        answer=-1
    return answer