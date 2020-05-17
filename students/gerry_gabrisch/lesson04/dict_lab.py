#!/usr/bin/env python3
#'''dict_lab.py for lesson04 by Gerry Gabrisch.  Started 4/2/2020'''

###   Dictionaries 1

whos_food = {'name':'Chris', 'city':'Seattle', 'cake':'Chocolate'}
print(whos_food)
#Deleteting the key also deletes the key's value...
del whos_food['cake']
print(whos_food)
#Add a new key with the value Mango to the dictionary
whos_food['fruit'] = 'Mango'
print(whos_food)
#Print all the keys...
print(whos_food.keys())
#Print the values...
print(whos_food.values())
if 'cake'  in whos_food:
    print('cake is in the dictionary')
else:
    print('cake is not a key in the dictionary')
    
if 'fruit' in whos_food:
    if whos_food['fruit'] =='Mango':
        print('Mango is a value in the dictionary')


###   Dictionaries 2

	
import copy
#Use deepcopy to make a new and free version of the dictionary...
tCount = copy.deepcopy(whos_food)
#Get all the keys one at a time...
for key in tCount.keys():
	#Get the values at this key, count the ts and Ts...add this to a new dictionary...
	x = {key: tCount[key].count('t') + tCount[key].count('T')}
	#Use the dictionary update method to update the dictionary with the t counts and not the original values...
	tCount.update(x)
print(tCount)

###   Sets...

#Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4...
def set_creator_20(divisor):
	'''makes a set with values between 0 and 20 but only with
	   values that are divisible by the divisor...'''
	#Make an empty set to store the set values...
	values = set()
	count = 0
	while count <=20:
		if count %  divisor == 0:
			values.add(count)
		count += 1
	return values

s2 = set_creator_20(2)
s3 = set_creator_20(3)
s4 = set_creator_20(4)
print('s2 = ',s2)
print('s3 = ',s3)
print('s4 = ',s4)

#Check to see if S3 is a subset of s2...
if s3 <= s2:
	print('s3 is a subset of s2')
else:
	print('s3 is not a subset of s2')
#Check to see if s4 is a subset of s2...	
if s4 <= s2:
	print('s4 is a subset of s2')
else:
	print('s4 is not a subset of s2')
	
###    Sets2
#Create and empty set...	
pyset = set()
#Iterate the word and add each unique letter to the set...
for i in 'Python':
	pyset.add(i)
print(pyset)
#Add an i to the set...
pyset.add('i')
print(pyset)

frozen_marathon = set()
for i in 'marathon':
	frozen_marathon.add(i)
#Make the set immutable by freezing it...	
frozen_marathon = frozenset(frozen_marathon)
print(frozen_marathon)
print('set union example = ', pyset | frozen_marathon)
print('set intersection example = ', pyset & frozen_marathon)