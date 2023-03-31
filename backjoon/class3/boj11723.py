import sys
import copy
input=sys.stdin.readline
n=int(input())
arr=[]
all=[i for i in range(1,21)]
for _ in range(n):
    a=input().rstrip().split()
    if len(a)==2:
        m=a[1]
        a=a[0]
        m=int(m)
    if a=='add':
        if m not in arr:
          arr.append(m)
    elif a=='remove':
        if m in arr:
          arr.remove(m)
    elif a=='check':
        if m in arr:
            print(1)            
        else:
            print(0)
    elif a=='toggle':
        if m in arr:
            arr.remove(m)
        else:
            arr.append(m)
    elif a=='all':
        del arr;
        arr=copy.deepcopy(all)
    else:
        arr=[]
