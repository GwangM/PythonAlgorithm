def solution(dartResult):
  #S일 경우 그대로, D는 제곱 T는 3제곱
  # *는 해당 점수와 이전 점수 2배로, index=0이면 그 다음 2배로, 중첩 가능
  # #은 이전 점수 -로 
  answer=0
  list=[0,0,0]
  index=-1
  for i in range(len(dartResult)):
    if dartResult[i]=="0":
      index+=1
      if i!=0:
        if dartResult[i-1]=="1":
          list[index]=10
        else:
          list[index]=0
      else:
        list[index]=0
    if dartResult[i]>="2" and dartResult[i]<="9":
      index+=1
      list[index]=int(dartResult[i])
    elif dartResult[i]=="D":
      list[index]*=list[index]
    elif dartResult[i]=="T":
      list[index]*=(list[index]*list[index])
    elif dartResult[i]=="*":
      list[index]*=2
      if index!=0:
        list[index-1]*=2
    elif dartResult[i]=="#":
      list[index]*=-1
    elif i!=(len(dartResult)-1):
      if dartResult[i]=="1" and dartResult[i+1]!="0":
        index+=1
        list[index]=int(dartResult[i])
  answer=sum(list)
  return answer