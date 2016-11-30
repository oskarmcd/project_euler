biggest_sum = 0
biggest_x = 0
biggest_y = 0


for x in range(1,100):
    for y in range(1,100):
        working_sum = 0
        number = x ** y
        for z in range(0, len(str(number))):
            working_sum = int(str(number)[z]) + working_sum
        # print(x, y, working_sum)
        if working_sum > biggest_sum:
            biggest_sum = working_sum
            biggest_x = x
            biggest_y = y


print(biggest_x, biggest_y, biggest_sum)