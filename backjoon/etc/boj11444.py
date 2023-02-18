from collections import defaultdict
n=int(input())
m= 1000000007
dp=defaultdict(int)
#f1=0 f2=1 f3=f2+f1 f4=f3+f2 
#fn=fn-1+fn-2, fn-fn-1=fn-2
dp[1]=1
dp[2]=1
def solve(n):
  if dp[n]!=0:
    return dp[n]
  elif n%2==1:
    b=n//2
    a=b+1
    c=solve(a)
    d=solve(b)
    dp[n]=(c**2+d**2)%m
    return dp[n]
  else:
    a=n//2
    b=a-1
    c=solve(a)
    d=solve(b)
    dp[n]=(c**2+2*c*d)%m
    return dp[n]

print(solve(n))