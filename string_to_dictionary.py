'''
Write a function that takes a string as input argument and returns a dictionary of letter counts i.e.
the keys of this dictionary should be individual letters and the values should be the total count of those letters.
You should ignore white spaces and they should not be counted as a character.
Also note that a small letter character is equal to a capital letter characte
'''


def string_to_dictionary(string1):
    temp_list = []
    return_dict = {}
    string1 = string1.replace(" ","")
    for x in string1.lower():
        temp_list.append(x)
    temp_list = list(set(temp_list))
    for i in temp_list:
        return_dict.update({i: string1.lower().count(i)})
    return return_dict


print(string_to_dictionary('resting in the heart of all men is Brahma'))