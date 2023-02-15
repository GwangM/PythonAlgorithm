import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
temp=[]
result=0
for i in range(n):
  r,c=map(int,input().split())
  #a b b c c d 
  #abc + acd / abd + bcd > ac(b+d) 혹은 bd(a+c)
  #ab bc cd de
  if i<2:
    temp.append([r,c])
  else:
    temp.append([r,c])
    



