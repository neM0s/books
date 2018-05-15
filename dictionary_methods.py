from copy import deepcopy
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}

#y = deepcopy(x)
y = x.copy()
y['username'] = 'mlh'
y['machines'].remove('bar')
print(y.get('example', "user don't exist in database"))
print(x)

y.setdefault('example', 'value')
print(y)
y['name'] = "mlh"
print(y)
print(y.items())
print(y.keys())