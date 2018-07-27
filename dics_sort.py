'''
Write a function that accepts a dictionary as input which contains the names and grades of students (The keys are student names and the values are lists of grades for 3 exams (1 Dimensional list))
 and returns the list of names for those students whose grade on all three exams is greater than or equal to 78.
'''


def _dictionary_names_grades_sample_(sample_dictionary):
    output_list = []
    keys = sample_dictionary.keys()
    for k in keys:
        each_list = sample_dictionary[k]
        grade1, grade2, grade3 = each_list[0], each_list[1], each_list[2]
        if grade1 >= 78 and grade2 >= 78 and grade3 >= 78:
            output_list.append(k)
    return output_list


print(_dictionary_names_grades_sample_({'Hectar': [80, 50, 0], 'John': [70, 80, 85], 'Undertaker': [90, 92, 93], 'Priest': [75, 78, 83], 'Henry': [80, 85.2, 88]}))