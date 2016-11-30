'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

import time
start_time = time.time()

def is_amicable(number):

    list_of_divisors = []
    sum = 0

    for x in range(1, number): # gets divisors
        if number % x == 0:
            list_of_divisors.append(x)
    # print(list_of_divisors, number)

    for numbers in list_of_divisors: # gets sum of divisors for first number
        sum = sum + numbers

    list_of_divisors = []

    for x in range(1, (sum)):  # gets divisors of sum of divisors of first number
        if sum % x == 0:
            list_of_divisors.append(x)

    sum2 = 0

    for numbers in list_of_divisors: # gets sum of divisors sum of divisors of first number
        sum2 = sum2 + numbers

    # print("sum of divisors of ", sum, " is ", sum2)

    if sum2 == number and sum != number:
        print(sum, number)
        return sum2

    # else:
        # print(sum,"-", "is not amicable to", number)
list = []
for x in range(0,10000):
    if is_amicable(x) != None:
        list.append(is_amicable(x))

print(list)
sum = 0

for numbers in list:
    sum = sum + numbers

print(sum)

print("--- %s seconds ---" % (time.time() - start_time))



