from collections import defaultdict
def solution(s):
    ap=defaultdict(int)
    for i in s:
        ap[i]+=1
    answer=[]
    for i in ap.keys():
        if ap[i]==1:
            answer.append(i)
    answer.sort()
    answer=''.join(answer)
    return answer