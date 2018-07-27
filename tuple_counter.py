def calculate_grades(file_name):
    # Make a connection to the file
    file_pointer = open(file_name, 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    return_tuple = ()
    for row in data:
        row_to_list = row.split(",")
        sum = 0
        lenght = len(row_to_list[1:])
        for i in row_to_list[1:]:
            sum = sum + int(i)
        return_tuple = return_tuple + ((row_to_list[0], sum / lenght),)
    return return_tuple


print(calculate_grades("file_name3"))