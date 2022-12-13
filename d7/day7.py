import pprint

pp = pprint.PrettyPrinter(depth=6)

f = open("input.txt")

filesystem = {}

def parsedir(directory):
    size = 0
    while True:
        line = f.readline().strip()
        print(line)
        if line == "":
            return directory

        #go back if dir = .., else recursively make folder
        elif line[0:4] == "$ cd":
            dirname = line[4:].strip()
            if dirname == "..":
                return directory
            else:
                directory[dirname] = parsedir({})
                #return directory
            
        elif line[0:5] == "$ ls":
            pass
        #add to directory
        elif line[0:3] == "dir":
            pass
        else:
            files = line.split(" ")
            #directory[files[1]] = files[0]
            size += int(files[0])
            directory['size'] = size

        
parsedir(filesystem)

pp.pprint(filesystem)

anspart1 = 0
sizeslist = []
def dirsize(directory):
    global anspart1
    global sizeslist
    size = 0
    for item in directory.values():
        if type(item) == dict:
            size += dirsize(item)
        else:
            size+= item
    if size < 100000:
        anspart1 += size
    sizeslist.append(size)
    return size
totalsize = dirsize(filesystem)
freespace = 70000000 - totalsize
deletefile =30000000 - freespace

print(anspart1)
for item in sorted(sizeslist):
    if item > deletefile:
        print(item)
        break

