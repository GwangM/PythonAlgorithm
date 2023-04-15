import sys

input = sys.stdin.readline

n = int(input())
arr=[0 for i in range(n)]
for i in range(n):
  start, end = map(int, input().split())
  arr[i] = (start, end)
  
arr.sort()
result = 0
temp1 = -1
temp2 = -1

for i, j in arr:
  if temp1 == -1:
    temp1 = i
    temp2 = j
    result += 1
  elif i >= temp2:
    temp1 = i
    temp2 = j
    result+=1
  elif j < temp2:
    temp2 = j
    
print(result)