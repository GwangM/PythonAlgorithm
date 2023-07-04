def solution(keymap, targets):
    alpha={}
    for i in keymap:
        temp=1
        for j in i:
            if j not in alpha:
                alpha[j]=temp
            elif alpha[j]>temp:
                alpha[j]=temp
            temp+=1
    answer = []
    for i in targets:
        count=0
        for j in i:
            if j not in alpha:
                count=-1
                break
            else:
                count+=alpha[j]
            
        answer.append(count)    
    
    return answer