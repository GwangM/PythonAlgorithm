import sys
import heapq

input=sys.stdin.readline
t=int(input())
for _ in range(t):
    k=int(input())
    le=0
    arr=[]
    reverse=[]
    for _ in range(k):
        o,n=input().split()
        n=int(n)
        if o=='I':
            heapq.heappush(arr,n)
            heapq.heappush(reverse,(-n,n))
            le+=1
        elif le==0:
            continue 
        elif n==1:
            heapq.heappop(reverse)
            le-=1
        else:
            heapq.heappop(arr)
            le-=1
        if le==0:
            arr.clear()
            reverse.clear()
    if le==0:
        print("EMPTY")
    else:
        print(reverse[0][1],arr[0])