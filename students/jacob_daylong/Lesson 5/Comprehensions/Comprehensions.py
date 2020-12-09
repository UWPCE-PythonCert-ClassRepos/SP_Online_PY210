feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']
comprehension = [delicacy.capitalize() for delicacy in feast]

#Comprehension is capitalizing and returning the result for each of the items within "feast". 
#Calling "comprehension" with a specific index is applying the capitalization and returning the specific value at the index called.
print("Exercise 1")
print("Comprehension is capitalizing and returning the result for each of the items within 'feast'.")
print("Calling 'comprehension' with a specific index is applying the capitalization and \nreturning the specific value at the index called.")
print("-"*20)
print(comprehension[0])
print(comprehension[2])
print("-"*20)
print()



feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']
comp = [delicacy for delicacy in feast if len(delicacy) > 6]

#printing the qty of the items in "feast" and then those that match the filter parameter of "comp"
print("Exercise 2")
print("Printing the quantity of the items in 'feast' and then those that match the filter parameter of 'comp'.")
print("-"*20)
print(len(feast))
print(len(comp))
print("-"*20)
print()



list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]
comprehension = [ skit * number for number, skit in list_of_tuples ]

#first printing the text value asocialted with the tuple, then taking the length of the text value and multiplying it by the numerical value in the tuple. 
print("Exercise 3")
print("First printing the text value asocialted with the tuple. \nThen taking the length of the text value and multiplying it by the numerical value in the tuple.")
print("-"*20)
print(len(list_of_tuples))
print(comprehension[0])
print(len(comprehension[1]))
print("-"*20)
print()



eggs = ['poached egg', 'fried egg']
meats = ['lite spam', 'ham spam', 'fried spam']
comprehension = \
[ '{0} and {1}'.format(egg, meat) for egg in eggs for meat in meats]

#first printing the length of the comprehension as dictated by the formatting parameters. then printing an example of index 0 in the comprehension. 
print("Exercise 4")
print("First printing the length of the comprehension as dictated by the formatting parameters. \nThen printing an example of index 0 in the comprehension.")
print("-"*20)
print(len(comprehension))
print(comprehension[0])
print("-"*20)
print()



comprehension = { c for c in 'aabbbcccc'}

#Returns one of each set in no particular order
print("Exercise 5")
print("Returns one of each set in no particular order")
print("-"*20)
print(comprehension)
print("-"*20)
print()



dict_of_weapons = {'first': 'fear',
                       'second': 'surprise',
                       'third':'ruthless efficiency',
                       'forth':'fanatical devotion',
                       'fifth': None}
dict_comprehension = \
{ k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon}

print("Exercise 6")
print("Dict comprehension")
print("-"*20)
print("True/False logic. First result is true, second is false because of case mismatch of 'first' vs. 'FIRST'.")
print()
print('first' in dict_comprehension)
print('FIRST' in dict_comprehension)
print("-"*20)
print("Length of dict_of_weapons")
print()
print(len(dict_of_weapons))
print(dict_of_weapons)
print("-"*20)
print("Dict_comprehension converts dict position to uppercase and filters out any option that doesn't have a weapon. \nWhich is way option 'FIVE' is missing.")
print()
print("Length of dict_comprehension")
print()
print(len(dict_comprehension))
print(dict_comprehension)
print("-"*20)
print()