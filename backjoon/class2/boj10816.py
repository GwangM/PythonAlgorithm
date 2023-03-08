import sys
input=sys.stdin.readline
n=input()
arr=list(map(int,input().split()))
m=input()
temp=[0 for i in range(10000001)]
search=map(int,input().split())
for i in arr:
    temp[i]+=1
arr1=[]
for i in search:
    arr1.append(str(temp[i]))
print(' '.join(arr1),end=' ')