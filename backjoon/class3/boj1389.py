import sys
from collections import deque
input = sys.stdin.readline

n,m=map(int,input().split())
arr=[[]for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    if b not in arr[a]:
      arr[a].append(b)
      arr[b].append(a)

def bfs(arr ,start):
   queue = deque([(start, 0)])
   visited=[start]
   result=0
   while queue:
      temp, stage=queue.popleft()
      stage+=1
      for i in arr[temp]:
         if i not in visited:
            visited.append(i)
            queue.append((i,stage))
            result+=stage
   return result
   
minNum=bfs(arr,1)
ans=1
for i in range(2,n+1):
   temp=bfs(arr,i)
   if temp<minNum:
      minNum=temp
      ans=i
print(ans)