'''
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''
import time
start_time = time.time()

first_number = 0
second_number = 1
print(first_number)
print(second_number)
counter = 99
total = 1
x = 1
while len(str(second_number)) < 1001:
    x = x + 1
    second_number = first_number + second_number
    if len(str(second_number)) == 1000:
        print(x, second_number)
        break
    first_number = second_number - first_number

print("--- %s seconds ---" % (time.time() - start_time))
