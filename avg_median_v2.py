'''
Write a function that accepts a tuple of positive integers and returns the mean and median of the integers as a tuple. For example if the input tuple is:
'''
import numpy

def _avg_median_(number_tuple):
    average = sum(number_tuple)/len(number_tuple)
    median = numpy.median(number_tuple)
    return (average, median)


print(_avg_median_((38, 39, 40, 42, 44, 44, 46, 47, 50, 50, 96)))
