n,k=map(int,input().split())
arr=[i for i in range(1,n+1)]
start=-1
total=n
result=[]
print("<",end='')
while arr:
    start+=k
    start%=total
    temp=arr.pop(start)
    start-=1
    if total!=1:
      print(temp, end=', ')
    total-=1
print(temp,end=">")