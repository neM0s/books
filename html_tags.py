import re
file = open("filename5")
for row in file:
    tmp = re.search(r"<([a-z]+)>(.*)</\1>", row)
    print(tmp.group(1) + ": " + tmp.group(2))