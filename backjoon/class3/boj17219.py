import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr={}
for i in range(n):
  a, b = input().split()
  arr[a] = b

for j in range(m):
  temp=input().strip()
  print(arr[temp])

