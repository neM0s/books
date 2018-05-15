'''
Write a function which accepts an input string and returns a reverse of the input string while the case for every single character is reversed.
The input string for this function would be a sentence (words separated by spaces) consisting of alphabetic characters. For example if:'''

def reverse_words(inp_str):
    tmp_list = inp_str.split()
    rvs_list = []
    final_str = ""
    for i in tmp_list:
        rvs_word = ""
        for x in reversed(i):
            rvs_word = rvs_word + x
        rvs_list.append(rvs_word)
    s = " "
    final_str = s.join(rvs_list)
    return final_str



print(reverse_words("this is a sample test"))