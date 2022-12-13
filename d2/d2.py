f = open("input2.txt")

score = 0
for line in f:
    game = line.split()
    
    if game[1] == "X":
        score +=0
        if game[0] == "A":
            score += 3
        if game[0] == "B":
            score += 1
        if game[0] == "C":
            score += 2
    if game[1] == "Y":
        score +=3

        if game[0] == "A":
            score += 1
        if game[0] == "B":
            score += 2
        if game[0] == "C":
            score += 3
    if game[1] == "Z":
        score +=6

        if game[0] == "A":
            score += 2
        if game[0] == "B":
            score += 3
        if game[0] == "C":
            score += 1
print(score)
