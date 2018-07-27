'''
Write a function that takes a string as input argument and returns a dictionary of vowel counts i.e.
the keys of this dictionary should be individual vowels and the values should be the total count of those vowels.
You should ignore white spaces and they should not be counted as a character. Also note that a small letter vowel is equal to a capital letter vowel.
'''


def vovel_counts(string1):
    vovels = "a, e, i, o, u"
    return_dict = {}
    string1 = string1.replace(" ","")
    for i in string1.lower():
        if i in vovels:
            return_dict[i] = string1.count(i)
    return return_dict


print(vovel_counts("total something"))