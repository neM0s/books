# Type your code here
def find_gcd(some_list):
    not_found = True
    while not_found:
        not_found = False
        iteration = int(some_list[0]/2)
        for i in some_list:
            if i % iteration != 0:
                not_found=True
        if iteration == 0:
            return 1
        else:
            iteration = iteration - 2
    return iteration + 2


print(find_gcd([3, 5, 9, 11, 13]))