#프린터큐
k=int(input())
import sys
input = sys.stdin.readline
for _ in range(k):
  n,m=map(int, input().split())
  idx=[i for i in range(n)]
  ary=list(map(int,input().split()))
  temp=ary[m]
  origin=ary[:]
  
  ary.sort(reverse=True)
  cnt=1
  for i in ary:
    id=origin.index(i)
    origin=origin[id:]+origin[:id]
    idx=idx[id:]+idx[:id]
    if idx[0]==m:
      print(cnt)
      break
    else:
      origin.pop(0)
      idx.pop(0)
      cnt+=1
  #가장 높은 수를 찾고 그 index 앞의 것들은 전부 뒤로 보내야
  #slicing [d:] + [:d] 뒤로 붙여준다. index를 저장해두고 바뀔 때마다 변경하는 방식으로 
  