points = [(0, 0)]
dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

b = 0

for line in open('lines.txt'):
    d, n, _ = line.split()
    dr, dc = dirs[d]
    n = int(n)
    b += n
    r, c = points[-1]
    points.append((r + dr * n, c + dc * n))

A = abs(sum(
    points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1])
    for i in range(len(points))
)) // 2
# above formula is shoelace formula for area of polygon given coordinates of vertices in order from 1 to n sigma i=1 to n (xi * ((y of i+1) - (y of i-1)))/2 (sum of all triangles in the counter clock wise direction for the origin, and 2 adjeacent points)
# https://www.mathopenref.com/coordpolygonarea.html
# only works on continuous polygons
i = A - b // 2 + 1
# above formula is A = i + b/2 - 1 (A is area, i is number of points inside, b is number of points on the border) Picks theorem     

print(i + b)