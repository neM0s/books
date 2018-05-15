def max_number(list):
    biggest = 0
    for i in list:
        if i > biggest:
            biggest = i
    return(biggest)

print(max_number([1,2,3]))