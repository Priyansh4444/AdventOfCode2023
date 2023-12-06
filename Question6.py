inputs, *blocks = open('lines.txt','r+').read().split("\n\n")

inputs = list(map(int, inputs.split(":")[1].split()))
