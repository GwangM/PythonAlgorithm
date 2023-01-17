#플러스 서비스 가입자 최대로 > 이모티콘 판매액 최대로
percent=[0.1,0.2,0.3,0.4]
buy=0 #플러스 구매자
max=0
def solve(users,emoticons,list,index, end):
  global percent
  for i in percent:
    list[index]=i #실제 적용 할인율
    if index!=end:
      solve(users, emoticons, list,index+1,end)
    else:
      sign=0
      for i in users:
        temp=0
        for j in range(len(list)):
          if 0.01*i[0]<=list[j]:
            temp+=(1-list[j])*emoticons[j]
        if temp>=i[1]:
          sign+=1#플러스 가입
      global buy
      global max
      if sign>=buy and max<temp:
        max=temp
        buy=sign
      

def solution(users, emoticons):
    #전부 40% 할인일 경우 플러스 최대
    #40%에서 줄여나가다 가입자가 줄어든 경우는 제외
    
    #자신의 기준에 따라 일정 비율 이상 할인하면 모두 구매한다.
    #구매 비용이 일정 가격 이상이면 플러스 서비스 가입
    #입력되는 것 users[i][0] 비율 users[i][1]가격
    global max
    list=[]
    for i in emoticons:
        list.append(0.1)
    global buy
    solve(users,emoticons,list, 0, len(emoticons)-1)  
    answer=[buy,max]
    return answer
users=[[40,10000],[25,10000]]
emoticons=[7000,9000]
print(solution(users,emoticons))