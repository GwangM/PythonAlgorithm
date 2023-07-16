from collections import deque #백트래킹

def solution(picks, minerals, using=[0,0,0]):
    answer = float('inf')
    #반환값이 더 작을시에 answer를 그 값으로 바꾼다.
    if using[0]<picks[0]:

    if using[1]<picks[1]:

    if using[2]<picks[2]:

    return answer