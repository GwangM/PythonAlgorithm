#1개 다르면 1, 2개 다르면 2
#3명일 경우 2명을 묶는 가지 3쌍을 다 합한 것
#종류는 16가지 n이 17이상 32이하면 무조건 겹치는 것 하나 이상, 33 이상이면 무조건 0이된다.
import sys
input=sys.stdin.readline
t=int(input())
distance=[[0 for j in range(32)]for k in range(32)]
for _ in range(t):
    n=int(input())
    if n>=33:
        arr=input()
        print(0)
    else:
        arr=input().split()
        for a in range(n):
            for b in range(n):
                temp=0
#                print(arr)
                for i in range(4):
                    if arr[a][i]!=arr[b][i]:
                        temp+=1
                distance[a][b]=temp
        answer=float('inf')
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i==j or j==k or i==k:
                        continue
                    temp=distance[i][j]+distance[j][k]+distance[i][k]
                    if answer>temp:
                        answer=temp
                    
        print(answer)
