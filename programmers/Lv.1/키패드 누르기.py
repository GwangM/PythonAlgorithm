
def solution(numbers, hand):
    answer = ''
    left=9
    right=11
    for i in numbers:
        if i%3==1:
            answer+='L'
            left=i-1
        elif i%3==0 and i!=0:
            answer+='R'
            right=i-1
        else:
            if i==0:
                j=10
            else:
                j=i-1#1씩 뺀 다음 몫과 나머지로 거리 계산 
            disl= abs(j//3-left//3)+abs(j%3-left%3)
            disr=abs(j//3-right//3)+abs(j%3-right%3)
            if disl==disr:
                if hand=='left':
                    answer+='L'
                    left=j
                else:
                    answer+='R'
                    right=j
            elif disl<disr:
                answer+='L'
                left=j
            else:
                answer+='R'
                right=j
    return answer