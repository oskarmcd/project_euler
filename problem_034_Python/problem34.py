import math
counter = 1
while True:
    working_value = 0
    counter = str(counter)
    for number in counter:
        working_value = working_value + math.factorial(int(number))
    if working_value == int(counter):
        print(counter)
    counter = int(counter)
    counter = counter + 1

