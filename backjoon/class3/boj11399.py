n = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = 0
temp = 0
for i in arr:
  temp += i
  result += temp
print(result)