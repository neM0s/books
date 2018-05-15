def make_incrementor (n): return lambda x: x + n
f = make_incrementor(2)
g = make_incrementor(6)

print f(42), g(42)

if 0:
    print("yes")
else:
    print("no")


if "a" in "there" or 6 % 2:
    print('true')
else:
    print('false')

print(6 % 2)

my_list = [ "cat", 2, "dog", 4]
x = 5 in my_list
print(x)
if x:
    print('yes')
else:
    print('no')

user_input = int(input("Please provide number: "))
if not user_input % 3:
    print("doto")

if 6/7:
    print('three')
elif 5 :
    print('five')
else:
    print('zero')

x == 0
print(not c)