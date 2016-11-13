"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?s
"""

def is_number_prime(number):
    if number % 2 == 0:
        return False
    for x in range ((number-1), 2 ,-1):
        if (number % x) == 0:
            return False
    return True

counter = 1
prime_counter = 1
while prime_counter != 10001:
    counter += 1
    print(prime_counter)
    if is_number_prime(counter):
        prime_counter += 1
print(counter)


