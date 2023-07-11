from collections import defaultdict
def solution(participant, completion):
    answer = ''
    set1=set(participant)
    set2=set(completion)
    set3=set1-set2
    if set3:
        answer=list(set3)[0]
    else:
        dict1=defaultdict(int)
        for i in completion:
            dict1[i]+=1
        for i in participant:
            dict1[i]-=1
            if dict1[i]==-1:
                answer=i
                break        
    return answer