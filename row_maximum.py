'''
Write a function named row_maximums that accepts a 2-dimensional list of numbers as parameter and returns a dictionary whose values would be the maximum value of each row
and whose keys would be the appropriate strings as specified below.
'''

# Type your code here
def row_maximums(some_multi_dimensional_list):
    results = {}
    for index,row in enumerate(some_multi_dimensional_list):
        maks = 0
        for number in row:
            if number > maks:
                maks = number
        key = 'row ' + str(index) + ' max'
        results[key] = maks
    return results

array = [[5, 0, 0, 0, 13],
 [0, 12, 0, 0],
 [20, 0, 11, 0],
  [6, 0, 0, 8]]


print(row_maximums(array))