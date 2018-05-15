D = {'food' : "mielonka", 'quantity' : 4, 'color' : 'pink'}
print(D['food'])
D['quantity'] += 1
print(D['quantity'])
print(D)

bob = dict(zip(['name', 'age', 'job'],['bob', 43, 'it']))
print(bob)

rec = {'name': {'first' : 'Bob', "Last" : 'Mostowski'}, 'jobs': ['dev', 'mgr'], 'age': 40}
print(rec)