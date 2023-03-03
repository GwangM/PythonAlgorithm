from collections import deque
import sys
input=sys.stdin.readline
arr=deque()
k=int(input())
for i in range(k):
    t=int(input())
    if t==0:
      arr.pop()
    else:
      arr.append(t)
print(sum(arr))