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