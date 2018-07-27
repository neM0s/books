'''
Write a function that accepts a filename as input argument, the file contains the information about a persons expenses on milk and bread
and returns a dictionary that contains exactly the strings 'milk' and 'bread' as the keys and their floating point values in a list as values.
Each line of the file may start with a 'm' or a 'b' denoting milk or bread respectively. For example if the contents of the file are:
'''

def milk_and_bread(file_name):
    file_pointer = open(file_name, 'r')
    data = file_pointer.readlines()
    new_dic = {"milk":[], "bread": []}
    for index,row in enumerate(data):
        data[index] = row.strip()
        clear_list = row.split(" ")
        to_append = [float(clear_list[1]), float(clear_list[2]), float(clear_list[3])]
        if "m" in clear_list[0]:
            new_dic["milk"].append(to_append)
        else:
            new_dic["bread"].append(to_append)
    return new_dic


print(milk_and_bread("file_name"))