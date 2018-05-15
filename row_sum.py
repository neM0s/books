# Type your code here

def row_sum(list2d):
    sam_list = []
    for i in list2d:
        sam = 0
        for x in i:
            sum = sum + x
        sam_list.append(sam)
    return sam_list