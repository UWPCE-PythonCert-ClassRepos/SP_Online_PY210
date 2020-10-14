#! /usr/bin/env python3

### Dict and Set Practice, Lesson 4
### By: B. Matthews
### 10/12/2020

labstuff = {
    'name': 'Chris',
    'city': 'Seattle',
    'cake': 'Chocolate'
}

print(labstuff)

for key in labstuff.keys():
    print(key, labstuff[key])

del labstuff['cake']            ## remove an entry

for key in labstuff.keys():
    print(key, labstuff[key])

labstuff['fruit'] = 'Mango'     ## add new entry

for key in labstuff.keys():
    print(key, labstuff[key])

print('cake' in labstuff)

for key in labstuff:
    if (labstuff[key] == 'Mango'):
        print('fruit found')

    x = labstuff[key].count('t')
    labstuff[key] = x

for key in labstuff:
    print(key, labstuff[key])

print(labstuff)

my_stuff = labstuff.values()
print(my_stuff)

## set lab exercises

s2 = {0}
s3 = {0}
s4 = {0}

i = 1
while (i < 21):
    if (i % 2 == 0):
        s2.add(i)
    if (i % 3 == 0):
        s3.add(i)
    if (i % 4 == 0):
        s4.add(i)
    i = i + 1

print("Is s3 in s2?", s3.issubset(s2))
print("Is s4 in s2?", s4.issubset(s2))

print(s2)
print(s3)
print(s4)

myset = {'p', 'y', 't', 'h', 'o', 'n'}
myset.add('i')
print(myset)

something = ("m", "a", "r", "t", "h", "o", "n")
fset = frozenset(something)
print(fset)

print("union is: ", myset.union(fset), "intersection is: ", myset.intersection(fset))








