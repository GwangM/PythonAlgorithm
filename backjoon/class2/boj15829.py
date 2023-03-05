n=int(input())
arr=input()
r=31; m=1234567891
result=0
temp=ord('a')-1

for i in range(len(arr)):
    a=ord(arr[i])-temp
    t=a*(r**i)
    result+=t
    result%=m
    
print(result)