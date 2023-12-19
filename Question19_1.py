ll = open('lines.txt').read()
maps = {}
detected = True
mapss, setts = ll.split('\n\n') 
mapss = mapss.split('\n')
setts = setts.split('\n')
mapflow = {}
execsets = {}
for i in range(len(mapss)):
    t = mapss[i][2:-1].split('{')
    t = t[1].split(',')
    s,_ = mapss[i].split('{')
    print(s)
    mapflow[s] = tuple(t)

print(mapflow)

for i in range(len(setts)):
    t = setts[i][1:-1].split(',')
    execsets[tuple(t)] = 'in'

print()
sums = 0

for i in execsets:
    condition = True
    x, m, a, s = i
    x = int(x[2:])
    m = int(m[2:])
    a = int(a[2:])
    s = int(s[2:])
    while condition:
        todo = execsets[i]
        qflow = mapflow[todo]
        t = 0
        while qflow != 'A':
            ss = False
            check = qflow[t]
            if len(check) <= 3:
                if check == 'A':
                    condition = False
                    sums += x + m + a + s
                    break
                if check == 'R':
                    condition = False
                    break
                qflow = mapflow[check]
                t = 0
                continue
            sign = check[1]
            
            signs = {'>': True, '<': False}
            num, dir = check[2:].split(':')
            num = int(num)
            if check[0] == 'x':
                if signs[sign]:
                    if x > num:
                        qflow = dir
                        ss = True
                else:
                    if x < num:
                        qflow = dir
                        ss = True
                t+=1

            if check[0] == 'm':
                if signs[sign]:
                    if m > num:
                        qflow = dir
                        ss = True
                else:
                    if m < num:
                        qflow = dir
                        ss = True
                t += 1
            if check[0] == 'a':
                if signs[sign]:
                    if a > num:
                        print('here')
                        qflow = dir
                        ss = True
                else:
                    if a < num:
                        qflow = dir
                        ss = True
                t += 1
            if check[0] == 's':
                if signs[sign]:
                    if s > num:
                        
                        qflow = dir
                        ss = True
                else:
                    if s < num:
                        qflow = dir
                        ss = True
                t += 1
            
            if dir == 'A' and ss:
                condition = False
                sums += x + m + a + s
                break
            if dir == 'R' and ss:
                condition = False
                break
            elif ss:
                qflow = mapflow[dir]
                t = 0

print(sums)