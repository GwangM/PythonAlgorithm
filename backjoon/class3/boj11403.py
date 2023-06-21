import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
arr=[[]for i in range(n)]
for i in range(n):
    arr[i]=list(map(int,input().split()))

def bfs(start,arr):
    queue=deque([start])
    visited=[0 for i in range(n)]
    while queue:
        temp=queue.popleft()
        for i in range(n):
            if arr[temp][i]==1 and visited[i]==0:
                visited[i]=1
                queue.append(i)

    print(*visited)

for i in range(n):
    bfs(i,arr)


