block1, _ = open('lines.txt').read().split("\n\n")

workflows = {}

for line in block1.splitlines():
    name, rest = line[:-1].split("{")
    rules = rest.split(",")
    workflows[name] = ([], rules.pop())
    for rule in rules:
        comparison, target = rule.split(":")
        key = comparison[0]
        cmp = comparison[1]
        n = int(comparison[2:])
        workflows[name][0].append((key, cmp, n, target))

def count(ranges, name = "in"):
    if name == "R":
        return 0
    if name == "A":
        product = 1
        for lo, hi in ranges.values():
            product *= hi - lo + 1
        return product
    
    rules, fallback = workflows[name]

    total = 0

    for key, cmp, n, target in rules:
        lo, hi = ranges[key]
        if cmp == "<":
            T = (lo, n - 1)
            F = (n, hi)
        else:
            T = (n + 1, hi)
            F = (lo, n)
        # check if it is between like 1-4000 and valid
        if T[0] <= T[1]:
            # if the range is true continue execute the command
            copy = dict(ranges)
            copy[key] = T
            total += count(copy, target)
        # check if it is between like 1-4000 and valid
        if F[0] <= F[1]:
            # if the range is false continue to the next condition
            ranges = dict(ranges)
            ranges[key] = F
        else:
            break
    else:
        # only if all conditions arent checked  (1,4000) then do the fallback
        total += count(ranges, fallback)
            
    return total

print(count({key: (1, 4000) for key in "xmas"}))
