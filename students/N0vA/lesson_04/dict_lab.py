#!/usr/bin/env python3

# Make dictionary as provide
dict_1 = dict(name='Chris', city='Seattle', cake='chocolate')
print(dict_1)

# Delete cake entry
dict_1.pop('cake')
print(dict_1)

# Add fruit -- Mango
dict_1['fruit'] = 'Mango'
print(dict_1)

# Display dictionary keys
print(dict_1.keys())

# Print dictionary values
print(dict_1.values())

# Display of cake is a key key in the dictionary
'cake' in dict_1

# Display whether Mango is a value in the dictionary
'Mango' in dict_1.values()

# Create a dictionary from dict_1 based on 't's in each value
dict_2 = dict(name='Chris', city='Seattle', cake='chocolate')

for k,v in dict_2.items():
    dict_2[k] = v.count('t')

print(dict_2)


# Sets - s2, s3, s4 of numbers from 0-20 divisible by that number
s2 = set()
s3 = set()
s4 = set()

for i in range(21):
    if i % 2 == 0:
        s2.add(i)
    if i % 3 == 0:
        s3.add(i)
    if i % 4 == 0:
        s4.add(i)

print(s2)
print(s3)
print(s4)
print(s3.issubset(s2))
print(s4.issubset(s2))

# Make set with letters from 'Python' and add 'i' to it

p = {'P', 'y', 't', 'h', 'o', 'n'}
p.add('i')
print(p)

# Create frozenset with 'marathon'
m = frozenset({'m', 'a', 'r', 'a', 't', 'h', 'o', 'n'})

union = p.union(m)
print(union)
inter = p.intersection(m)


