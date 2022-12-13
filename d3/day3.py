f = open("test.txt")

matches = []
for line in f:
    line = line.strip()

    halfidx = int(len(line)/2)
    bags = [line[0:halfidx],line[halfidx:]]
    exitloop = False
    for i in bags[0]:
        for j in bags[1]:
            if i == j:
                matches.append(i)
                exitloop = True
                break;
        if exitloop:
            break;

print(matches)

points = 0
for x in matches:
    if x.isupper():
        points += ord(x) - 64 + 26
    else:
        points += ord(x) - 96

print(points)

matches = []
with open("input3.txt") as file:
    while True:
        l1 = file.readline()
        l2 = file.readline()
        l3 = file.readline()
        if l1 == "" or l2 == "" or l3 == "":
            break;
        
        exitloop = False
        for i in l1:
            for j in l2:
                if i == j:
                    for k in l3:
                        if i == k:
                            matches.append(i)
                            exitloop = True
                            break;
                if exitloop:
                    break;
            if exitloop:
                break;
    file.close()
print(matches)

points = 0
for x in matches:
    if x.isupper():
        points += ord(x) - 64 + 26
    else:
        points += ord(x) - 96

print(points)
