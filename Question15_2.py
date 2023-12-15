ll = open('lines.txt').read()
lines = ll.split(',')
def hash(l):
	v = 0
	for ch in l:
		v += ord(ch)
		v *= 17
		v %= 256
	return v
total = 0
ftotal = 0
oddlist = []
wordset = set()
dicitonarywords = {}
for i in range(len(lines)):
    total = 0
    
    if '=' in lines[i]:
        t1 = lines[i].index('=')
        word , number = lines[i][:t1], lines[i][t1+1:]
        number = int(number)
        if word in wordset:
                dicitonarywords[word] = number
        else:
                dicitonarywords[word] = number
                wordset.add(word)

    elif '-' in lines[i]:
        word=lines[i][:-1]
        if word in dicitonarywords:
            del dicitonarywords[word]

boxseen = {}
l = list(dicitonarywords.keys())
for i in range(len(l)):
    hash1 = hash(l[i])
    if hash1 in boxseen:
        boxseen[hash1] = boxseen[hash1] + 1
    else:
        boxseen[hash1] = 1
    
    total = total + (dicitonarywords[l[i]] * boxseen[hash1] * (hash1+1))

print(len(boxseen))
print(total)

