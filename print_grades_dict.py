# Type your code here
import re
def create_grades_dict(file_name2):
    input_file = open(file_name2)
    some_data = input_file.readlines()
    parsed_dict = {}
    return_dict = {}
    name_dict = {}
    for row in some_data:
        row_list = row.split(",")
        if row[0] not in name_dict:
            name_dict[row_list[0]] = row_list[1]
        for item in row_list:
            if row_list[0].strip() in parsed_dict:
                if re.search("Test_[1-4]", item.strip()) is not None:
                    indexik=row_list.index(item)
                    parsed_dict[row_list[0]].update({row_list[indexik].strip(): int(row_list[indexik+1])})
            else:
                if re.search("Test_[1-4]", item.strip()) is not None:
                    indexik=row_list.index(item)
                    parsed_dict[row_list[0]] = {row_list[indexik].strip(): int(row_list[indexik+1])}
    for key in parsed_dict.keys():
        return_dict[key] = [name_dict[key].strip()]
        sum = 0
        for i in range(1,5):
            if "Test_" + str(i) in parsed_dict[key]:
                sum = sum + parsed_dict[key]["Test_" + str(i)]
                return_dict[key].append(parsed_dict[key]["Test_" + str(i)])
            else:
                return_dict[key].append("0")
        return_dict[key].append(sum/4)
    return return_dict
def print_grades(file_name2):
    # Call your create_grades_dict() function to create the dictionary
    grades_dict=create_grades_dict(file_name2)
    print("{0: ^10s} | {1: ^16s} | {2: ^5}1 | {2: ^5}2 | {2: ^5}3 | {2: ^5}4 | {3: ^6} |".format("ID","Name","Test_","Avg."))
    for row in sorted(grades_dict.keys()):
        print("{: ^10s} | {: <16s} | {: >6} | {: >6} | {: >6} | {: >6} | {: >6.2f} |".format(row, grades_dict[row][0], grades_dict[row][1],grades_dict[row][2],grades_dict[row][3],grades_dict[row][4],grades_dict[row][5]))
print_grades("file_name2")