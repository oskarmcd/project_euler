'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

i personally removed all quotation marks to name list.
'''
with open('unordered.txt') as f:
    names = [i.split(",") for i in f.readlines()]

names = sorted(names[0])
names = [x.lower() for x in names]

def score(index_value, name):
    alphabet_value = 0
    for letter in name:
        letter_value = 0
        letter_value = ord(letter) - 96
        alphabet_value = alphabet_value + letter_value
    return (index_value * alphabet_value)

counter = 1
total_val = 0
for name in names:
    total_val = total_val + score(counter, name)
    counter = counter + 1

print(total_val)