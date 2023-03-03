n=int(input())
from collections import deque 
temp=deque([i for i in range(1,n+1)])
t=temp.popleft()
while temp:
   t=temp.popleft()
   temp.append(t)
   t=temp.popleft()
print(t)