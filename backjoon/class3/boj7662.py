import sys
import heapq

input=sys.stdin.readline
t=int(input())
for _ in range(t):
    k=int(input())
    arr=[]
    for _ in range(k):
        o,n=input().split()
        n=int(n)
        if o=='I':
            heapq.heappush(arr,n)
        elif len(arr)==0:
            continue 
        elif n==1:
            heapq.heappop()           
        else:
            heapq.heappop()