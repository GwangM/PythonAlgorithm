import heapq
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
byte=list(map(int,input().split()))
cost=list(map(int,input().split()))
#byte/cost 낮으면 안좋음
byteTotal=0
costTotal=0
rate=[]
inf=float("inf")
for i in range(n):   
   heapq.heappush(rate,[cost[i]/byte[i],i])

while(byteTotal<m):
  temp=heapq.heappop(rate)[1]
  print(temp)
  costTotal+=cost[temp]
  byteTotal+=byte[temp]



print(costTotal)
