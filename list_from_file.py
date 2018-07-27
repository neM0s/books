'''
Write a function named one_to_2D which receives an input list and two integers r and c as parameters and returns a new two-dimensional list having r rows and c columns.
Note that if the number of elements in the input list is larger than r*c then ignore the extra elements. If the number of elements in the input list is less than r*c
then fill the two dimensional list with the keyword None. For example if your fuction is called as hown below
'''

def math_chem(file_name):
    file_pointer = open(file_name, 'r')
    data = file_pointer.readlines()
    new_dic = {}
    for index,row in enumerate(data):
        if int(tmp_list[1]) >
        data[index] = row.strip()
        tmp_list = row.split(",")
        new_dic[tmp_list[0]] = [float(tmp_list[1]), float(tmp_list[2]), float(tmp_list[3]), float(tmp_list[4])]
    return new_dic


print(list_from_file("file_name"))