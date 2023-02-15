n=int(input())
#f1=0 f2=1 f3=f2+f1 f4=f3+f2 
#fn=fn-1+fn-2, fn-fn-1=fn-2
def solve(n):
  if n==1:
    return 0
  elif n==2:
    return 1
  elif n%2==0:
    a=n//2
    b=a-1
    c=solve(a)
    d=solve(b)
    
  else:
