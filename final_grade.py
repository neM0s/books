import math
def avg_q(list):
    sorted_list = (sorted(list))
    sorted_list = sorted_list[2:]
    return (sum(sorted_list)/4)

def avg_a(list):
    sorted_list = (sorted(list))
    sorted_list = sorted_list[1:]
    return (sum(sorted_list)/3)

def final_grade_calc(file_name):
    file_opened = open(file_name, "r")
    some_data = file_opened.readlines()
    result = {}
    for row in some_data:
        name, q1, q2, q3, q4, q5, q6, a1, a2, a3, a4, midterm, final = row.strip().split(",")
        average_q = avg_q((int(q1.strip()), int(q2.strip()), int(q3.strip()), int(q4.strip()), int(q5.strip()), int(q6.strip())))
        average_a = avg_a((int(a1.strip()), int(a2.strip()), int(a3.strip()), int(a4.strip())))
        average = (average_a + average_q + int(midterm) + int(final)) / 4
        if average >= 60:
            result[name] = "pass"
        else:
            result[name] = "fail"
    return result

print(final_grade_calc("file_name5"))