# Type your code here
def calculate_expenses(filename):
    input_file = open(filename)
    some_data = input_file.readlines()
    sorted_list_tupes = []
    hidden_dictionary = {}
    for row in some_data:
        tuple_len = len(sorted_list_tupes)
        product,price = row.split(",")
        product,price = product.strip(),price.strip()
        if product not in hidden_dictionary.keys():
            hidden_dictionary[product] = 1
        else:
            hidden_dictionary[product] += 1
        price_string = ('${:.2f}'.format(float(price)))
        tmp_list = (product, price_string)
        if len(sorted_list_tupes) == 0:
            sorted_list_tupes.append(tmp_list)
            continue
        for index,item in enumerate(sorted_list_tupes):
            if sorted_list_tupes[index][0] == product:
                print(sorted_list_tupes[index][1], price, hidden_dictionary[product], product, price)
                average_price = (float(sorted_list_tupes[index][1][1:]) + float(price))/hidden_dictionary[product]
                tmp_list = (product, average_price)
            if (index + 1) == tuple_len:
                sorted_list_tupes.append(tmp_list)
                break
            if product < item[0]:
                sorted_list_tupes.insert(index,tmp_list)
                break


print(calculate_expenses("file_name4"))