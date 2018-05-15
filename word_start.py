'''Write a function that accepts a string and a character as input and returns the count of all the words in the string which start with the given character.
Assume that capitalization does not matter here. You can assume that the input string is a sentence i.e. words are separated by spaces and consists of alphabetic characters.
'''


def word_start(inp_sentence, inp_str):
    words_list = inp_sentence.lower()
    words_list = words_list.split()
    inp_str = inp_str.lower()
    sum = 0
    for i in words_list:
        if i[0] == inp_str:
            sum = sum +1
    return sum


print(word_start("asdaa sas ad rerge ada", "a"))