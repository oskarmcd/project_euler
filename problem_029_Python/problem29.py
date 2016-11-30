'''
How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
'''
list_of_values = []
for a in range(2,101):
    for b in range(2,101):
        if a**b not in list_of_values:
            list_of_values.append(a**b)

print(len(sorted(list_of_values)))