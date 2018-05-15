# Type your code here
n=int(input('please enter an integer between 1 and 9999: '))
under_twenty = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
"sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
under_hundred = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

thousand=n//1000
hundred=(n%1000)//100
tens=(n%100)//10
singulars=n%10
printer=''
print(tens, singulars)


if thousand > 0:
    printer=under_twenty[thousand-1] + " thousand "
if hundred > 0:
    printer=printer + under_twenty[hundred-1] + " hundred "
if tens >= 2:
    printer=printer + under_hundred[tens-1] + " " + under_twenty[singulars-1]
if tens == 1:
    printer=printer + under_twenty[singulars+9]
else:
    printer=printer + under_twenty[singulars-1]

print(printer)