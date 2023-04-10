import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())

arr = [[]for i in range(n+1)]
for i in range(m):
  u, v = map(int, input().split())
  arr[u].append(v)
  arr[v].append(u)

def bfs(arr, visited, start):
  queue = deque([start])
  visited.append(start)

  while queue:
    temp = queue.popleft()
    for i in arr[temp]:
      if i not in visited:
        visited.append(i)
        queue.append(i)

visited = []
result=0
for i in range(1,n+1):
  if i not in visited:
    bfs(arr, visited, i)
    result += 1
    
print(result)