'''
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
digits: https://projecteuler.net/problem=13

'''
with open('numbers.txt') as f:
    numbers = [i.split() for i in f.readlines()]

working_value = 0

for rows in numbers:
    working_value = working_value + int(rows[0])

print(str(working_value)[:10])
