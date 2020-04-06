##!/usr/bin/env python3
#'''dict_lab.py for lesson04 by Gerry Gabrisch.  Started 4/2/2020'''

###   Dictionaries 1

whosFood = {'name':'Chris', 'city':'Seattle', 'cake':'Chocolate'}
print(whosFood)
#deleteting the key also deletes the keys value...
del whosFood['cake']
print(whosFood)
#add a new key with the value Mango to the dictionary
whosFood['fruit'] = 'Mango'
print(whosFood)
#print all the keys...
print(whosFood.keys())
#print the values...
print(whosFood.values())
if 'cake'  in whosFood:
    print('cake is in the dictionary')
else:
    print('cake is not a key in the dictionary')
    
if 'fruit' in whosFood:
    if whosFood['fruit'] =='Mango':
        print('Mango is a value in the dictionary')


###   Dictionaries 2

	
import copy
#use deepcopy to make a new and free version of the dictionary
tCount = copy.deepcopy(whosFood)
#Get all the keys one at a time...
for key in tCount.keys():
	#get the values at this key, count the ts and Ts...add this to a new dictionary
	x = {key: tCount[key].count('t') + tCount[key].count('T')}
	#use the dictionary update method to update the dictionary with the t counts and not the original values...
	tCount.update(x)
print(tCount)

###   Sets...

#Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4
def SetCreator20(divisor):
	'''makes a set with values between 0 and 20 but only with
	   values that are divisible by the divisor...'''
	#make an empty set to store the set values...
	values = set()
	count = 0
	while count <=20:
		if count %  divisor == 0:
			values.add(count)
		count += 1
	return values

s2 = SetCreator20(2)
s3 = SetCreator20(3)
s4 = SetCreator20(4)
print('s2 = ',s2)
print('s3 = ',s3)
print('s4 = ',s4)

if s3 <= s2:
	print('s3 is a subset of s2')
else:
	print('s3 is not a subset of s2')
	
if s4 <= s2:
	print('s4 is a subset of s2')
else:
	print('s4 is not a subset of s2')
	
###    Sets2
pyset = set()
for i in 'Python':
	pyset.add(i)
print(pyset)
pyset.add('i')
print(pyset)

frozenMarathon = []
for i in 'marathon':
	frozenMarathon.append(i)
frozenMarathon = frozenset(frozenMarathon)
print(frozenMarathon)
print('set union example = ', pyset | frozenMarathon)
print('set intersection example = ', pyset & frozenMarathon)