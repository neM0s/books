# Type your code here
def crazy_list(some_list):
    iteration = -1
    lenght=len(some_list)/2+1
    for i in range(0, int(lenght)):
        if some_list[i] != some_list[iteration]:
            return False
        iteration = iteration - 1
    return True



let_test=[5, 6, 8, 9, 'PYTHON', 9, 8, 6, 5]
crazy_list(let_test)