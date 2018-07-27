'''
Write a function that takes a 4 digit integer (from 1000 to 9999 both inclusive) as input argument and returns the integer using words as shown below:
if the input integer is 9900 then the function should return the string "nine thousand nine hundred"
one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen,
sixteen, seventeen, eighteen, nineteen, twenty, thirty, forty, fifty, sixty, seventy, eighty,
ninety, hundred, thousand
'''

def _number_to_words_(number):
    low_numbers = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}
    mid_numbers = {0: "ten", 1: "eleven", 2: "tvelve", 3: "thirteen", 4: "fourteen", 5: "fifteen", 6: "sixteen", 7: "seventeen", 8: "eighteen", 9: "nineteen"}
    high_number = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
    str_number = str(number)
    first, second, third, fourth = str_number[0], str_number[1], str_number[2], str_number[3]
    return_string = ""
    return_string = low_numbers[int(first)] + " thousand"
    if int(second) > 0:
        return_string = return_string + " " + low_numbers[int(second)] + " hundred"
    if int(third) > 1:
        return_string = return_string + " " + high_number[int(third)]
        if int(fourth) > 0:
            return_string = return_string + " " + low_numbers[int(fourth)]
    elif int(third) == 1 and int(fourth) > 0:
        return_string = return_string + " " + mid_numbers[int(fourth)]
    elif int(third) == 1 and int(fourth) == 0:
        return_string = return_string + " ten"
    elif int(third) == 0 and int(fourth) > 0:
        return_string = return_string + " " + low_numbers[int(fourth)]
    return return_string




print(_number_to_words_(1029))
