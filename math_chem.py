'''
Write a function that takes a file name (string) of a CSV file which contains the information about student's names and their grades for four courses
and returns a dictionary that contains information about the students whose grades in both Math and Chemistry is above 70.
Note that if the file has any comments (lines starting with #) then you should ignore such a line. The file will have the following format:
'''

def math_chem(file_name):
    file_pointer = open(file_name, 'r')
    data = file_pointer.readlines()
    new_dic = {}
    for index,row in enumerate(data):
        data[index] = row.strip()
        tmp_list = row.split(",")
        if "#" not in tmp_list[0]:
            if int(tmp_list[1]) > 70 and int(tmp_list[3]) > 70:
                new_dic[tmp_list[0]] = [float(tmp_list[1]), float(tmp_list[2]), float(tmp_list[3]), float(tmp_list[4])]
    return new_dic


print(math_chem("file_name"))