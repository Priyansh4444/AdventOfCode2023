from collections import deque

class Module:
    def __init__(self, name, type, outputs):
        self.name = name
        self.type = type
        self.outputs = outputs

        if type == "%":
            self.memory = "off"
            # initially off
        else:
            self.memory = {}
            # has no memory at first if it isnt flip flop
    def __repr__(self):
        return self.name + "{type=" + self.type + ",outputs=" + ",".join(self.outputs) + ",memory=" + str(self.memory) + "}"

modules = {}
#set of instructions
broadcast_targets = []
# broadcast buttons


for line in open('lines.txt'):
    left, right = line.strip().split(" -> ")
    outputs = right.split(", ")
    if left == "broadcaster":
        broadcast_targets = outputs
    else:
        type = left[0]
        # flip flop or conjunction
        name = left[1:]
        modules[name] = Module(name, type, outputs)

for name, module in modules.items():
    # go through every module to seperate them to fill the memories of the conjunction file
    for output in module.outputs:
        if output in modules and modules[output].type == "&":
            # initially they are all at low
            modules[output].memory[name] = "lo"

lo = hi = 0

for _ in range(1000):
    # press the button 1 thousand times, each new button starts with lowsignal cuz button and broadcast gives low signal
    lo += 1
    q = deque([("broadcaster", x, "lo") for x in broadcast_targets])
    # have each broadcaster target till each cycle ends
    while q:
        # complete every branch and node
        origin, target, pulse = q.popleft()
        # add pulse to pulse count
        if pulse == "lo":
            lo += 1
        else:
            hi += 1
        # if we reach the end of a cycle continue
        if target not in modules:
            continue
        module = modules[target]
        
        if module.type == "%":
            if pulse == "lo":
                # if its low and the memory is on then switch it off and if its off switch it on
                module.memory = "on" if module.memory == "off" else "off"
                # if its high pulse and the memory is on then make the pulse low else make it high
                outgoing = "hi" if module.memory == "on" else "lo"
                for x in module.outputs:
                    # execute each node
                    q.append((module.name, x, outgoing))
            # if we come across a high pulsejust ignore it
        else:
            module.memory[origin] = pulse
            # change the pulse of the origin to what was encountered
            outgoing = "lo" if all(x == "hi" for x in module.memory.values()) else "hi"
            for x in module.outputs:
                q.append((module.name, x, outgoing))

print(lo * hi)