import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[0 for _ in range(n)]
visited=[[False for _ in range(m)]for _ in range(n)]
for i in range(n):
    arr[i]=input()
    if "I" in arr[i]:
        x=i
        y=arr[i].index("I")

def bfs(arr, x,y):
    queue=deque([(x,y)])
    visited[x][y]=True
    answer=0
    while queue:
        tempX,tempY=queue.popleft()
        if arr[tempX][tempY]=='P':
            answer+=1
        if tempX-1>=0 and visited[tempX-1][tempY]==False and arr[tempX-1][tempY]!='X':
            visited[tempX-1][tempY]=True
            queue.append((tempX-1,tempY))     
        if tempY-1>=0 and visited[tempX][tempY-1]==False and arr[tempX][tempY-1]!='X':
            visited[tempX][tempY-1]=True
            queue.append((tempX,tempY-1)) 
        if tempX+1<=n-1 and visited[tempX+1][tempY]==False and arr[tempX+1][tempY]!='X':
            visited[tempX+1][tempY]=True
            queue.append((tempX+1,tempY)) 
        if tempY+1<=m-1 and visited[tempX][tempY+1]==False and arr[tempX][tempY+1]!='X':
            visited[tempX][tempY+1]=True
            queue.append((tempX,tempY+1))   
    if answer==0:
        return 'TT'
    else:
        return answer

print(bfs(arr,x,y))