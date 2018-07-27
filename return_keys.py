'''
Write a function named return_keys which accepts a dictionary and an integer as input and returns an ascending sorted list of all the keys whose values contain the input integer.
Note that the keys of this dictionary are strings while the values of this dictionary are 1 Dimensional lists of integers.
For example if the input dictionary is:
'''


def return_keys(dict1,number1):
    list_returned = []
    for key in dict1.keys():
        if number1 in dict1[key]:
            list_returned.append(key)
    list_returned.sort()
    return list_returned

sample_dictionary = {"rabbit" : [1, 2, 3],
          "kitten" : [2, 2, 6],
          "lioness": [6, 8, 9]}
print(return_keys(sample_dictionary, 2))