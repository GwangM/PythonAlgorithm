import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
arr=input().split()
cha=100
if n>=100:
    answer=n-100
else:
    answer=100-n
num=[]
for i in range(1000001):
    temp=str(i)
    no=False
    for j in temp:
        if j in arr:
            no=True
            break
    
    temp=abs(n-i)+len(temp)
    if no==False and temp<answer:
        answer=temp

print(answer)