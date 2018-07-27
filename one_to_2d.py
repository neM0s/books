'''
Write a function named one_to_2D which receives an input list and two integers r and c as parameters and returns a new two-dimensional list having r rows and c columns.
Note that if the number of elements in the input list is larger than r*c then ignore the extra elements. If the number of elements in the input list is less than r*c
then fill the two dimensional list with the keyword None. For example if your fuction is called as hown below
'''

def one_to_2D(some_list, r, c):
    new_list = []
    element = 0
    for index in range(r):
        temporary = []
        if element <= len(some_list):
            for something in range(c):
                temporary.append(some_list[element])
                element = element + 1
            new_list.append(temporary)
    return new_list


print(one_to_2D([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 4, 4))