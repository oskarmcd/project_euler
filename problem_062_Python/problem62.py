
dict = {}
x = 0
print("start")

while True:
    # print("x val:",x, "cubed",x ** 3)
    print(x)
    # list[x ** 3] = list[x ** 3] + 1
    if ''.join(sorted(str(x ** 3))) in dict:
        dict[''.join(sorted(str(x ** 3)))][0] = dict[''.join(sorted(str(x ** 3)))][0] + 1
        if dict[''.join(sorted(str(x ** 3)))][0] == 5:
            print("found", dict[''.join(sorted(str(x ** 3)))][0])
            print("found", dict[''.join(sorted(str(x ** 3)))][1])
            # print(x ** 3)
            break
    else:
        dict[''.join(sorted(str(x ** 3)))] = []
        dict[''.join(sorted(str(x ** 3)))].append(1)
        dict[''.join(sorted(str(x ** 3)))].append(x ** 3)

    x  = x + 1

# print(dict)

