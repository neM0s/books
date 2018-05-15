def mystrip(string1):
    new_string = ""
    for i in string1:
        utf_number = ord(i)
        if utf_number > 96 and utf_number < 123:
            actual = chr(utf_number - 32)
            new_string = new_string + actual
        elif utf_number > 64 and utf_number < 91:
            actual = chr(utf_number + 32)
            new_string = new_string + actual
        else:
            new_string = new_string + i
    return new_string

string1="Python RocKS MY WORLD"
print(mystrip(string1))