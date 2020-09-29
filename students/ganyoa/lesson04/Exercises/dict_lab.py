print('dictionaries01')
print('original dictionary:')
dict_01 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'chocolate'}
print(dict_01)

dict_01.pop('cake')
print('\n''cake removed:')
print(dict_01)

dict_01.setdefault('fruit', 'Mango')
print('\n''fruit, Mango added:')
print(dict_01)

print('\n''dictionary keys:')
for key in dict_01.keys():
    print(key)

print('\n''dictionary values:')
for value in dict_01.values():
    print(value)

print('\n''check if "cake" is a key:')
print('cake' in dict_01.keys())

print('\n''check if "Mango" is a value:')
print('Mango' in dict_01.values())

print('\n''dictionaries02')
print('original dictionary:')
dict_01 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'chocolate'}
print(dict_01)

dict_02 = {}
for key, value in dict_01.items():
    dict_02.update({key: value.lower().count('t')})
print(dict_02)

print('\n''Sets01')
s2 = set()
s3 = set()
s4 = set()

for i in range(1,21):
    if i % 2 == 0:
        s2.add(i)
    if i % 3 == 0:
        s3.add(i)
    if i % 4 == 0:
        s4.add(i)

print('s2:', s2)
print('s3:', s3)
print('s4:', s4)

print('\n''is s3 a subset of s2?')
print(s3.issubset(s2))
print('is s4 a subset of s2?')
print(s4.issubset(s2))


print('\n''Sets02')
#create a set with the letters in ‘Python’ and add ‘i’ to the set
x = {"P","y", "t", "h", "o", "n"}
x.add('i')
print(x)

#create a frozenset with the letters in ‘marathon’
fs = frozenset({'m', 'a', 'r', 'a', 't', 'h', 'o', 'n'})

print('x and fs union:', x.union(fs))
print('x and fs intersection:', x.intersection(fs))
