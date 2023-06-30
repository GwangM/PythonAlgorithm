def solution(park, routes):
    row=len(park)
    column=len(park[0])
    for i,x in enumerate(park):
        if 'S' in x:
            start=[i,x.index('S')]
    for i in routes:
        if i[0]=='E':
            go=True
            for j in range(1,int(i[2])+1):            
                if start[1]+j>column-1 or park[start[0]][start[1]+j]=='X':
                    go=False
                    break
            if go:
                start[1]+=int(i[2])
        elif i[0]=='W':
            go=True
            for j in range(1,int(i[2])+1):            
                if start[1]-j<0 or park[start[0]][start[1]-j]=='X':
                    go=False
                    break
            if go:
                start[1]-=int(i[2])
            
        elif i[0]=='N':
            go=True
            for j in range(1,int(i[2])+1):            
                if start[0]-j<0 or park[start[0]-j][start[1]]=='X':
                    go=False
                    break
            if go:
                start[0]-=int(i[2])
            
        else:
            go=True
            for j in range(1,int(i[2])+1):            
                if start[0]+j>row-1 or park[start[0]+j][start[1]]=='X':
                    go=False
                    break
            if go:
                start[0]+=int(i[2])
    
    return start