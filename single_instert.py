# Type your code here
def single_insert_or_delete(s1,s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    low_s1 = s1.lower()
    low_s2 = s2.lower()
    if abs(len_s1 - len_s2) > 1:
        return 2
    elif low_s1 == low_s2:
        return 0
    elif len_s1 > len_s2:
        for i in range(len_s2):
            if low_s1[i] != low_s2[i]:
                if low_s1[i+1:] != low_s2[i:]:
                    return 2
                else:
                    return 1
    else:
        for i in range(len_s1):
            if low_s1[i] != low_s2[i]:
                if low_s1[i:] != low_s2[i+1:]:
                    return 2
                else:
                    return 1



print(single_insert_or_delete("doga", "Dog"))