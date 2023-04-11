from collections import deque

n,m=map(int,input().split())

visited=[0 for _ in range(100001)]
#append 방식은 오래 걸리기 때문에 미리 배열을 할당해준다.

def bfs(n,m,visited):
  queue = deque([(n,0)])
  visited[n]=1
  while queue:
    temp, distance = queue.popleft()
    a = temp - 1
    b = temp + 1
    c = temp * 2
    distance+=1
    if a == m or b == m or c == m:
      return distance

    if a>-1 and visited[a]==0:
      visited[a]=1
      queue.append((a,distance))
    if b<100001 and visited[b]==0:
      visited[b]=1
      queue.append((b, distance))
    if c<100001 and visited[c]==0:
      visited[c]=1
      queue.append((c,distance))

if n >= m:
  print(n - m)
else:
  print(bfs(n,m,visited))