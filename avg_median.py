'''
Write a function that accepts a tuple of positive integers and returns the mean and median of the integers as a tuple. For example if the input tuple is:
'''
#from __future__ import division

def _avg_median_(number_tuple):
    sorted_tuple = sorted(number_tuple)
    if len(number_tuple) % 2 == 0:
        median_index = int((len(number_tuple) / 2) - 1)
        lenght = 2
    else:
        median_index = int((len(number_tuple) // 2))
        lenght = 1
    count = 0
    summary = 0
    median = 0
    for number in number_tuple:
        summary = summary + number
        count = count + 1
    average = float(summary) / count
    print sorted_tuple
    for i in range(lenght):
        median = median + sorted_tuple[median_index]
        median_index = median_index + 1
    return (average, median/float(lenght))


print(_avg_median_((38, 39, 40, 42, 44, 44, 46, 47, 50, 50, 96)))
