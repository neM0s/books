# Type your code here
def find_longest_word(some_string):
    str_list =  some_string.split()
    longest = 0
    for i in str_list:
        if len(i) > longest:
            longest = len(i)
            winner = i
    return(winner)


print(find_longest_word("sada asd sdas ad"))