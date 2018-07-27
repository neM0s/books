'''
Write a function named find_word_horizontal that accepts a 2-dimensional list of characters (like a crossword puzzle) and a string (word) as input arguments.
This function searches the rows of the 2d list to find a match for the word.
If a match is found, this functions returns a list containing row index and column index of the start of the match, otherwise it returns the value None (no quotations).
'''
def find_word_horizontal(crosswords,word):
    # insert the code from your function in part 1 here
    if not crosswords or not word:
        return None
    for index, row in enumerate(crosswords):
        tmp_str = ''.join(row)
        if tmp_str.find(word) != -1:
            horizontal_match = [index,tmp_str.index(word)]
            return horizontal_match
    return None

def find_word_vertical(crosswords,word):
    # insert the code from your function in part 2 here
    if not crosswords or not word:
        return None
    number_of_columns=len(crosswords[0])
    for col_index in range (number_of_columns):
        temp_str=''
        for row_index in range(len(crosswords)):
            temp_str=temp_str+crosswords[row_index][col_index]
        if temp_str.find(word)>=0:
            return [temp_str.find(word),col_index]
    return None

def capitalize_word_in_crossword (crosswords,word):
    horizontal_find = find_word_horizontal(crosswords,word)
    vertical_find = find_word_vertical(crosswords,word)
    word_lengh = len(word)
    if horizontal_find != None:
        horizontal_index = horizontal_find[1]
        for i in range(word_lengh):
            crosswords[horizontal_find[0]][horizontal_index] = crosswords[horizontal_find[0]][horizontal_index].upper()
            horizontal_index = horizontal_index + 1
        return crosswords
    if vertical_find != None:
        vertical_index = vertical_find[0]
        for i in range(word_lengh):
            crosswords[vertical_index][vertical_find[1]] = crosswords[vertical_index][vertical_find[1]].upper()
            vertical_index = vertical_index + 1
        return crosswords
    else:
        return crosswords


crosswords=[['s', 'd', 'o', 'g'], ['c', 'u', 'c', 'm'], ['a', 'c', 'a', 't'], ['t', 'e', 't', 'k']]
word='car'
print(capitalize_word_in_crossword(crosswords,word))