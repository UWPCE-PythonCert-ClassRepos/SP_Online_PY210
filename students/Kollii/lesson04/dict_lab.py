#!/usr/bin/env python3

# Lesson 4 - DictLab

# DICTIONARY 1 

dict1 = {
    'name': 'Chris',
    'city': 'Seattle',
    'cake': 'Chocolate',
}

print(" This is original Dictionary \n")
print(dict1)

print("\nCake Element removed from Dictionary")
print(dict1.pop("cake"))

print('\n fruit = Mango added added to Dictionary')
dict1['fruit'] = 'Mango'
print(dict1)

print('\n Display the dictionary keys.')
for x in dict1:
    print(x)

print('\n Display the dictionary values.')
for x in dict1:
    print(dict1[x])


print('Is cake in the Dictionay-dict1 ?  {}'.format('cake' in dict1.keys()))

print('Is Mango in Dictionay-dict1 ?  {}'.format('Mango' in dict1.values()))

####### DICTIONARY 2 ##############

dict2 = {
    'name': 'Chris'.count('t'),
    'city': 'Seattle'.count('t'),
    'cake': 'Chocolate'.count('t'),
}

print('\n Dictionary with the number of ‘t’s in each value as the value \n ')
print(dict2)

#  SET 1

s2 = set() 
s3 = set() 
s4 = set()

for x in range(0,20):
    if x%2 == 0:
        s2.update([x])

for x in range(0,20):
    if x%3 == 0:
        s3.update([x])

for x in range(0,20):
    if x%4 == 0:
        s4.update([x])


print('\n**** SET- s2 ******')
print("s2 contains numbers from zero through twenty, divisible by 2  {} ", s2)

print('\n**** SET- s3 ******')
print("s2 contains numbers from zero through twenty, divisible by 3  {} ", s3)

print('\n**** SET- s4 ******')
print("s2 contains numbers from zero through twenty, divisible by 4  {} ", s4)

print('\nis s3 is a subset of s2 ---', s3.issubset(s2))

print('\nis s4 is a subset of s2 ---', s4.issubset(s2))

# SET 2


set_str = {'P','y','t','h','o','n'}
set_str.add('i')
set_frz = frozenset(['m','a','r','a','t','h','o','n'])

print('\n******* UNION OF set PHYTHON and frozenset MARATHON ***********')
print(set_str.union(set_frz))

print('\n******* INTERSECTION OF set PHYTHON and frozenset MARATHON ***********')
print(set_str.intersection(set_frz))



