import heapq,sys
input=sys.stdin.readline

n=int(input())
arr=[]
for i in range(n):
    x=int(input())
    if x==0:
       if arr:
          ans=heapq.heappop(arr)
          print(ans)
       else:
          print(0)
    else:
       heapq.heappush(arr,x) 