import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int, input().split())
arr = [0 for i in range(n)]

for i in range(n):
  arr[i]=list(map(int, input().split()))
  
queue=deque()
for i in range(n):
  for j in range(m):
    if arr[i][j] == 1:
      queue.append((i,j))

def bfs(queue):
  end = queue[-1]
  result=0
  while queue:
    i,j = queue.popleft()
    if j+1<m and arr[i][j+1] == 0:
      queue.append((i, j + 1))
      arr[i][j + 1] = 1
    if j-1>-1 and arr[i][j-1] == 0:
      queue.append((i, j - 1))
      arr[i][j - 1] = 1
    if i-1>-1 and arr[i-1][j] == 0:
      queue.append((i - 1, j))
      arr[i - 1][j] = 1
    if i+1<n and arr[i+1][j] == 0:
      queue.append((i+ 1, j))
      arr[i+ 1][j] = 1
    if end == (i, j) and queue:
      result += 1
      end=queue[-1]
  return result

if queue:
  temp=bfs(queue)
  for i in arr:
    if 0 in i:
      temp = -1
      break
  print(temp)
else:
  print(-1)