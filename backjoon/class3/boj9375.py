import sys
from collections import defaultdict
input = sys.stdin.readline
t = int(input())
for _ in range(t):
  n = int(input())
  temp=defaultdict(lambda:1)#아무것도 안입은 상태를 더한다.
  for _ in range(n):
    a, b = input().split()
    temp[b] += 1
  #모든 value 더한 것, 2개씩 곱한 것, ...
  result = 1
  value=list(temp.values())
  for i in range(len(value)):
    result*=value[i]
  print(result-1)#하나라도 착용해야 하므로 아무것도 없는 경우를 뺀다.