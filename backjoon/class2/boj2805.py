n,m=map(int,input().split())
tree=list(map(int,input().split()))
start=0
end=max(tree)
#개수로 넣는 게 나을 것 같다.
while(start<=end):
    mid=(start+end)//2
