end = False
x = 1
while not end:
    x = x + 1
    if sorted(str(x)) == sorted(str(int(2 * x))) == sorted(str(int(3 * x))) == sorted(str(int(4 * x))) == sorted(str(int(5 * x))) == sorted(str(int(6 * x))):
        print(x)
        break
