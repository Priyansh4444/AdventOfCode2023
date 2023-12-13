with open('lines.txt', 'r') as f:
    lines = f.read()

pict = lines.split('\n')

lens = []
for i in range(len(pict)):
   lens.append(pict[i].split(' '))
for i in range(len(lens)):
    for j in range(len(lens[i])):
        lens[i][j] = lens[i][j].split(',')

numbers = []
wors = []
for i in range(len(lens)):
    for j in range(1,len(lens[i]),2):
        for k in range(len(lens[i][j])):
            lens[i][j][k] = int(lens[i][j][k])        
        numbers.append(lens[i][j])
        wors.extend(lens[i][j-1])

lens = wors
choice = ['.','#']
def check(line, chains):
    chaincheck = [0]
    t = 0
    i = 0
    while i in range(len(line)):
        while i in range(len(line)) and line[i] == '#':
            chaincheck[t] += 1
            i+=1
        if '#' in line[i:] and chaincheck[-1]:
            chaincheck.append(0)
            t+=1
        i+=1
    if chaincheck == chains:
        return True
    else:
        return False

i = 0   
fcount = 0
while i in range(len(lens)):
    j = 0
    copy = lens[i]
    counter = lens[i].count('?')
    combinations = [['.', '#'] for _ in range(counter)]
    result = [[]]
    for countetr in combinations:
        result = [x+[y] for x in result for y in countetr]
    for res in result:
        copy_list = list(copy)
        res = ''.join(res)
        while '?' in copy_list:
            copy_list[copy_list.index('?')] = res[0]
            res = res[1:]
        copy = ''.join(copy_list)
        if check(copy, numbers[i]):
            fcount += 1
        copy = lens[i]
    j += 1
    i += 1
print(fcount)
