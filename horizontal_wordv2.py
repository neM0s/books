'''
Write a function named find_word_horizontal that accepts a 2-dimensional list of characters (like a crossword puzzle) and a string (word) as input arguments.
This function searches the rows of the 2d list to find a match for the word.
If a match is found, this functions returns a list containing row index and column index of the start of the match, otherwise it returns the value None (no quotations).
'''

def _find_word_horizontal(crosswords,word):
    if not crosswords or not word : # if empty then return None
        return None
    for index,row in enumerate(crosswords):
        print(index,row)
        temp_str=''.join(row)
        if temp_str.find(word)>=0:
            return [index,temp_str.find(word)]
    return None



crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
word='cat'
print(_find_word_horizontal(crosswords,word))