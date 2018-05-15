def mystrip(string1):
    new_string = string1
    if string1[-1] == " ":
        for i in string1[-1:0:-1]:
            print "+" + "i:" + i +"end" + new_string + " " + "+"
            if i == " ":
                new_string = new_string[:-1]
            else:
               break
    return new_string

mystring="  We love python    "
print(mystrip(mystring))