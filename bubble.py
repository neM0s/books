# Type your code here
def _sorting_fun(org_list):
    new_list = org_list
    lenght = 0
    for i in org_list:
        lenght=lenght + 1
    finished = True
    while finished:
        finished = False
        for i in range(0,lenght-1):
            if new_list[i] > new_list[i+1]:
                temp = new_list[i]
                new_list[i] = new_list[i+1]
                new_list[i+1] = temp
                finished = True
    return new_list


print(_sorting_fun([6,3,1]))