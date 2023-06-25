import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[[]for _ in range(n)]
for i in range(n):
    temp=list(map(int,input().split()))
    arr[i]=temp
maxNum=0
    
for i in range(n):
    for j in range(m):
        if i+1<=n-1 and j+1<=m-1:
            temp=arr[i][j]+arr[i+1][j]+arr[i][j+1]+arr[i+1][j+1]
            if maxNum<temp:
                maxNum=temp
        if i+1<=n-1 and j+2<=m-1:
            temp1=arr[i][j]+arr[i][j+1]+arr[i][j+2]
            temp2=arr[i+1][j]+arr[i+1][j+1]+arr[i+1][j+2]
            max1=max(arr[i][j:j+3])
            max2=max(arr[i+1][j:j+3])
            temp=temp1+max2
            if maxNum<temp:
                maxNum=temp
            temp=temp2+max1
            if maxNum<temp:
                maxNum=temp
            max1=max(arr[i][j],arr[i][j+2])
            max2=max(arr[i+1][j],arr[i+1][j+2])
            temp=arr[i][j+1]+arr[i+1][j+1]+max1+max2
            if maxNum<temp:
                maxNum=temp
        if i+2<=n-1 and j+1<=m-1:
            temp1=arr[i][j]+arr[i+1][j]+arr[i+2][j]
            temp2=arr[i][j+1]+arr[i+1][j+1]+arr[i+2][j+1]
            max1=max(arr[i][j],arr[i+1][j],arr[i+2][j])
            max2=max(arr[i][j+1],arr[i+1][j+1],arr[i+2][j+1])
            temp=temp1+max2
            if maxNum<temp:
                maxNum=temp
            temp=temp2+max1
            if maxNum<temp:
                maxNum=temp
            max1=max(arr[i][j],arr[i+2][j])
            max2=max(arr[i][j+1],arr[i+2][j+1])
            temp=arr[i+1][j]+arr[i+1][j+1]+max1+max2
            if maxNum<temp:
                maxNum=temp

        if i+3<=n-1:
            temp=arr[i][j]+arr[i+1][j]+arr[i+2][j]+arr[i+3][j]
            if maxNum<temp:
                maxNum=temp
        if j+3<=m-1:
            temp=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i][j+3]
            if maxNum<temp:
                maxNum=temp

print(maxNum)