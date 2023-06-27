def solution(board):
    answer = 0
    n=len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                if i-1>=0:
                    board[i-1][j]=-1
                    if j-1>=0:
                        board[i-1][j-1]=-1
                    if j+1<=n-1:
                        board[i-1][j+1]=-1
                if j-1>=0:
                    board[i][j-1]=-1
                if j+1<=n-1 and board[i][j+1]==0:
                    board[i][j+1]=-1
                if i+1<=n-1:
                    if j-1>=0 and board[i+1][j-1]==0:
                        board[i+1][j-1]=-1
                    if board[i+1][j]==0:
                        board[i+1][j]=-1
                    if j+1<=n-1 and board[i+1][j+1]==0:
                        board[i+1][j+1]=-1
    
    for i in board:
        for j in i:
            if j==0:
                answer+=1
    return answer