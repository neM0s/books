name = raw_input("Name: ")
choice = raw_input("Phone number (p) or address (a): ")


people = {
    'Alice': {
        'phone': '23213',
        'addr': 'somewhere'
    },
    'Beth': {
        'phone': '342',
        'addr': "galaxy"
    }
}

labels = {
    'phone': 'phone number',
    'addr': 'address'
}
key = choice
if choice == 'p': key = 'phone'
if choice == 'a': key = 'addr'

person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')

print("%s's %s is %s." % (name, label, result))