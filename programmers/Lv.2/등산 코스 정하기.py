from collections import deque
def solution(n, paths, gates, summits):
    #i와 j를 연결하는 w만큼의 weight
    #gates는 시작,도착
    #summits 중 하나를 거쳐야 한다.
    inf=float("inf")
    for x in gates:
      temp=-1
      for p in paths:
        if p[0]==x:
          temp=p
          break
      #bfs보다 dfs가 더 적합해 보인다.
      queue=deque((temp))
      summit=False
      intensity=inf
      while queue:
        q=queue.popleft()
        if intensity>q[2]:
          #이때 summits 번호도 기억해야 한다.
          intensity=q[2]

    answer = []
    return answer
  