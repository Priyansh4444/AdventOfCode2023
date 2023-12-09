with open('lines.txt', 'r') as file:
    report = file.read()

lines = report.strip().split('\n')
values = []

for line in lines:
    numbers = line.split()
    values.append(numbers)
for value in values:
    for i in range(len(value)):
        value[i] = int(value[i])

for i in range(len(values)):
    values[i] = list(reversed(values[i]))

def difference(values,currsum,lastdiffs):
    copydiff = values.copy()
    currsum += values[-1]
    if set(values) == {0}:
        return currsum
    else:
        for i in range(len(values)-1):
            copydiff[i] = - values[i] + values[i+1]
        copydiff.pop()
        diff = copydiff[-1] - copydiff[-2]
        curtsum = difference(copydiff,currsum,diff)
    return curtsum
s = []
for i in range(len(values)):
    lastdiff = values[i][-1] - values[i][-2]
    s.append(difference(values[i],0,lastdiff))
print(sum(s))
