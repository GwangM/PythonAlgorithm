import sys
from collections import defaultdict
input = sys.stdin.readline
t = int(input())
for _ in range(t):
  n = int(input())
  temp=defaultdict(int)
  for _ in range(n):
    a, b = input().split()
    temp[b] += 1
  #모든 value 더한 것, 2개씩 곱한 것, ...
  