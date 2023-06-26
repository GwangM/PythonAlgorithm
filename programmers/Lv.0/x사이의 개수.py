def solution(myString):
    temp=myString.split('x')
    answer = list(map(len,temp))
    return answer