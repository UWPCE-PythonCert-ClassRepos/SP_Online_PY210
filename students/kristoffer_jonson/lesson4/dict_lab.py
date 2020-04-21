#!/usr/bin/env python3

#Dictionaries 1
cake_dict = {'name' : 'Chris','city': 'Seattle','cake':'Chocolate'}
print(cake_dict)

# Delete the entry for “cake”.
cake_dict.pop('cake')
print(cake_dict)

# Add an entry for “fruit” with “Mango” and display the dictionary.
cake_dict['fruit'] = 'Mango'
print(cake_dict)

# Display the dictionary keys.
# Display the dictionary values.
for i,j in cake_dict.items():
    print(i,j)

# Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
# Display whether or not “Mango” is a value in the dictionary (i.e. True).
print('Is cake in the dictionary?')
print('cake' in cake_dict)

print('Is Mango a value in the dictionary?')
print('Mango' in cake_dict.values())

#Dictionaries 2
cake_dict = {'name' : 'Chris','city': 'Seattle','cake':'Chocolate'}
cake_ts = cake_dict.copy()
for i,j in cake_dict.items():
    # count = 0
    # for k in j.lower():
    #     if k == 't':
    #         count = count + 1
    cake_ts[i]  = j.lower().count('t')

print(cake_ts)

#Sets
# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4 (figure out a way to compute those – don’t just type them in).
# Display the sets.
# Display if s3 is a subset of s2 (False)
# and if s4 is a subset of s2 (True).
s2 = set()
s3 = set()
s4 = set()
s2_list = []
s3_list = []
s4_list = []
for i in range(21):
    if i%2 == 0:
        s2_list.append(i)
    if i%3 == 0:
        s3_list.append(i)
    if i%4 == 0:
        s4_list.append(i)
s2.update(s2_list)
s3.update(s3_list)
s4.update(s4_list)
print(s2)
print(s3)
print(s4)

#Sets2
# Create a set with the letters in ‘Python’ and add ‘i’ to the set.
s_python = set(['p','y','t','h','o','n'])
s_python_list = list(s_python) + ['i']
s_python.update(s_python_list)
print(s_python)

# Create a frozenset with the letters in ‘marathon’.
f_marathon = (('m','a','r','a','t','h','o','n'))

# Display the union and intersection of the two sets.
print('Union of pythoni and marathon')
print(s_python.union(f_marathon))

print('Intersection of pythoni and marathon')
print(s_python.union(f_marathon))
