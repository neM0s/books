database = [
    ['albert', '1234'],
    ['wiotek', '1234']
]

username = raw_input("username: ")
pin = raw_input("pin: ")

if [username, pin] in database: print "Access granted"