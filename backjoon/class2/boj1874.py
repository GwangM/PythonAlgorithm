n=int(input())
stack=[0]
result=[]
turn=False
count=1
no=False
for i in range(n):
  num=int(input())
  if turn==False:
    while stack[-1]<num:
      stack.append(count)
      count+=1
      result.append('+')
    while stack[-1]>num:
      stack.pop()
      result.append('-')
      if stack[-1]<num:
        no=True
        break
    if stack[-1]==num:
        stack.pop()
        result.append('-')
    if no==True:
      break
    if num==n:
      turn=True
  else:
    if stack[-1]==num:
      stack.pop()
      result.append("-")
    else:
      no=True
      break

if no==True:
  print("NO")
else:
  for i in result:
    print(i)
