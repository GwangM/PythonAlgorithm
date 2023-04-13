import sys

input = sys.stdin.readline

n = int(input())
arr=[0 for i in range(n)]
for i in range(n):
  start, end = map(int, input().split())
  arr[i] = (start, end)
  
arr.sort()
print(arr)