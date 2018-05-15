# Type your code here
def single_insert_or_delete(s1,s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    low_s1 = s1.lower()
    low_s2 = s2.lower()
    tmp_s1 = low_s1
    tmp_s2 = low_s2
    if len_s1 == len_s2:
        for i in range(0, len_s1-1):
            if low_s1[i] != low_s2[i]:
                return 2
    elif len_s1 - len_s2 > 1 or len_s2 - len_s1 > 1:
        return 2:
    else:
        for i in range(0,len_s1-1):
            if low_s1[i] != low_s2[i]:



print(single_insert_or_delete("dog", "Dog"))