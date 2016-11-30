'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''
def get_factorial(counter, working_value=1):
    if counter == 1:
        return working_value
    else:
        working_value = working_value * counter
        return get_factorial(counter - 1, working_value)

sum = 0
factorial = get_factorial(100)

for x in range(0, len(str(factorial))):
    sum += int(str(factorial)[x])

print(sum)