import sys
input=sys.stdin.readline
small=0
big=0
arr=[]
while(True):
    temp=input()
    if temp==".\n":
        break
    else:
      for i in temp:
         if i=="(":
            small+=1
            arr.append(1)
         elif i==")":
            if small==0:
               small=-1
               break
            else:
               t=arr.pop()
               if t==2:
                  small=-1
                  break
               small-=1
         elif i=="[":
            arr.append(2)
            big+=1
         elif i=="]":
            if big==0:
               big=-1
               break
            else:
               t=arr.pop()
               if t==1:
                  big=-1
                  break
               big-=1
      if big!=0 or small!=0:
         print("no")
         big=0
         small=0
      else:
         print("yes")            