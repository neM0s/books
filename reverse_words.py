def find_mismatch(s1, s2):
    new_s1 = s1.lower()
    new_s2 = s2.lower()
    len_s1 = len(new_s1)
    len_s2 = len(new_s2)
    counter = 0
    if len_s1 - len_s2 > 1 or len_s2 - len_s1 > 1:
        return 2
    elif len_s1 > len_s2 or len_s2 > len_s1:
        return 2
    else:
        for i in range(0, len_s2-1):
            if new_s2[i] != new_s1[i]:
                counter = counter +1
    if counter > 1:
        return 2
    elif counter == 1:
        return 1
    else:
        return 0


print(find_mismatch('sin', 'sink'))