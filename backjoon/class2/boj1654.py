k,n=map(int, input().split())
list=[]
for i in range(k):
 list.append(int(input()))
start=0
list.sort()
end=list[-1]
while(start<=end):
  sum=0
  mid=(start+end)//2
  if(mid==0):
    mid=1
  for i in list:
    sum+=i//mid
  if(sum>=n):
    start=mid+1
  else:
    end=mid-1
  mid=(start+end)//2
print(mid)