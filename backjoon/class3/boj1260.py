import sys
from collections import deque
import copy
input=sys.stdin.readline

n,m,v=map(int,input().split())
arr=[[]for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

arr=list(map(sorted,arr))

def bfs(arr ,start):
    queue=deque([start])
    visited=[start]
    print(start, end=' ')
    while queue:
        temp=queue.popleft()
        for i in arr[temp]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
                print(i, end=' ')    


def dfs(arr,start):
    queue=deque([start])
    visited=[]
    while queue:
        temp=queue.pop()        
        if temp not in visited:
            visited.append(temp)
            if arr:
              arr[temp].reverse()
              queue.extend(arr[temp])
            print(temp,end=' ')
arr2=copy.deepcopy(arr)
dfs(arr,v)
print()
bfs(arr2,v)