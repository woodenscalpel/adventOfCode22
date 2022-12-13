
stacks = [line.strip() for line in open("start.txt")]
stacks2 = [line.strip() for line in open("start.txt")]
#stacks2 = stacks
instructions = [line.strip().split(" ") for line in open("input.txt")]

for instruction in instructions:
    amt,start,end = int(instruction[1]),int(instruction[3]) - 1,int(instruction[5]) - 1

    stacks[start], stacks[end] = stacks[start][:len(stacks[start])-amt],stacks[end] + stacks[start][-amt:][::-1]   #PART 1
    stacks2[start], stacks2[end] = stacks2[start][:len(stacks2[start])-amt],stacks2[end] + stacks2[start][-amt:]   #PART 2

print("Part 1: " + "".join([x[-1] for x in stacks]))
print("Part 2: " + "".join([x[-1] for x in stacks2]))
