filse = open('lines.txt', 'r+')

lines = filse.read()
lines = lines.split('\n')
lines.insert(0, '.' * 100)
lines.insert(len(lines), '.'*100)

for line in range(len(lines)):
    lines[line] = '.' + lines[line] + '.'

schematic = lines
total = []
locationstar = []
for i in range(len(schematic)):
    for j in range(len(schematic[i])):
        if schematic[i][j] == '*':
            locationstar.append((i,j))
for i in range(len(schematic)):
    j = 0
    while j < len(schematic[i]):
        if schematic[i][j].isdigit() == True:
            numleng = 1
            skipcount = 0
            switch = False
            while j < len(schematic[i]) and schematic[i][j].isdigit():
                numleng += 1
                j += 1
            num = int(schematic[i][j-numleng+1:j])
            print(num)
            total.append([num,(i,j-numleng+1,j-1)])
        j += 1
print(total)
print(locationstar)
f = 0
for location in locationstar:
    m = 1
    count = 0
    for i in range(len(total)):
        location_x = location[0]
        location_y = location[1]    
        position_x = total[i][1][0]
        position_ymin = total[i][1][1]
        position_ymax = total[i][1][2]
        if abs(location_x - position_x) <= 1 and (abs(location_y - position_ymax) <= 1 or abs(location_y - position_ymin) <= 1):
            m*= total[i][0]
            print(m)
            count += 1
    if count > 1:
        f += m
print(f)
