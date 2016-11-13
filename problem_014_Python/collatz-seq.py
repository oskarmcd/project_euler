"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""
def length_collatz(subject):
    og_subject = subject
    counter = 1
    while subject != 1:
        if subject % 2 == 0:
            counter += 1
            subject = subject / 2
        else:
            counter += 1
            subject = (3*subject) + 1
    subject_counter = (og_subject, counter)
    return subject_counter


def is_it_longest(tuple_val, max_so_far):
    if tuple_val[1] > max_so_far:
        return True

max_so_far = 0
longest_number = 0
for x in range(1, 1000000):
    print(x)
    current_it = length_collatz(x)
    if is_it_longest(current_it, max_so_far):
        max_so_far = current_it[1]
        longest_number = current_it[0]

print(longest_number)
