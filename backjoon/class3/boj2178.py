import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(input())
ans=float('inf')
def bfs(arr,n,m):
    queue=deque([(0,0,1)])
    visited=[(0,0)]
    while queue:
        t1,t2,result=queue.popleft()
        for i in range(t1-1,t1+2):
              if i==-1 or i==n:
                continue
              if (i,t2) not in visited and arr[i][t2]=='1':
                      queue.append((i,t2,result+1))
                      visited.append((i,t2))
                      if i==n-1 and t2==m-1:
                          return result+1
        for j in range(t2-1,t2+2):
              if j==-1 or j==m:
                continue
              if (t1,j) not in visited and arr[t1][j]=='1':
                      queue.append((t1,j,result+1))
                      visited.append((t1,j))
                      if t1==n-1 and j==m-1:
                          return result+1
    return -1 
print(bfs(arr,n,m))
        
    
    
    