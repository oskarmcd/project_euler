'''
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
'''

sample_answer = 2 ** 1000

sum = 0

for x in range(0, len(str(sample_answer))):
    sum += int(str(sample_answer)[x])

print(sum)