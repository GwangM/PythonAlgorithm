def solution(name, yearning, photo):
    le=len(name)
    di = {name[i]:yearning[i] for i in range(le)}
    le=len(photo)
    answer=[0 for i in range(le)]
    for i in range(le):
        for j in photo[i]:
            if j in di:
                answer[i]+=di[j]
        
    return answer