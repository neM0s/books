'''
Write a function that takes a two-dimensional list (list of lists) of numbers as argument and returns a list which includes the maximum value of each column.
Assume that the length of columns is consistent in each row.
'''

def maxim_in_row(list2d):
    max_list = []
    for i in range(len(list2d)):
        temp = 0
        for x in range(len(list2d[0])):
            if list2d[i][x] > temp:
                temp = list2d[i][x]
            max_list.append(temp)
    return max_list

print(maxim_in_row(([1,2,3],[2,3,4])))