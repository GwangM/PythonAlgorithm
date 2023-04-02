import sys
input=sys.stdin.readline
arr=[0 for i in range(21)]
arr[1]=1; arr[2]=2; arr[3]=4
for i in range(4,12):
    arr[i]=arr[i-1]+arr[i-2]+arr[i-3]
t=int(input())
for _ in range(t):
    n=int(input())
    #점화식 맨 뒤 수를 덧붙이는 방식으로
    print(arr[n])
