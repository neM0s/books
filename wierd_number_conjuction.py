# Type your code here
def pattern_sum(a, b):
    tmp_string = str(a)
    list_addition = []
    sum = a
    for i in range(1,b):
        tmp_string = tmp_string + str(a)
        list_addition.append(tmp_string)
    for x in list_addition:
        sum = sum + int(x)
    return sum

print(pattern_sum(5,3))