import heapq

def solution(n, roads, sources, destination):
    answer = []
    inf=float('inf')
    routine=[[inf for j in range(n+1)]for i in range(n+1)]
    for i in range(n+1):
      routine[i][i]=0
    for i in roads:
      routine[i[0]][i[1]]=1
      routine[i[1]][i[0]]=1
      
    for i in range(1,n+1):
      min(routine[i])

    return answer