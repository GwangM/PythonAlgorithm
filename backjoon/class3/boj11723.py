import sys

input=sys.stdin.readline
n=int(input())

s=0
for _ in range(n):
    a=input().split()
    if a[0]=='add':
        s=s|(1<<int(a[1]))
    elif a[0]=='remove':
        s=s&~(1<<int(a[1]))
    elif a[0]=='check':
        if s&(1<<int(a[1]))==1<<int(a[1]):
            print(1)
        else:
            print(0)
    elif a[0]=='toggle':
        s=s^(1<<int(a[1]))
    elif a[0]=='all':
        s=(1<<21)-1
    else:
        s=0
