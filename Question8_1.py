with open('lines.txt', 'r') as file:
    lines = file.readlines()

# Define the nodes


# Define the path
path = lines[0].strip()
nodes = {}
for line in lines[2:]:
    key, value = line.strip().split(' = ')
    nodes[key] = tuple(value.strip('()').split(', '))

print(nodes)
current_node = 'AAA'  # Start at the first node
i = 0
s = len(path)   
count = 0
while current_node != 'ZZZ':
    direction = path[i%s]  # Get the first direction  
    if direction == 'R':
        current_node = nodes[current_node][1]  # Go to the right node
    elif direction == 'L':
        current_node = nodes[current_node][0]  # Go to the left node
    i += 1
    count+=1

print(count)  # Outputs: ZZZ