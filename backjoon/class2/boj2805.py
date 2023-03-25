n,m=map(int,input().split())
tree=list(map(int,input().split()))
tree.sort()
start=0
end=tree[-1]
#개수로 넣는 게 나을 것 같다.
result=0
le=len(tree)
while(start<=end):
    mid=(start+end)//2
    temp=0

    for i in range(le-1,-1,-1):
        if tree[i]<=mid:
            break
        else:
            temp+=(tree[i]-mid)

    if temp>=m and mid>result:
        result=mid
        start=mid+1
    else:
        end=mid-1

print(result)