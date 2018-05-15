'''
Write a function that takes a string consisting of alphabetic characters as input argument and returns the lower case of the most common character.
Ignore white spaces i.e. Do not count any white space as a character.
Note that capitalization does not matter here i.e. that a lower case character is equal to a upper case character.
In case of a tie between certain characters return the last character that has the most count
'''

def most_common_chr(inp_str):
    count = 0
    winner = ""
    new_str = inp_str.lower()
    new_str= new_str.replace(" ","")
    for i in new_str:
        if new_str.count(i) >= count:
            count = new_str.count(i)
            winner = i
    return winner




print(most_common_chr("The cosmos is infinite"))