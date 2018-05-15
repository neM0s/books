# Type your code here

def column_sum(list2d):
    list_sam = []
    for i in range(0,len(list2d[0])-1):
        sam = 0
        for x in range(0, len(list2d)):
            sam = sam + list2d[x][i]
        list_sam.append(sam)
    return list_sam