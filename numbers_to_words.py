'''
Write a function that takes an integer as input argument and returns the integer using words. For example if the input is 4721 then the function should return the string "four seven two one".
Note that there should be only one space between the words and they should be all lowercased in the string that you return.
'''


def _number_to_words_(integer1):
    numbers = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    return_int = ''
    str_int = str(integer1)
    for i in str_int:
        return_int = return_int + " " + (numbers[int(i)])
    return return_int.lstrip()


print(_number_to_words_(3627))