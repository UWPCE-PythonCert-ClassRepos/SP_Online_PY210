#!/usr/bin/env python3

# Ins and outs of Python Lists

# Series1

# Create and display list of fruits
fruits = ['Apples','Pears','Oranges','Peaches']
print('Current list of fruits:',fruits)

# Add a new fruit to the list and display
new_fruit = input('Pick a fruit (pun fully intended) to add to the list > ')
fruits.append(new_fruit)
print('New list of fruits:',fruits)

# Prompt for a number and display corresponding fruit
num_fruits = len(fruits)
prompt = 'Enter a number between 1 and {:d} to select a fruit > '.format(num_fruits)
while True:
    selection = int(input(prompt))
    if selection >= 1 and selection <= num_fruits:
        # Valid selection
        print('{:d} -> {}'.format(selection,fruits[selection-1]))
        break
    else:
        # Invalid selection
        print('Invalid selection, please retry.')

# Add another fruit (using +) and display
new_fruit = input('Pick another fruit to add > ')
fruits = [new_fruit] + fruits
print('New list of fruits:',fruits)

# Add one more fruit (using insert) and display
new_fruit = input('Pick one more fruit to add > ')
fruits.insert(0,new_fruit)
print('New list of fruits:',fruits)

# Display all fruits beginning with P
print('All fruits from the list that begin with \'P\':')
for fruit in fruits:
    if fruit.startswith('P'):
        print(fruit)
