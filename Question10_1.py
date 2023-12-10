with open('lines.txt', 'r') as f:
    lines = f.read()

lines = lines.split('\n')
lines = [line.strip() for line in lines]
pipes = []
for line in lines:
    pipes.append(list(line))
firstdir = 0,0
dir = 0,90,180,270
for i in range(len(pipes)):
    for j in range(len(pipes[i])):
        if pipes[i][j] == 'S':
            start = (i,j)
            if i<len(pipes)-1:
                if pipes[i+1][j] == '|':
                    firstdir = +1,0
                    dirs = 0
                    break
                elif pipes[i+1][j] == 'F':
                    firstdir = -1,1
                    dirs = 0
                    break
                elif pipes[i+1][j] == '7':
                    firstdir = +1,0
                    dirs = 0
                    break
            if j< len(pipes[i])-1:
                if pipes[i][j+1] == '-':
                    dirs = 1
                    firstdir = 0,1
                    break
                elif pipes[i][j+1] == 'J':
                    dirs = 1
                    firstdir = 0,1
                    break
                elif pipes[i][j+1] == '7':
                    dirs = 1
                    firstdir = 0,1
                    break
            if i>0:
                if pipes[i-1][j] == '|':
                    firstdir = -1,0
                    dirs = 2
                    break
                elif pipes[i-1][j] == '7':
                    firstdir = -1,0
                    dirs = 2
                    break
                elif pipes[i-1][j] == 'F':
                    dirs = 2
                    firstdir = -1,0
                    break
            if j>0:
                if pipes[i][j-1] == '-':
                    firstdir = 0,-1
                    dirs = 3
                    break
                elif pipes[i][j-1] == 'F':
                    firstdir = 0,-1
                    dirs = 3
                    break
                elif pipes[i][j-1] == 'L':
                    firstdir = 0,-1
                    dirs = 3
                    break
            break
count = 0
copyfirst = start
start  = start[0]+firstdir[0],start[1]+firstdir[1]
print(pipes[start[0]][start[1]])
while copyfirst != start:
    count += 1
    if dirs == 0:
        if pipes[start[0]][start[1]] == '|':
            start = start[0]+1,start[1]
        elif pipes[start[0]][start[1]] == 'L':
            start = start[0],start[1]+1
            
            dirs = 1
        elif pipes[start[0]][start[1]] == 'J':
            start = start[0],start[1]-1
            dirs = 3
    elif dirs == 1:
        if pipes[start[0]][start[1]] == '-':
            start = start[0],start[1]+1
        elif pipes[start[0]][start[1]] == '7':
            start = start[0]+1,start[1]
            
            dirs = 0
        elif pipes[start[0]][start[1]] == 'J':
            start = start[0]-1,start[1]
            dirs = 2
    elif dirs == 2:
        if pipes[start[0]][start[1]] == '|':
            start = start[0]-1,start[1]
        elif pipes[start[0]][start[1]] == '7':
            start = start[0],start[1]-1
            dirs = 3
        elif pipes[start[0]][start[1]] == 'F':
            start = start[0],start[1]+1
            dirs = 1
    elif dirs == 3:
        if pipes[start[0]][start[1]] == '-':
            start = start[0],start[1]-1
        elif pipes[start[0]][start[1]] == 'F':
            start = start[0]+1,start[1]
            dirs = 0
        elif pipes[start[0]][start[1]] == 'L':
            start = start[0]-1,start[1]
            dirs = 2
print((count)//2)