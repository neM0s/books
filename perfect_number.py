def perfect_number(number):
    tmp_list = []
    returned = False
    for i in range(1, number):
        if number % i == 0:
            print(i)
            tmp_list.append(i)
    sum=0
    for i in tmp_list:
        sum=sum+i
        print(sum)
    if sum == number:
        returned=True
    return returned

print(perfect_number(28))