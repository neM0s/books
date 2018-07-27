import re
lines = ["surname: Obama, prename: Barack, profession: president", "surname: Merkel, prename: Angela, profession: chancellor"]
for line in lines:
    print(re.split(",* *\w*: ", line)[1:])