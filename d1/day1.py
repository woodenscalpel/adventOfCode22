
f = open("input1.txt")

elfcals = 0
elfs = []
for line in f:
    if line == "\n":
        elfs.append(elfcals)
        elfcals = 0
    else:
        elfcals += int(line)
print(max(elfs))

accum = 0
for i in range(3):
    accum += max(elfs)
    elfs.remove(max(elfs))
print(accum)

