'''Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.'''
list_calc = range(2000, 3201)
result = []

for i in list_calc:
    if i % 7 == 0 and i % 5 != 5:
        result.append(i)
print result