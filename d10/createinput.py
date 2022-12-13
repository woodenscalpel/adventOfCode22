outputs = ["...#..#.###...###..###.####.###.........",
           "...#..#.###...##....#..#....#..#........"
           "...#..#..#...#..#....#.#....#.#.........",
           "...#..#..#........#....####.#..#........",
           "...#..#..#...#....#....#....#..#........",
           "...#..#..#...#.##.#.##.#....###.........",]
prevx = 1

out = open("myinput.txt","w")
for output in outputs:
    blocks = [output[i:i+2] for i in range(0,len(output),2)]

    currentcycle = 2
    instructions = []
    for block in blocks:
        if block == "..":
            instructions.append(0)
        if block == ".#":
            instructions.append((currentcycle+2))
        if block == "#.":
            instructions.append((currentcycle-1))
        if block == "##":
            instructions.append(currentcycle)
        
        currentcycle += 2

    in2 = []
    for item in instructions:
        diff = item-prevx
        in2.append(diff)
        prevx = item


    for instruction in in2:
        if instruction == 0:
            out.write("noop\nnoop\n")
        else:
            out.write("addx "+str(instruction)+"\n")
