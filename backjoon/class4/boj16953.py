from collections import deque
a,b=map(int,input().split())

def bfs(a,b):
    if a==b:
        return 1
    queue=deque([(b,1)])
    answer=-1
    while queue:
        temp,num=queue.popleft()
        if temp%2==0 and (temp//2)>=a:
            temp1=temp//2
            if temp1==a:
                return num+1
            else:
                queue.append((temp1,num+1))
        if temp%10==1 and temp>10*a:
            temp2=temp//10
            if temp2==a:
                return num+1
            else:
                queue.append((temp2,num+1))
    return answer
print(bfs(a,b))