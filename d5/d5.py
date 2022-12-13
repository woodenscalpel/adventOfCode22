
stacks = [line.strip() for line in open("start.txt")]

instructions = [line.strip().split(" ") for line in open("input.txt")]

for instruction in instructions:
    amt = int(instruction[1])
    start = int(instruction[3]) - 1
    end = int(instruction[5]) - 1

    #print(stacks[start])
    #print(amt)
    #print(stacks[start][-amt:])

    leftover = stacks[start][:len(stacks[start])-amt]

    #chunk = stacks[start][-amt:][::-1]   #PART 1
    chunk = stacks[start][-amt:]   #PART 2

    stacks[start] = leftover
    stacks[end] = stacks[end] + chunk
    print("STEP",stacks)

print(stacks)
