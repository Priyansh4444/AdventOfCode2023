import math
with open('lines.txt', 'r') as f:
    lines = f.read()

galaxy = lines.split('\n')


for i in range(len(galaxy)):
    for j in range(len(galaxy[i])):
        print(galaxy[i][j], end='')
    print()

i = 0
while i in range(len(galaxy)):
    print(set(galaxy[i]))
    if set(galaxy[i]) == {'.'}:
        print('i =', i)
        galaxy.insert(i, ['.']*len(galaxy[i]))
        i += 1
    i += 1
for t in range(len(galaxy)):
    for j in range(len(galaxy[t])):
        print(galaxy[t][j], end='')
    print()

col = 0
# Assuming 'matrix' is the 2D list
while col in range(len(galaxy[0])):
    gl = []
    for row in range(len(galaxy)):
        if col < len(galaxy[row]):
            gl.append(galaxy[row][col])
    print(set(gl))
    if set(gl) == {'.'}:
        for row in range(len(galaxy)):
                galaxy[row] = list(galaxy[row])
                galaxy[row].insert(col, '.')
                galaxy[row] = ''.join(galaxy[row])
        col+=1
    col += 1
count = 0
loc = []
for t in range(len(galaxy)):
    galaxy[t] = list(galaxy[t])
    for j in range(len(galaxy[t])):
        if galaxy[t][j] == '#':
            count += 1
            galaxy[t][j] = count
            loc.append((t, j))

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = abs(x2 - x1) + abs(y2 - y1)
    return distance



for i in range(len(galaxy)):
    for j in range(len(galaxy[i])):
        print(galaxy[i][j], end='')
    print()

distances = []
for i in range(len(loc)):
    point1 = loc[i]
    unique_points = loc[i+1:]
    shortest_path = float('inf')
    for point2 in unique_points:
        distance = calculate_distance(point1, point2)
        distances.append(math.ceil(distance))
print(distances)
print(sum(distances))
         
        

