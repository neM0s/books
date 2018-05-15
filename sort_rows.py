def sort_row(list2d):
    for rows in list2d:
        rows.sort(reverse=True)
    return list2d

print(sort_row([[4, 2, 3, 4], [0, 5, 3, 2], [-5, -2, 13, 4], [12, 11, 30, -20]]))