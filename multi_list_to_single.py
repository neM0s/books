'''
Write a function that accepts a 2-dimensional list of integers, and returns a sorted (ascending order) 1-Dimensional list containing all the integers from the original 2-dimensional list.
'''


def list2d_to_list1d(list2d):
    new_list = []
    for i in list2d:
        new_list = new_list + i
    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(len(new_list)-1):
            if new_list[i+1] < new_list[i]:
                unsorted = True
                temp = new_list[i]
                new_list[i] = new_list[i+1]
                new_list[i+1]=temp
    return new_list

print(list2d_to_list1d(([2,5,3],[5,2,7],[8,9,4])))