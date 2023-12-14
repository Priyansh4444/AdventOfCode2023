ll = open('lines.txt').read().strip()
lines = ll.split('\n')
caches = {}
for i in range(len(lines)):
            lines[i] = list(lines[i])


def makestring(lines,dir):
    l = ''.join([''.join(lines[i]) for i in range(len(lines))])
    return l,dir


def change(lines, dir):
    global caches
    if makestring(lines, dir) in caches.keys():
        return caches[makestring(lines, dir)]
    if dir == 0:
        for t in range(len(lines)):
            for i in range(len(lines)-1):
                for j in range(len(lines[i])):
                    if lines[i+1][j] == 'O' and lines[i][j] == '.':
                        lines[i+1][j], lines[i][j] = lines[i][j], lines[i+1][j]
    if dir == 2:
        for t in range(len(lines)):
            for i in range(len(lines)-1,0,-1):
                for j in range(len(lines[i])):
                    if lines[i-1][j] == 'O' and lines[i][j] == '.':
                        lines[i-1][j], lines[i][j] = lines[i][j], lines[i-1][j] 
    if dir == 1:
        for t in range(len(lines)):
            for i in range(len(lines)):
                for j in range(len(lines[i])-1):
                    if lines[i][j+1] == 'O' and lines[i][j] == '.':
                        lines[i][j+1], lines[i][j] = lines[i][j], lines[i][j+1]
    if dir == 3:
        for t in range(len(lines)):
            for i in range(len(lines)):
                for j in range(len(lines[i])-1,0,-1):
                    if lines[i][j-1] == 'O' and lines[i][j] == '.':
                        lines[i][j-1], lines[i][j] = lines[i][j], lines[i][j-1]
    caches[makestring(lines, dir)] = lines
    return lines


def scores(lines):
    total = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'O':
                total += len(lines)-i
    return total


scorest = []
target = 0
for i in range(1000000000):
    print(scores(lines))
    t = hash(makestring(lines, 0)[0])
    # making a hash of each state
    if not target and t in scorest:
        #checking if that state has already been seen
        start = scorest.index(t)
        #start = index of start of cycle
        length = len(scorest) - start
        #length = length of cycle
        target = (1000000000 - start) % length + start + length
        #target = index of state we want aka (1000000000 - start) = removes number of non cycle elements, % length = removes number of cycles
        # + start + length means go ahead that many spaces and extract that element and print it
        print(start,length,target)

    if len(scorest) == target and target:
        print(scorest)
        print(scores(lines))
        break
    scorest.append(t)

    lines = change(lines, 0)
    lines = change(lines, 1)
    lines = change(lines, 2)
    lines = change(lines, 3)
