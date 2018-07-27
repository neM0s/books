'''
Write a function named find_word_horizontal that accepts a 2-dimensional list of characters (like a crossword puzzle) and a string (word) as input arguments.
This function searches the rows of the 2d list to find a match for the word.
If a match is found, this functions returns a list containing row index and column index of the start of the match, otherwise it returns the value None (no quotations).
'''

def find_word_vertical(list2d, string1):
    first_letter_table = []
    for row in range(len(list2d)):
        for element in range(len(list2d[row])):
            if string1[0] == list2d[row][element]:
                first_letter_table.append([row, element])
    for element in first_letter_table:
        match = 0
        frs = element[0]
        sec = element[1]
        row_lenght = len(list2d[frs])
        for letter in string1:
            if sec < row_lenght:
                if letter != list2d[frs][sec]:
                    match = match - 1
                else:
                    match = match + 1
                    if match == len(string1):
                        return element
                frs = frs + 1
    return None



crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
word='cat'
print(find_word_vertical(crosswords,word))