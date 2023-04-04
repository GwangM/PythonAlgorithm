import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[]
for i in range(n):
    temp=list(map(int,input().split()))
    arr.append(temp)
maxNum=0
    
for i in range(n):
    for j in range(m):
        down_three=arr[i][j]+arr[i+1][j]+arr[i+2][j]
        right_three=arr[i][j]+arr[i][j+1]+arr[i][j+2]
        maxTemp=0