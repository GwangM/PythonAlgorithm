import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    yes=True
    temp=0
    arr=input()
    for i in arr: 
      if i=="(":
          temp+=1
      elif i==")":
          temp-=1
          if temp==-1:
              break
    if temp!=0:
        yes=False
    if yes:
        print("YES")
    else:
        print("NO")