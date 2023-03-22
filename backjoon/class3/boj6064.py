import sys
input=sys.stdin.readline
t=int(input())
def gcd(x,y):
    if x<y:
        temp=x
        x=y
        y=temp
    while(True):
        r=x%y
        if r==0:
            return y
        x=y
        y=r

for _ in range(t):
    m,n,x,y=map(int,input().split())
    if x>m or y>n:
        print(-1)
    elif m==n:
        if x!=y:
            print(-1)
        else:
          print(x)
    else:
        if n>m:
            temp=n;n=m;m=temp;temp=x;x=y;y=temp
        temp=x-1
        y-=temp
        while(y<1):
            y+=m
            temp-=m
        while (y-1)%(m-n)!=0:
            y+=n
            if y>n*m//gcd(m,n):
                print(-1)
                break
        if (y-1)%(m-n)==0:
          cycle=(y-1)//(m-n)
          k=1+cycle*m+temp
          print(k)                    