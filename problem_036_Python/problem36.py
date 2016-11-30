'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''


def palindrome_check(number):
    number = str(number)
    if len(number) > 0:
        if number[0] == number[-1]:
            return palindrome_check(number[1:-1])
        else:
            return False
    else:
        return True

sum = 0
for x in range(1,1000001):
    if palindrome_check(x):
        if palindrome_check("{0:b}".format(x)):
            sum = sum + x

print(sum)
