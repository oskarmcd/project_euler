'''
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''
import time
from itertools import permutations

start_time = time.time()

def check(numbers):
    numbers = str(numbers)
    working_product = 0
    for number in numbers:
        number = int(number)
        working_product = working_product + (number ** 5)
    if working_product == int(numbers) and working_product > 1:
        print(working_product)
        return(working_product)
    else:
        return 0

working = 0
for x in range(1, 9876543210):
    working = working + check(x)
    # print(working)


print("--- %s seconds ---" % (time.time() - start_time))


