from collections import deque 
#출발지마다 bfs를 할 경우 시간초과
#목적지로부터 bfs를 하여 미리 배열에 넣어두는 방식으로

def solution(n, roads, sources, destination):
    answer = []
    inf=float('inf')
    routine=[[inf for j in range(n+1)]for i in range(n+1)]
    for i in roads:
      routine[i[0]][i[1]]=1
      routine[i[1]][i[0]]=1
    visited=[False for i in range(n+1)]
    temp=bfs(destination,routine, visited,n)
    return[temp[i] for i in sources] 

def bfs(start, roads, visited,n):
  queue=deque([(start,0)])
  visited[start]=True
  value=[-1 for i in range(n+1)]
  value[start]=0
  while queue:
    position, d=queue.popleft()
    next_d=d+1
    for temp in enumerate(roads[position]):
      i,j=temp
      if j==1 and not visited[i]:
          queue.append((i,next_d))
          value[i]=next_d
          visited[i]=True
  return value