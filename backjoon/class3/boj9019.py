import sys
from collections import deque

input= sys.stdin.readline
t=int(input())
def dslr(a,b,arr):
    queue=deque([a])
    arr[a]=''
    while queue:
        temp=queue.popleft()
        d=2*temp%10000
        if d==b:
            return arr[temp]+'D'
        elif arr[d]==-1:
            arr[d]=arr[temp]+'D'
            queue.append(d)
        if temp==0:
            s=9999
        else:
            s=temp-1
        if s==b:
            return arr[temp]+'S'
        elif arr[s]==-1:
            arr[s]=arr[temp]+'S'
            queue.append(s)
        st=str(temp)
        le=len(st)
        st=(4-le)*'0'+st
        l=int(st[1:]+st[0])
        r=int(st[-1]+st[:-1])
        if l==b:
            return arr[temp]+'L'
        elif arr[l]==-1:
            arr[l]=arr[temp]+'L'
            queue.append(l)
        if r==b:
            return arr[temp]+'R'
        if arr[r]==-1:
            arr[r]=arr[temp]+'R'
            queue.append(r)
            
for _ in range(t):
    a,b=map(int,input().split())
    arr=[-1 for _ in range(10000)]
    print(dslr(a,b,arr))