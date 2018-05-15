my_own_list = [1, 2, 3]
print(my_own_list)

my_own_list.append(4)
print(my_own_list)
second = [5 ,6]
my_own_list.extend(second)
print(my_own_list)
list_count = my_own_list.count(1)
print(list_count)
print(my_own_list.index(1))
my_own_list.remove(3)
print(my_own_list)
my_own_list.reverse()
print(my_own_list)