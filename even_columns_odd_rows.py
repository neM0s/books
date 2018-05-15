'''
Write a function that will receive a 2D list of integers. The function should return the count of how many rows of the list have even sums and the count of how many rows have odd sums.
For example if the even count was 2, and odd count was 4 your function should return them in a list like this: [2, 4].
'''

def even_columns_odd_rows(list2d):
    odd_sum = 0
    even_sum = 0
    for rows in list2d:
        if sum(rows) % 2 == 0:
            even_sum = even_sum + 1
        else:
            odd_sum = odd_sum + 1
    return [even_sum, odd_sum]


print(even_columns_odd_rows(([1,2,3,4],[4,5,3,6],[9,8,3,4])))

