'''
Write a function that accepts two (matrices) 2 dimensional lists a and b of unknown lengths and returns their product.
Hint: Two matrices a and b can be multiplied together only if the number of columns of the first matrix(a) is the same as the number of rows of the second matrix(b).
Do NOT use numpy module for this exercise. The input for this function will be two 2 Dimensional lists. For example if the input lists are:
a = [[2, 3, 4],
     [3, 4, 5]]
b = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]
'''

def _product_of_two_vectors_sample_(a, b):
    if len(a[0]) != len(b):
        return None
    # Create the result matrix and fill it with zeros
    output_list=[]
    temp_row=len(b[0])*[0]
    for r in range(len(a)):
        output_list.append(temp_row[:])
    for row_index in range(len(a)):
        for col_index in range(len(b[0])):
            sum=0
            for k in range(len(a[0])):
                sum=sum+a[row_index][k]*b[k][col_index]
            output_list[row_index][col_index]=sum
    return output_list


a = [[2, 3, 4],
    [3, 4, 5]]
b = [[4, -3, 12],
    [1, 1, 5],
    [1, 3, 2]]
print(_product_of_two_vectors_sample_(a,b))
#print(a[0][0]*b[0][0] + a[0][1]*b[1][0]+ a[0][2]*b[2][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]+ a[0][2]*b[2][1])