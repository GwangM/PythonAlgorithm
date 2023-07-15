def solution(plans):
    answer = []
    dict1={}
    for i in plans:
        i[1]=int(i[1][:2])*60+int(i[1][3:])
        i[2]=i[1]+int(i[2])
    plans.sort(key = lambda x : x[1])
    arr=[]
    for i in range(len(plans)):
        arr.append(plans[i])
        if arr and i+1<len(plans):
            while plans[i+1][1]>=arr[-1][2]:
                answer.append(arr[-1][0])
                if len(arr)>1:
                    arr[-2][2]+=(arr[-1][2]-arr[-1][1])
                arr.pop()
                if len(arr)==0:
                    break
    while arr:
        answer.append(arr[-1][0])
        arr.pop()
    return answer