'''
Write a function named multiplication_table that receives a positive integer 'n' as parameter and returns a n by n multiplication table as a two-dimensional list.
'''

def multiplication_table(n):
    new_list = [[] for _ in range(n)]
    multi = 1
    for i in range(n):
        for x in range(1, n+1):
            new_list[i].append(x * multi)
        multi = multi + 1
    return(new_list)

print(multiplication_table(4))