import sys
import heapq
from collections import defaultdict

input=sys.stdin.readline
t=int(input())
for _ in range(t):
    k=int(input())
    arr=[]
    reverse = []
    n_dict=defaultdict(int)
    for _ in range(k):
        o,n=input().split()
        n=int(n)
        if o == 'I':
            n_dict[n]+=1
            heapq.heappush(arr,n)
            heapq.heappush(reverse,-n)
        elif n == 1:
            while (reverse):
                max_num=-heapq.heappop(reverse)
                if n_dict[max_num] != 0:
                    n_dict[max_num] -= 1
                    break
        else:
            while(arr):
                min_num=heapq.heappop(arr)
                if n_dict[min_num] != 0:
                    n_dict[min_num] -= 1
                    break
    while (reverse and n_dict[-reverse[0]] == 0):
        heapq.heappop(reverse)
    while (arr and n_dict[arr[0]] == 0):
        heapq.heappop(arr)
    
    if arr:
        print(-reverse[0], arr[0])
    else:
        print("EMPTY")