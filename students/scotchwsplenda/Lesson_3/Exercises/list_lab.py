#!/usr/bin/env python3

print('-------------------Series 1-------------------')

'''Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.'''
dbase = ["Apples", "Pears", "Oranges", "Peaches"]

'''Display the list (plain old print() is fine…).'''
print(dbase)

'''Ask the user for another fruit and add it to the end of the list.'''
dbase.append(input("Add a fruit: "))

'''Display the list.'''
print(dbase)

'''Ask the user for a number and display the number back to the user and the
fruit corresponding to that number (on a 1-is-first basis). Remember that
Python uses zero-based indexing, so you will need to correct.'''
x = int(input(f"give me a number between 1 and {len(dbase)}: "))-1
print(dbase[x])

'''Add another fruit to the beginning of the list using “+” and display the
 list.'''
dbase = [input("Add a fruit: ")] + dbase
print(dbase)

'''Add another fruit to the beginning of the list using insert() and display
 the list.'''

xx = input("Add a fruit: ")
dbase.insert(0, xx)
print(dbase)

'''Display all the fruits that begin with “P”, using a for loop.'''
for pp in dbase:
    if pp[0].upper() == 'P':
        print(pp)

print('-------------------Series 2-------------------')

'''Display the list.'''
print(dbase)

'''Remove the last fruit from the list.'''
dbase.pop()

'''Display the list.'''
print(dbase)

'''Ask the user for a fruit to delete, find it and delete it.'''
deli = input('Give me a fruit to delete: ')
dbase.remove(deli)

print('-------------------Series 3-------------------')

'''Ask the user for input displaying a line like “Do you like apples?” for each
 fruit in the list (making the fruit all lowercase).'''

HatedFruit = []

for fruit in dbase:
    dele = input('do you hate {} ? Y/N: '.format(fruit))
    if dele.upper() == 'Y':
        HatedFruit.append(fruit)
        continue
    if dele.upper() == 'N':
        continue
    else:
        print('Follow directions')

print(HatedFruit)

'''For each “no”, delete that fruit from the list.'''

dbase = [x for x in dbase if x not in HatedFruit]
print(dbase)

'''Display the list.'''
print(dbase)

print('-------------------Series 4-------------------')

'''Make a new list with the contents of the original, but with all the letters
 in each item reversed.'''
bb = []
for ff in dbase:
    ff = ff[::-1]
    bb.append(ff)

'''Delete the last item of the original list. Display the original list and the
 copy.'''
dbase.pop()
print(dbase)
print(bb)
print('Press any key to exit')
input()
