from collections import deque
def solution(n, lost, reserve):
    answer = n
    j=0
    lost.sort()
    reserve.sort()
    clost=[i for i in lost if i not in reserve]
    creserve=[i for i in reserve if i not in lost]
    le1=len(clost)
    le2=len(creserve)
    j=0
    for i in range(le1):
        if clost[i]-1 in creserve:
            creserve.remove(clost[i]-1)
        elif clost[i]+1 in creserve:
            creserve.remove(clost[i]+1)
        else:
            answer-=1
    return answer
arr=deque([3])
#print(arr[-1])
print(solution(5,[2,4],[3]))