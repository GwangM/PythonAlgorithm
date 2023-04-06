n = int(input())
inf=float('inf')
arr = [inf for i in range(n+1)]
arr[0]=0
i = 1
arr1 = []
arr2 = []
while (True):
  temp = i * i
  if temp > n:
    break
  arr[temp] = 1
  arr1.append(temp)
  i += 1

for i in arr1:
  for j in arr1:
    temp = i + j 
    if temp > n:
      continue
    if arr[temp] == 1:
      continue
    arr[temp] = 2
    arr2.append(temp)

for i in arr1:
  for j in arr2:
    temp=i+j
    if temp > n:
      continue
    if arr[temp] < 3:
      continue
    arr[temp] = 3
    

if arr[n] == inf:
  print(4)
else:
  print(arr[n])

