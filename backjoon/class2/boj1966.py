
k=int(input())
import sys
input = sys.stdin.readline
for _ in range(k):
  n,m=map(int, input().split())
  ary=list(map(int,input().split()))
  temp=ary[m]
  print(ary)
  ary.sort(reverse=True)
  print(ary)
  print(ary.index(temp)+1)
  #가장 높은 수를 찾고 그 index 앞의 것들은 전부 뒤로 보내야
  #slicing [d:] + [:d] 뒤로 붙여준다. index를 저장해두고 바뀔 때마다 변경하는 방식으로 
  