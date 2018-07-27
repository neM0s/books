'''
Write a function that accepts a string which contains a particular date from the Gregorian calendar. Your function should return what day of the week it was.
Here are a few examples of what the input string(Month Day Year) will look like. However, you should not 'hardcode' your program to work only for these input!
day of the week (w) = (d + floor(2.6m - 0.2) - 2c + y + floor(y/4) + floor(c/4)) modulo 7
'''


import numpy
def _day_of_the_week_(string_date):
    months = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
    week = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
    century = int(string_date[-4:-2])
    year = int(string_date[-2:])
    string_split = string_date.split()
    day = int(string_split[1])
    month = months[string_split[0]]
    day_week = int((day + numpy.floor((2.6*month) - 0.2) - (2*century) + year + (numpy.floor(year / 4)) + numpy.floor(century / 4)) % 7)
    return week[day_week]


print(_day_of_the_week_("May 5 1992"))
