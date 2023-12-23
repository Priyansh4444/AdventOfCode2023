import sys
sys.setrecursionlimit(10000000)
from copy import deepcopy
from collections import deque

ll = open('lines.txt').read().strip()
lines = ll.split('\n')
lines = [list(line) for line in lines]
linescopy = deepcopy(lines)
for i in range(len(lines)):
    lines[i] = list(lines[i])


def print_map(l):
    for i in l:
        for j in i:
            print(j,end="")
        print()

q = [([1,0],[0,1],0)]

print_map(lines)
lengg = 1
dirssign = {'>':[0,1],'<':[0,-1],'^':[-1,0],'v':[1,0]}
directions = [[0,1],[1,0],[-1,0],[0,-1]]
while q:
    dir, location, count = q.pop(0)
    count += 1
    dir = list(dir)
    for dirs in directions:
        diry,dirx = tuple(dirs)
        if diry == -dir[0] and dirx == -dir[1]:
            continue
        ddir = [diry,dirx]
        locationx,locationy = tuple(location)
        potentialx,potentialy = dirx + locationx, diry + locationy
        if 0<= potentialx < len(lines[0]) and 0 <= potentialy < len(lines):
            
            if lines[potentialy][potentialx] in list(dirssign.keys()) and dirssign[lines[potentialy][potentialx]] == ddir:
                print('yes')
                pl = [potentialx,potentialy]
                q.append((ddir, pl,count))
            if lines[potentialy][potentialx] == '.':
                pl = [potentialx,potentialy]
                q.append((ddir, pl,count))
            if potentialx == len(lines[0])-2 and potentialy == len(lines)-2:
                lengg = max(lengg,count)
    
print(lengg)