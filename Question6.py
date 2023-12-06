Time, Distance = open('lines.txt','r+').read().split("\n")
t = Time.strip().split(":")[1]
d = Distance.strip().split(":")[1]
t = [int(x.strip()) for x in t.split(" ") if x.strip() != ""]
d = [int(x.strip()) for x in d.split(" ") if x.strip() != ""]
races = list(zip(t,d))
raceswon = [0] * len(races)
i = 0
for race in races:
    for time in range(race[0]):
        if (race[0] - time) * time > race[1]:
            raceswon[i] += 1
    i += 1
f = 0
for race in raceswon:
    f += race   
print(f)