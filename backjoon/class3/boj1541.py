arr=input()
op='+'
i=0
result=0
temp=''
while(i<len(arr)):
    if op=='+':
        if arr[i]=='-':
            result+=int(temp)
            temp=''
            op='-'
        elif arr[i]=='+':
            result+=int(temp)   
            temp=''
        else:
            temp+=arr[i]           
    else:
        if arr[i]=='-' or arr[i]=='+':
            result-=int(temp)
            temp=''
        else:
            temp+=arr[i]    
    i+=1
if op=='+':
    result+=int(temp)
else:
    result-=int(temp)
print(result)