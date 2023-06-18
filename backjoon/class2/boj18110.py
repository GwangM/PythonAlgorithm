import sys
input=sys.stdin.readline
def round(num):
    return int(num)+(1 if num-int(num)>=0.5 else 0)
n=int(input())
arr=[0 for i in range(n)]
for i in range(n):
    arr[i]=int(input())

arr.sort()
m=n*0.15
m=round(m)
sum=0
for i in range(m,n-m):
    sum+=arr[i]
if sum!=0:
    result=sum/(n-2*m)
else:
    result=0
print(round(result))