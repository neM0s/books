'''
Write a function which accepts an input string and returns a reverse of the input string while the case for every single character is reversed.
The input string for this function would be a sentence (words separated by spaces) consisting of alphabetic characters. For example if:'''

def reverse_words(inp_str):
    tmp_str = ""
    for i in range(len(inp_str) -1, -1, -1):
        tmp_str = tmp_str + inp_str[i].swapcase()
    return tmp_str



print(total_reverse(this is a sample test"))