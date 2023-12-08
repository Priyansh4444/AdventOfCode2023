import math
import math
with open('lines.txt', 'r') as file:
    lines = file.readlines()

# Define the nodes

# Define the path
path = lines[0].strip()
nodes = {}
for line in lines[2:]:
    key, value = line.strip().split(' = ')
    nodes[key] = tuple(value.strip('()').split(', '))

l = []
for keys in nodes.keys():
    if keys[2] == 'A':
        l.append(keys)
i = 0
s = len(path)   
count = 0
counts = [] 
check = [False] * len(l)
for part in range(len(l)):
    current_node = l[part]
    i = 0
    count = 0
    while current_node[-1] != 'Z':
        direction = path[i%s]  # Get the first direction  
        if direction == 'R':
            current_node = nodes[current_node][1]  # Go to the right node
        elif direction == 'L':
            current_node = nodes[current_node][0]  
        count += 1# Go to the left node
        i+=1
    counts.append(count)
print(counts)
lcm = math.lcm(*counts)
print(lcm)  # Outputs the lowest common multiple of all elements in counts
 # Outputs: ZZZ