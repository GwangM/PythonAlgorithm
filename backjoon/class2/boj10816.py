import sys
input=sys.stdin.readline
n=input()
arr=map(int,input().split())
m=input()
temp=[0 for i in range(10000003)]
search=map(int,input().split())
for i in arr:
    temp[i]+=1
arr1=[]
for i in search:
    print(temp[i],end=' ')