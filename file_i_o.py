'''
Write a function that accepts a file name as input argument and constructs and returns a nested dictionary from it.
The keys of this dictionary should be last names, and the values should be dictionaries that contain first names as the keys and integer ages as the values.
Note that the data may contain multiple people with the same last name, but it will have unique first names.
Ignore any lines that start with '#' The file will contain comma separated values (CSV) For example if the contents of the file are:
{'Abbey': {'Matthew': 65, 'Courtney': 67, 'Lucas': 60, 'Mark': 60},
 'Orion': {'Chloe': 49, 'Resa': 86, 'Eva': 76, 'Joseph': 45},
 'Adams': {'Krishna': 35, 'Yohaan': 54}}
'''

def _file_io_(filename):
    input_file = open(filename)
    some_data = input_file.readlines()
    new_dict = {}
    for index,row in enumerate(some_data):
        row = row.strip()
        surname, name, age = row.split(",")
        if name not in new_dict.keys():
            new_dict[name] = {surname: age}
        else:
            new_dict[name].update({surname: age})
        return new_dict





print(_file_io_("file_name"))