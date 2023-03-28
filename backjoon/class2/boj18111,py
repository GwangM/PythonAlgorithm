import sys
input=sys.stdin.readline

n,m,b=map(int,input().split())
arr=[]
res={}
for _ in range(n):
  temp=map(int,input().split())
  arr.extend(temp)
result=[0 for i in range(257)]
inf=float('inf')
for i in range(257):
  plus=0;minus=0
  for j in arr:
    if j<i:
      plus+=(i-j)
    elif j>i:
      minus+=(j-i)
  if plus>minus+b:
    result[i]=inf
  else:
    result[i]=plus+2*minus

re=min(result)
for i in range(257):
  if result[i]==re:
    height=i
print(re,height)