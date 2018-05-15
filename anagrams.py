# Type your code here
def test_for_anagrams(my_string1, my_string2):
    lexicon1 = my_string1.lower().split()
    lexicon2 = my_string2.lower().split()
    for i in lexicon1:
        if i in lexicon:
            lexicon.pop(i)
        else:
            return False
    return True


print(test_for_anagrams("colon", "nooloc"))