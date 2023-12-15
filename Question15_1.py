ll = open('lines.txt').read().strip()
lines = ll.split(',')

total = 0
ftotal = 0
d = {}
for i in range(len(lines)):
    total = 0
    if '=' in lines[i]:
        d[lines[i].split('=')[1]] = [lines[i].split('=')[0]] if lines[i].split('=')[1] in d else d[lines[i].split('=')[1]].extend(lines[i].split('=')[0])
    for j in range(len(lines[i])):
        total =( total + ord(lines[i][j])) * 17
    ftotal = ftotal + total% 256


print(ftotal)

