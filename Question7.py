with open('lines.txt', 'r') as file:
    lines = file.readlines()

# Initialize empty lists
list1 = []
list2 = []

# Split each line and append to the lists
for line in lines:
    item1, item2 = line.strip().split()
    list1.append(item1)
    list2.append(int(item2))  # Convert to int assuming the second item is an integer

l1power = []
l1subpower = []
checkfhouse = False
highestcount = 0

for i in range(len(list1)):
    highestcount = 0
    word = list1[i].replace('J','')
    letter = list1[i][0]
    for j in range(len(word)):
        if highestcount <= list1[i].count(word[j]):
            highestcount = list1[i].count(word[j])
            letter = word[j]
    power = 0
    copy = list1[i][:]
    while 'J' in copy and letter != 'J':
        copy = copy.replace('J',letter)
    print(copy)
    for j in range(len(copy)):
        power += (copy.count(copy[j]))
    l1power.append(power)

print(l1power)
def bubble_sort(l1, l2, l1power):
    n = len(l1)
    subpower = ['A','K','Q','T','9','8','7','6','5','4','3','2','J']
    for i in range(n-1):
        for j in range(0, n-i-1):
            if l1power[j] == l1power[j+1]:
                count = 0
                while l1[j][count] == l1[j+1][count]:
                    count += 1
                if subpower.index(l1[j][count]) < subpower.index(l1[j+1][count]):
                    l1[j], l1[j+1] = l1[j+1], l1[j]
                    l2[j], l2[j+1] = l2[j+1], l2[j]
                    l1power[j], l1power[j+1] = l1power[j+1], l1power[j]
                    continue
            if l1power[j] > l1power[j+1]:
                l1[j], l1[j+1] = l1[j+1], l1[j]
                l2[j], l2[j+1] = l2[j+1], l2[j]
                l1power[j], l1power[j+1] = l1power[j+1], l1power[j]

# Call the bubble_sort function
bubble_sort(list1, list2, l1power)
i = 0
s = 0
for l in list2:
    i+=1
    s+= i * l
print(s)
