import sys
sys.setrecursionlimit(10000000)
from copy import deepcopy

ll = open('lines.txt').read().strip()
lines = ll.split('\n')
lines = [list(line) for line in lines]
linescopy = deepcopy(lines)
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
def reset():
    global copymaps
    global passed
    global linescopy
    global lines
    lines = deepcopy(linescopy)
    copymaps = [list(line) for line in lines]
    passed = [list(line) for line in lines]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            copymaps[i][j] = '.'
            passed[i][j] = 0
copymaps = copymap[:]
count = 0
def move(grid,dir,x,y):
    global copymaps
    global passed
    if dir[0] + x >= len(grid) or dir[1] + y >= len(grid[0]) or dir[0] + x < 0 or dir[1] + y < 0:
        return 0
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
    
    if grid[move1[0]][move1[1]] == '|':
        if dir[1]:
            dir = 1,0
            move(grid,dir,move1[0],move1[1])
            dir = -1,0
    elif grid[move1[0]][move1[1]] == '-':
        if dir[0]:
            dir = 0,1
            move(grid,dir,move1[0],move1[1])
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
    
    move(grid,dir,move1[0],move1[1])
    
def count(map):
    count = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '#':
                count += 1
    return count + 1
l = []
dir = 1,0
for i in range(len(lines)):
    reset()
    copymaps[0][i] = '#'
    move(lines,(1,0),0,i)
    l.append(count(copymaps))
    reset()
    copymaps[len(lines[0])-1][i] = '#'
    move(lines,(-1,0),len(lines[0])-1,i)
    l.append(count(copymaps))

dir = 0,1
for i in range(len(lines[0])):
    reset()
    copymaps[i][0] = '#'
    move(lines,(1,0),i,0)
    l.append(count(copymaps))
    reset()
    copymaps[i][len(lines)-1] = '#'
    move(lines,(-1,0),i,len(lines)-1)
    
    l.append(count(copymaps))
print(l)
print(max(l))