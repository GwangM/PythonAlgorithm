m,n,h=map(int, input().split())
list=[]
for i in range(h):
  list.append([])
  for j in range(n):
    list[i].append(list(map(int, input().split())))


print(list)
