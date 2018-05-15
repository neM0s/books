# Type your code here
def pattern_sum(a, b):
    sum = 0
    for i in range(1, b+1):
        sum = sum + (a ** i)
    return sum

print(pattern_sum(5,3))

a = 1
b = 3
stringunio = str(a)
for i in range(b):
    stringunio = stringunio + stringunio(a)
    print str