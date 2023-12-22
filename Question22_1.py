bricks = [list(map(int, line.replace("~", ",").split(","))) for line in open('lines.txt')]
# length six arrays
bricks.sort(key=lambda brick: brick[2])
# sort them in ascending order of z value to make processing a bit easier so that every time we drop a brick we only need to check if its x and y intersects with each other

# check if 2 rectangles overrlap by seeing if their x ranges intersect or their y ranges intersect
def overlaps(a, b):
    return max(a[0], b[0]) <= min(a[3], b[3]) and max(a[1], b[1]) <= min(a[4], b[4])


# Drop each brick
for index, brick in enumerate(bricks):
    max_z = 1
    # running maximum z value it can have after it drops(how far can it fall)
    for check in bricks[:index]:
        if overlaps(brick, check):
            # we need to make sure that the brick does not fall beyond check
            max_z = max(max_z, check[5] + 1)
            # max_z position it can drop to is the value of that check is y coordinate + 1
    # we adjust bricks new height
    brick[5] -= brick[2] - max_z
    # We drop the brick down to max_z
    brick[2] = max_z

bricks.sort(key=lambda brick: brick[2])

k_supports_v = {i: set() for i in range(len(bricks))}
v_supports_k = {i: set() for i in range(len(bricks))}

for j, upper in enumerate(bricks):
    for i, lower in enumerate(bricks[:j]):
        # check if the block is directly above it and overlaps to add it to the supports
        if overlaps(lower, upper) and upper[2] == lower[5] + 1:
            k_supports_v[i].add(j)
            v_supports_k[j].add(i)

total = 0

for i in range(len(bricks)):
    # if there are more than one supporters for each support then add one to the total for each count
    if all(len(v_supports_k[j]) >= 2 for j in k_supports_v[i]):
        total += 1

print(total)