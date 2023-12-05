import math
numcards = []
def cardwinnings(card_num, line):
    card1,card2 = line.split('|')[0],line.split('|')[1]
    card1 = set(card1.split(' '))
    card2 = set(card2.split(' '))
    numintersection = len(card1.intersection(card2))-1
    global numcards
    count = numcards[card_num-1]
    while count >= 1:
        copy = 1
        while numintersection>=1:
            numcards[card_num-1 + copy] += numcards[card_num-1]
            numintersection-=1
            copy+=1
        count -= 1
    return

    
filse = open('lines.txt', 'r+')

lines = filse.read()
lines = lines.split('\n')

for line in range(len(lines)):
    lines[line] = lines[line].split(':')
    numcards.append(1)

for linet in lines:
    line = linet[1]
    print(linet[0][-1:linet[0].index(' ')])
    cardwinnings(card_num=int(linet[0][linet[0].index(' '):]),line=line)
print(numcards)
print(sum(numcards))
