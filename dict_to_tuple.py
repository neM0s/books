'''
Write a function that accepts a dictionary as input and returns a tuple of tuples. That is your first tuple should be the tuple of all the keys,
and the second tuple should be tuple of all the values in the dictionary. For example if the input dictionary is:
'''

def _dict_to_tuple_(dict1):
    values = sorted(dict1.values())
    keys = sorted(dict1.keys())
    return (keys,values)


print(_dict_to_tuple_({1:"a", 2:"b", 3:"c", 4:"d"}))
