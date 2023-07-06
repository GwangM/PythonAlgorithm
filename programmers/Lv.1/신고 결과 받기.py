from collections import defaultdict
def solution(id_list, report, k):
    answer = defaultdict(int)
    rep=defaultdict(int)
    result=defaultdict(str)
    repo=defaultdict(int)
    for i in report:
        if rep[i]==0:
            rep[i]+=1
        else:
            continue
        a,b=i.split()
        repo[b]+=1
        result[b]+=(a+' ')
    
    for i,x in repo.items():
        if x>=k:
            for j in result[i].split():
                answer[j]+=1
    le=len(id_list)
    num=[0 for i in range(le)]
    for i in range(le):
        num[i]=answer[id_list[i]]
    return num