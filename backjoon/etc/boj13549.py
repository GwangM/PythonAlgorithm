from collections import deque
n,k=map(int,input().split())
#걸을 때만 시간이 들고 순간이동은 시간이 들지 않음
#x+a 2x+2a 4x+4a
#2x+a 4x+2a
if n>=k:
  print(n-k)
else:
  distance=k-n
  arr_k=deque()
  arr_k.append(k)
  while arr_k:
    k=arr_k.popleft()
    if k%2==0:
      k//=2
      if distance>abs(k-n):
        distance=abs(k-n)
        arr_k.append(k)
    else:
      k1=(k+1)//2
      k2=(k-1)//2
      if distance>abs(k1-n):
        distance=abs(k1-n)
        arr_k.append(k1)
      if distance>abs(k2-n):
        distance=abs(k2-n)
        arr_k.append(k2)

  print(distance)
