name = list("perl")

print(name)
name[1:] = list("ython")

print(name)
name[2:2] = list("12")

print(name)
name[2:4] = []

print(name)

print(name.count('p'))