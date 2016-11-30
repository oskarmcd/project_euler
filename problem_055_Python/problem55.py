'''
How many Lychrel numbers are there below ten-thousand?
'''

def is_palindrome(number, counter):
    number = int(number) + int(str(number)[::-1])
    number = str(number)
    if number[::-1] == number:
        return False
    elif number[::-1] != number and counter == 50:
        return True
    else:
        return is_palindrome(number, counter + 1)

counter = 0
for x in range(1, 10000):
    if is_palindrome(x, 0):
        print(x)
        counter = counter + 1
print(counter)
