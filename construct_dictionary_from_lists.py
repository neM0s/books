'''
Write a function named row_maximums that accepts a 2-dimensional list of numbers as parameter and returns a dictionary whose values would be the maximum value of each row
and whose keys would be the appropriate strings as specified below.
'''

# Type your code here
def construct_dictionary_from_lists(names_list, ages_list, scores_list):
    dictionary = {}
    for index,row in enumerate(names_list):
        if scores_list[index] > 60:
            exam = "pass"
        else:
            exam = "fail"
        dictionary[names_list[index]] = [ages_list[index], scores_list[index], exam]
    return dictionary



print(construct_dictionary_from_lists(["paul", "saul", "steve", "chimpy"], [28, 59, 22, 5], [61, 85, 55, 60]))