from collections import defaultdict
def solution(X, Y):
    answer = ''
    arr1=defaultdict(int)
    arr2=defaultdict(int)
    for i in X:
        arr1[i]+=1
    for i in Y:
        arr2[i]+=1
    temp="9876543210"
    result=defaultdict(int)
    for i in temp:
        result[i]=min(arr1[i],arr2[i])
    for i in temp:
        answer+=(i*result[i])
    if answer=='':
        answer='-1'
    elif answer[0]=='0':
        answer='0'
    return answer