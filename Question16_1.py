import sys
sys.setrecursionlimit(10000000)

ll = open('lines.txt').read().strip()
lines = ll.split('\n')
liness = [list(line) for line in lines]
Mirrors = ['/', '\\']
splitters = ['|', '-']
for i in range(len(lines)):
    lines[i] = list(lines[i])
copymap = [list(line) for line in lines]
passed = [list(line) for line in lines]
dir = 0,1
for i in range(len(lines)):
    for j in range(len(lines[i])):
        copymap[i][j] = '.'
        passed[i][j] = 0
def printmap(copymapss):
    for i in range(len(copymapss)):
            for j in range(len(copymapss[i])):
                print(copymapss[i][j],end='')
            print()
start = 0,0

copymaps = copymap[:]
count = 0
def move(grid,dir,x,y,count):
    global copymaps
    global passed
    copymaps[x][y] = '#'
    if dir[0] + x >= len(grid) or dir[1] + y >= len(grid[0]) or dir[0] + x < 0 or dir[1] + y < 0:
        return count
    move1 = dir[0] + x , dir[1] + y
    if passed[move1[0]][move1[1]] > 4:
        return
    copymaps[move1[0]][move1[1]] = '#'
    passed[move1[0]][move1[1]] +=1
    if grid[move1[0]][move1[1]] == '>' and dir == (0,1):
        return
    if grid[move1[0]][move1[1]] == '<' and dir == (0,-1):
        return
    if grid[move1[0]][move1[1]] == 'v' and dir == (1,0):
        return
    if grid[move1[0]][move1[1]] == '^' and dir == (-1,0):
        return
    if grid[move1[0]][move1[1]] == '.':
        if dir == (0,1):
            grid[move1[0]][move1[1]] = '>'
        elif dir == (0,-1):
            grid[move1[0]][move1[1]] = '<'
        elif dir == (1,0):
            grid[move1[0]][move1[1]] = 'v'
        elif dir == (-1,0):
            grid[move1[0]][move1[1]] = '^'
    
    if grid[move1[0]][move1[1]] == '|' :
        if dir[1]:
            dir = 1,0
            move(grid,dir,move1[0],move1[1],count)
            dir = -1,0
    elif grid[move1[0]][move1[1]] == '-':
        if dir[0]:
            dir = 0,1
            move(grid,dir,move1[0],move1[1],count)
            dir = 0,-1
    elif grid[move1[0]][move1[1]] == '/':
        if dir == (0,1):
            dir = -1,0
        elif dir == (0,-1):
            dir = 1,0
        elif dir == (1,0):
            dir = 0,-1
        elif dir == (-1,0):
            dir = 0,1
    elif grid[move1[0]][move1[1]] == '\\':
        if dir == (0,1):
            dir = 1,0
        elif dir == (0,-1):
            dir = -1,0
        elif dir == (1,0):
            dir = 0,1
        elif dir == (-1,0):
            dir = 0,-1
    
    move(grid,dir,move1[0],move1[1],count)
    
def count(map):
    count = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '#':
                count += 1
    return count
printmap(lines)
print(move(lines,(0,1),0,-1,0))
printmap(lines)
printmap(copymaps)
print(count(copymaps))


        