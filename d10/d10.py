x = 1
cycles = []

for line in open("input.txt"):
    line = line.strip().split()
    if line[0] == "noop":
        cycles.append(x)
    if line[0] == "addx":
        line[1] = int(line[1])
        cycles.append(x)
        cycles.append(x)
        x = x + line[1]


idx = 19
accum = 0
while idx < len(cycles):
    accum += cycles[idx]*(idx+1)
    idx += 40
print(accum)
        
image = ""
for row in [cycles[i:i+40] for i in range(0,len(cycles),40)]:
    for idx,x in enumerate(row):
        if x-1 <= idx <= x+1:
            image +='#'
        else: image += '.'
    print(image)
    image = ''



