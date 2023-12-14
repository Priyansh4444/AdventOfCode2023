ll = open('lines.txt').read().strip()
lines = ll.split('\n')

for i in range(len(lines)):
    lines[i] = list(lines[i])
for t in range(len(lines)):
    for i in range(len(lines)-1):
        for j in range(len(lines[i])):
            if lines[i+1][j] == 'O' and lines[i][j] == '.':
                lines[i+1][j], lines[i][j] = lines[i][j], lines[i+1][j]

for i in range(len(lines)):
    for j in range(len(lines[i])):
        print(lines[i][j], end='')
    print()

total = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == 'O':
            total += len(lines)-i

print(total)



