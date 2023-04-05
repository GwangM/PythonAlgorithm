import sys
input = sys.stdin.readline
arr = [0 for _ in range(100001)]

n, m = map(int, input().split())
num = map(int, input().split())
idx = 1
for i in num:
  arr[idx] = i + arr[idx-1]
  idx += 1
for i in range(m):
  i, j = map(int, input().split())
  print(arr[j]-arr[i-1])