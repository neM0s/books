# Type your code here
def MY_2D_LIST(n):
    result = [[1]]
    for number in range(1, n):
        tmp_list = [1]
        for second_number in range(1, number):
            value = (result[number-1][second_number-1] + result[number-1][second_number])
            tmp_list.append(value)
        tmp_list.append(1)
        result.append(tmp_list)
    return result




print(MY_2D_LIST(8))