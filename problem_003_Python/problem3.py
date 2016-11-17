import math
base_number = 600851475143
factor_list = []
for x in range(1, int(math.sqrt(base_number))):
    if base_number % x == 0:
        factor_list.append(x)

non_prime_list = []
for number in factor_list:
    for x in range(2, int(number / 2)):
        if number % x == 0:
            try:
                factor_list.remove(number)
            except ValueError:
                print(number, "already removed")


print(factor_list)
