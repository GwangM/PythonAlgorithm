import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
arr=[[]for i in range(n)]

for i in range(n):
    arr[i]=input()

#0,0부터 전부 순회
def bfs(arr,n):#일반 bfs
    visited=[[False for _ in range(n)]for _ in range(n)]
    answer=0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==True:
                continue
            queue=deque([(i,j)])
            visited[i][j]=True
            color=arr[i][j]
            answer+=1
            while queue:
                tempX,tempY=queue.popleft()
                if tempX-1>=0 and visited[tempX-1][tempY]==False and arr[tempX-1][tempY]==color:
                    visited[tempX-1][tempY]=True
                    queue.append((tempX-1,tempY))
                if tempY-1>=0 and visited[tempX][tempY-1]==False and arr[tempX][tempY-1]==color:
                    visited[tempX][tempY-1]=True
                    queue.append((tempX,tempY-1))
                if tempX+1<=n-1 and visited[tempX+1][tempY]==False and arr[tempX+1][tempY]==color:
                    visited[tempX+1][tempY]=True
                    queue.append((tempX+1,tempY))
                if tempY+1<=n-1 and visited[tempX][tempY+1]==False and arr[tempX][tempY+1]==color:
                    visited[tempX][tempY+1]=True
                    queue.append((tempX,tempY+1))
    return answer

def bfs_rg(arr,n):#색약 bfs
    visited=[[False for _ in range(n)]for _ in range(n)]
    answer=0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==True:
                continue
            queue=deque([(i,j)])
            visited[i][j]=True
            color=arr[i][j]
            answer+=1
            while queue:
                tempX,tempY=queue.popleft()
                if tempX-1>=0 and visited[tempX-1][tempY]==False and (arr[tempX-1][tempY]==color or (arr[tempX][tempY]!='B' and arr[tempX-1][tempY]!='B')):
                    visited[tempX-1][tempY]=True
                    queue.append((tempX-1,tempY))
                if tempY-1>=0 and visited[tempX][tempY-1]==False and (arr[tempX][tempY-1]==color or (arr[tempX][tempY]!='B' and arr[tempX][tempY-1]!='B')):
                    visited[tempX][tempY-1]=True
                    queue.append((tempX,tempY-1))
                if tempX+1<=n-1 and visited[tempX+1][tempY]==False and (arr[tempX+1][tempY]==color or (arr[tempX][tempY]!='B' and arr[tempX+1][tempY]!='B')):
                    visited[tempX+1][tempY]=True
                    queue.append((tempX+1,tempY))
                if tempY+1<=n-1 and visited[tempX][tempY+1]==False and (arr[tempX][tempY+1]==color or (arr[tempX][tempY]!='B' and arr[tempX][tempY+1]!='B')):
                    visited[tempX][tempY+1]=True
                    queue.append((tempX,tempY+1))
    return answer

print(bfs(arr,n),bfs_rg(arr,n))