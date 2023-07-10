
def solution(board, moves):
    answer = 0
    n=len(board)
    temp=[[board[i][j] for i in range(n) if board[i][j]!=0]for j in range(n)]
    arr=[]
    for i in moves:
        j=i-1
        if temp[j]:
            t=temp[j].pop(0)
            if arr:
                if arr[-1]==t:
                    answer+=2
                    arr.pop()
                else:
                    arr.append(t)
            else:
                arr.append(t)    
    return answer