import sys
from collections import deque
input=sys.stdin.readline

t=int(input())
for _ in range(t):
  p=input()
  n=input()
  x=deque(input()[1:-2].split(','))
  #split을 이용하여 , 기준으로 분리하고 join으로 ,를 나중에 넣는다.
  front=True
  er=False
  for i in p:
    if i =='R':
      front = not front
    elif i=='D':
      if len(x)==0:
        print('error')
        er=True
        break
      elif front==True:
        x.popleft()
      else:
        x.pop()
  if er:
    continue
  
  if front:
    print('['+','.join(x)+']')
  else:
    x.reverse()
    print('['+','.join(x)+']')