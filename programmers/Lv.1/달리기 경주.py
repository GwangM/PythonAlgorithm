def solution(players, callings):
    answer = []
    di={}
    for i,x in enumerate(players):
        di[x]=i
    #players[di[i]]와 players[di[i]-1]을 바꾼다.
    for i in callings:
        temp=players[di[i]-1]
        players[di[i]-1]=players[di[i]]
        players[di[i]]=temp
        di[temp]+=1
        di[i]-=1
        
    answer=players
    return answer