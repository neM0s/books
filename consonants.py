# Type your code here
def count_consonants(some_string):
    vovels = ('a', 'e', 'i', 'o', 'u')
    new_string = some_string.replace(" ", "")
    count = 0
    for i in new_string.lower():
        if i not in vovels:
            count = count + 1
    return count


print(count_consonants("asdad"))