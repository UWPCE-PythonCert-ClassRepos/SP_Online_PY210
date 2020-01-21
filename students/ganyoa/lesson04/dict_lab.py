#dictionaries01
print('original dictionary:')
cake_dict = {'name': 'Chris', 'city': 'Seattle', 'cake': 'chololate'}
print(cake_dict)

cake_dict.pop('cake')
print('\n''cake removed:')
print(cake_dict)

cake_dict.setdefault('fruit', 'Mango')
print('\n''fruit, Mango added:')
print(cake_dict)

print('\n''dictionary keys:')
for key in cake_dict.keys():
    print(key)

print('\n''dictionary values:')
for value in cake_dict.values():
    print(value)

print('\n''check if "cake" is a key:')
print('cake' in cake_dict.keys())

print('\n''check if "Mango" is a value:')
print('Mango' in cake_dict.values())