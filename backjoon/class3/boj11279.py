import heapq,sys
input=sys.stdin.readline

n=int(input())
arr=[]
for _ in range(n):
    temp=int(input())
    if temp==0:
        if arr:
            a,b=heapq.heappop(arr)
            print(b)
        else:
            print(0)
    else:
        heapq.heappush(arr,(-temp,temp))

