def solution(ingredient):#if s[-4:] == [1, 2, 3, 1]:
    answer = 0
    i=0
    n=len(ingredient)
    while(i<n):
        if i>2 and ingredient[i-3:i+1]==[1,2,3,1]:
            answer+=1
            for _ in range(4):
                ingredient.pop(i-3)
            n-=4
            i-=3          
        else:
            i+=1
    return answer

arr=[2, 1, 1, 2, 3, 1, 2, 3, 1]
print(solution(arr))