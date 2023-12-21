import math
from collections import deque
# Good question, but very assumption based!!!
class Module:
    def __init__(self, name, type, outputs):
        self.name = name
        self.type = type
        self.outputs = outputs

        if type == "%":
            self.memory = "off"
        else:
            self.memory = {}
    def __repr__(self):
        return self.name + "{type=" + self.type + ",outputs=" + ",".join(self.outputs) + ",memory=" + str(self.memory) + "}"

modules = {}
broadcast_targets = []

for line in open('lines.txt'):
    left, right = line.strip().split(" -> ")
    outputs = right.split(", ")
    if left == "broadcaster":
        broadcast_targets = outputs
    else:
        type = left[0]
        name = left[1:]
        modules[name] = Module(name, type, outputs)

for name, module in modules.items():
    for output in module.outputs:
        if output in modules and modules[output].type == "&":
            modules[output].memory[name] = "lo"

# we need to know which modules feed into rx
# we assuming there is only 1 feed called rx, this syntax of a single element helps us assert there is only one item with that name, and now know what feeds into rx
(feed,) = [name for name, module in modules.items() if "rx" in module.outputs]

# we assume that each of the modules will produce a low pulse input except at the lcm of the cycle lengths of each

cycle_lengths = {}

# everything that leads to rx conjunction
seen = {name: 0 for name, module in modules.items() if feed in module.outputs}
print(modules)
presses = 0

while True:
    # now infinite presses so we do while True 
    presses += 1
    q = deque([("broadcaster", x, "lo") for x in broadcast_targets])
    
    while q:
        origin, target, pulse = q.popleft()
        
        if target not in modules:
            continue
        
        module = modules[target]
        
        # we record theis cycle for when we are on the feed module, xr
        if module.name == feed and pulse == "hi":
            seen[origin] += 1
            # we saw this x amount of times and get a hi every n times, hypothesis to checking
            if origin not in cycle_lengths:
                cycle_lengths[origin] = presses
                print(cycle_lengths[origin], origin)
            else:
                assert presses == seen[origin] * cycle_lengths[origin]
                # we should expect that the number of times we see 
                
            if all(seen.values()):
                x = 1
                for cycle_length in cycle_lengths.values():
                    x = x * cycle_length // math.gcd(x, cycle_length)
                    # or x = math.lcm(x,cycle_length)
                print(x)
                exit(0)
        
        if module.type == "%":
            if pulse == "lo":
                module.memory = "on" if module.memory == "off" else "off"
                outgoing = "hi" if module.memory == "on" else "lo"
                for x in module.outputs:
                    q.append((module.name, x, outgoing))
        else:
            module.memory[origin] = pulse
            outgoing = "lo" if all(x == "hi" for x in module.memory.values()) else "hi"
            for x in module.outputs:
                q.append((module.name, x, outgoing))
