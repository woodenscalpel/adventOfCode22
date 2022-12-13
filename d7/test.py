f = open("test.txt")

def testf(file):
    print(file.readline())
    return file

print(testf(f))
print(testf(f))
print(testf(f))
