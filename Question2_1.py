
with open('lines.txt', 'r') as file:
    line = file.readline()
    Games = []
    while line:
        se = line.split(':')
        s = se[1].split(';')
        maxred = 0
        maxgreen = 0
        maxblue = 0
        for i in range(len(s)):
            colors = s[i].split(',')
            for c in range(len(colors)):
                colorss = colors[c].split(' ')
                if 'red' in colorss[2]  :
                    maxred = max(maxred, int(colorss[1]))
                elif  'green' in colorss[2]:
                    maxgreen = max(maxgreen, int(colorss[1]))
                    
                elif 'blue' in colorss[2]:
                    maxblue = max(maxblue, int(colorss[ 1]))
        
        Games.append(maxred * maxgreen * maxblue)
        line = file.readline()
    print(sum(Games))