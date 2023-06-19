import sys
import copy
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
arr=[[]for i in range(n)]
x=0
y=0
for i in range(n):
    arr[i]=list(map(int,input().split()))
    if 2 in arr[i]:
        x=i
        y=arr[i].index(2)

distance=copy.deepcopy(arr)

def bfs(x,y,arr):
    queue=deque([(x,y,0)])
    visited=[[x,y]]
    while queue:
        tempX,tempY,dist=queue.popleft()
      
        distance[tempX][tempY]=dist
        if tempX-1>=0 and arr[tempX-1][tempY]==1 and [tempX-1,tempY] not in visited:
            visited.append([tempX-1,tempY])
            queue.append((tempX-1,tempY,dist+1))
        if tempY-1>=0 and arr[tempX][tempY-1]==1 and [tempX,tempY-1] not in visited:
            visited.append([tempX,tempY-1])
            queue.append((tempX,tempY-1,dist+1))
        if tempX+1<=n-1 and arr[tempX+1][tempY]==1 and [tempX+1,tempY] not in visited:
            visited.append([tempX+1,tempY])
            queue.append((tempX+1,tempY,dist+1))
        if tempY+1<=m-1 and arr[tempX][tempY+1]==1 and [tempX,tempY+1] not in visited:
            visited.append([tempX,tempY+1])
            queue.append((tempX,tempY+1,dist+1))
bfs(x,y,arr)
    