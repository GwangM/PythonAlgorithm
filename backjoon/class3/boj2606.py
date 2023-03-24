import sys
from collections import deque
input=sys.stdin.readline
t=int(input())
n=int(input())
arr=[[]for i in range(t+1)]

def bfs(start,arr):
    queue=deque([start])
    visited=[start]
    result=0
    while queue:
        temp=queue.popleft()
        for i in arr[temp]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
                result+=1

    return result


for i in range(n):
    a,b=map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

print(bfs(1,arr))
