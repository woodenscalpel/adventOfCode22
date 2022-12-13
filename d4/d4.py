f = open("in4.txt")


def overlap(team):
    for i in range(team[0][0], team[0][1]+1):
        for j in range(team[1][0], team[1][1]+1):
            if i == j:
                return 1
    return 0


silveraccum = 0
goldaccum = 0
for line in f:
    team = [[int(x) for x in pair.split("-")] for pair in line.strip().split(",")]
    if (team[0][0] <= team[1][0] and team[0][1] >= team[1][1]) or (team[1][0] <= team[0][0] and team[1][1] >= team[0][1]):
        silveraccum += 1
    goldaccum += overlap(team)

print(silveraccum)
print(goldaccum)

