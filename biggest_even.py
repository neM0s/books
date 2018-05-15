# Type your code here
def biggest_even(list2d):
    max = 0
    for i in list2d:
        for x in i:
            if x % 2 == 0:
                print ("even", x)
                if x > max:
                    max = x
    if x:
        return max
    else:
        return None


print biggest_even([[1, 2, 3, 5], [1, 5, 3, 5]])