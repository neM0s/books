# Type your code here

def palindrome(string1):
    new_string = string1.lower()
    last = -1
    palidrom = True
    for i in range(0,len(new_string)-1):
        if new_string[i] != new_string[last]:
            palidrom = False
        last = last - 1
    return palidrom

print(palindrome("Radar"))