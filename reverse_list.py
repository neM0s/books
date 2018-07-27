''' a function named list_to_tuples that receives a two dimensional list of strings as parameter and returns a tuple of tuples where the content of each inner list is reversed as shown below:
For example if the two dimensional list received by the function is
'''

def list_to_tuples(MY_LIST):
    return_tuple = ()
    print(len(MY_LIST))
    return_tuple[0] = ('abs')
    for row in MY_LIST:
        return_tuple = return_tuple, tuple(reversed(row))
        print(return_tuple)








print(list_to_tuples([['mean', 'really', 'is', 'jean'],['world', 'my', 'rocks', 'python']]))