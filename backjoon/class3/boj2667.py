from collections import deque
n=int(input())
arr=[]
for i in range(n):
  arr.append(input())


def bfs(arr):
  visited = []
  queue=deque()
  result = 0
  count=[]
  for i in range(n):
    for j in range(n):
      if arr[i][j] == '1' and (i,j) not in visited:
        visited.append((i, j))
        queue.append((i, j))
        result += 1
        temp=0
        while queue:
          tempI, tempJ = queue.popleft()
          temp+=1
          if tempJ<n-1 and arr[tempI][tempJ + 1] == '1' and (tempI,tempJ+1) not in visited:
            visited.append((tempI, tempJ + 1))
            queue.append((tempI, tempJ + 1))
          if tempJ>0 and arr[tempI][tempJ - 1] == '1'and (tempI,tempJ-1) not in visited:
            visited.append((tempI, tempJ - 1))
            queue.append((tempI, tempJ - 1))
          if tempI<n-1 and arr[tempI+1][tempJ] == '1' and (tempI+1,tempJ) not in visited:
            visited.append((tempI+1, tempJ))
            queue.append((tempI+1, tempJ))
          if tempI>0 and arr[tempI-1][tempJ] == '1' and (tempI-1,tempJ) not in visited:
            visited.append((tempI-1, tempJ))
            queue.append((tempI-1, tempJ ))
        count.append(temp)
  count.sort()
  print(result)
  for i in count:
    print(i)

bfs(arr)