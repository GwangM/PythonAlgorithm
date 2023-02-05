import heapq
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
byte=list(map(int,input().split()))
cost=list(map(int,input().split()))
#byte/cost 낮으면 안좋음

d=[([0]*(10001))for _ in range(n)]

for i in range(n):
  for j in range(70):
    b=byte[i]
    c=cost[i]
    if i==0:
      d[i][j]+=byte[i]
    elif d[i-1][j]<m:
      d[i][j]=d[i-1][j]+byte[i]
    else:
      d[i][j]=max(d[i-1][j],d[i-1][j-c]+b)
min=float("inf")
print(d)
for i in range(n):
  for j in range(70):
    if d[i][j]>=m and min>j:
      min=j
print(min)