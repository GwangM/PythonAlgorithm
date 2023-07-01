arr1=input()
arr2=input()
result=[0 for _ in range(1000)]
for i in range(len(arr1)):
    temp=0
    for j in range(len(arr2)):
        if temp<result[j]:
            temp=result[j]
        elif arr1[i]==arr2[j]:
            result[j]=temp+1
print(max(result))