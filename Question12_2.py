cache = {}
def count(cfg, nums):
    if cfg == "":
        return 1 if nums == () else 0 
    #  Because if the string is empty we expect nothing if there is nothing in nums
    #  and we expect 0 if there is something in nums
    if nums == ():
        return 1 if '#' not in cfg else 0
    # same reasoning as above case
    result = 0
    key = (cfg, nums)
    if key in cache:
        return cache[key]
    if cfg[0] in ".?":
        result += count(cfg[1:],nums)
    # if first character is a .? than we can treat it as a dot in this case, (first split case) for the ?
    # num of possible occurences where the first spring is operational will remove first string and check the rest
    if cfg[0] in "#?":
        # marks the start of a block
        # 3 cases to to check if block is valid, 
        if nums[0] <= len(cfg) and "." not in cfg[:nums[0]] and (nums[0] == len(cfg) or cfg[nums[0]] != '#'):
            result += count(cfg[nums[0]+1:], nums[1:])
    cache[key] = result
    return result

total = 0
for line in open('lines.txt'):
    cfg,nums = line.split()
    nums = tuple(map(int, nums.split(',')))
    cfg = '?'.join([cfg]*5)
    nums *= 5
    total += count(cfg, nums)

print(total)