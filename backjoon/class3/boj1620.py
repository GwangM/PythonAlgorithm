import sys
input=sys.stdin.readline
n,m=map(int,input().split())
arr={}
reversedArr={}
for i in range(1,n+1):
    temp=input().rstrip()
    arr[i]=temp
    reversedArr[temp]=i

for _ in range(m):
    temp=input().rstrip()
    if temp[0]>='0'and temp[0]<='9':
        temp=int(temp)
        print(arr[temp])
    else:
        print(reversedArr[temp])