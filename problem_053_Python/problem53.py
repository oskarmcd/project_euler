import math
'''
How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?
'''

def get_combin(n, r):
    if r > n:
        return 0
    val = ((math.factorial(n)) / ((math.factorial(r)) * (math.factorial(n-r))))
    return val

counter = 0
for n in range(1,101):
    for r in range(1,101):
        if get_combin(n, r) > 1000000:
            counter += 1

print(counter)