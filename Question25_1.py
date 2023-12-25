import networkx as nx
import matplotlib.pyplot as plt

input = open('lines.txt').readlines()
l = {}
g = g = nx.Graph()
for lines in input:
    words = lines.split(':')
    name = words[0]
    connects = words[1].split()
    if name not in l:
        l[name] = connects
    else:
        l[name].extend(connects)
    for words in connects:
        if words not in l:
            l[words] = [name]
        elif name not in l[words]:
            l[words].append(name)


l['psj'].remove('jcz')
l['jcz'].remove('psj')
l['nqh'].remove('rmt')
l['rmt'].remove('nqh')
l['ltn'].remove('trh')
l['trh'].remove('ltn')

def count(nodes,seen,c):
    if nodes in l:
        seen.add(nodes)
        c+=1
        for words in l[nodes]:
            if words not in seen:
                seen.add(words)
                c += count(words,seen,0)
    return c


print(count('psj',set(),0))
print(count('jcz',set(),0))