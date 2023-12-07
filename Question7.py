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

power = [0,1,2,3,4,5]
subpower = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
l1power = []
l1subpower = []
checkfhouse = False
for i in range(len(list1)):
    s = set(sorted(list1[i]))
    for item in sorted(list(s)):
        if list1[i].count(item) == 3:
            if len(s) == 2:
                print(list1[i])
                checkfhouse = True     
            break
        elif list1[i].count(item) == 2:
            s.add(4)
            break
    if len(s) == 1:
        l1power.append(5)
    elif len(s) == 2:
        if checkfhouse:
            l1power.append(3.5)
            continue
        l1power.append(4)
    elif len(s) == 3:
        l1power.append(3)
    elif len(s) == 4:
        l1power.append(2)
    elif len(s) == 5:
        l1power.append(1)
    else:
        l1power.append(0)
def bubble_sort(l1, l2, l1power):
    n = len(l1)
    subpower = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
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
