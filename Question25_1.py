import networkx as nx
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(100000)
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
        g.add_edge(name,words)


l['psj'].remove('fdb')
l['fdb'].remove('psj')
l['nqh'].remove('rmt')
l['rmt'].remove('nqh')
l['ltn'].remove('trh')
l['trh'].remove('ltn')
g.remove_edge('nqh','rmt')
g.remove_edge('ltn','trh')

def count(nodes,seen,c):
    if nodes in l:
        seen.add(nodes)
        c+=1
        for words in l[nodes]:
            if words not in seen:
                seen.add(words)
                c += count(words,seen,0)
    return c

nx.draw(g,with_labels=True)
plt.show()
print(count('psj',set(),0))
print(count('fdb',set(),0))