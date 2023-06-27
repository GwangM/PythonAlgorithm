def solution(n):
    arr=[[0 for _ in range(n)]for _ in range(n)]
    tempx=0
    tempy=-1
    count=0
    dx=0
    dy=1

    for i in range(1,n*n+1):
        if (0<=(tempy+dy)<=(n-1))==False or(0<=tempx+dx<=n-1)==False or arr[tempx+dx][tempy+dy]!=0:
            count=(count+1)%4
        if count==0:
            dx=0
            dy=1
        elif count ==1:
            dx=1
            dy=0
        elif count==2:
            dx=0
            dy=-1
        else:
            dx=-1
            dy=0
        if arr[tempx+dx][tempy+dy]!=0:
            break
        else:
            tempx+=dx
            tempy+=dy
            arr[tempx][tempy]=i

    return arr