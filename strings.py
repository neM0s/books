format = "First %30s, and now second %s"
string_value = ("one", "second")

print(format % string_value)

from math import pi

print("float with 3 precision %.3f" % pi)

from string import Template

s = Template('$first is going $second')
print(s)
n = s.substitute(first='jasiek', second='down')
print(n)


float = "A: %+07.2f"
value2 = -10.12345
print(float % value2)

float3 = "A: %+07.2f"
value3 = 10.12345
print(float3 % value3)