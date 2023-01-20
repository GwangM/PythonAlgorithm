#뒤의 수는 앞의 수 이상이어야 하므로 앞의 수부터 N까지 반복하도록
n,m=map(int,input().split())
stack=[1]
visited=[0,0,0,0,0,0,0,0]
index=0
while stack:
  temp=stack.pop()
  visited[index]=temp
  for i in range(n,temp-1,-1):
    stack.append(i)
    