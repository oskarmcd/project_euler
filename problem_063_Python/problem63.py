list = []
for x in range(1,1000):
    for y in range(1,1000):
        if len(str(x ** y)) == y:
            list.append(str(x**y))
            print(len(list))
