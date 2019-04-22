#!/usr/bin/env python3

# Ins and outs of Python Lists

# Series 1

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

# Save copy of original list for future series
original_fruits = fruits[:]

# Series 2

# Display current list of fruits
print('Current list of fruits:',fruits)

# Remove last fruit from list
print('Removing last fruit from list')
fruits.pop()
print('New list of fruits:',fruits)

# Remove a fruit by request
to_remove = input('Name a fruit to remove from the list > ')
if fruits.count(to_remove) > 0: # Make sure fruit exists (error will occur if it doesn't)
    location = fruits.index(to_remove) # Find index of fruit
    # Display fruit and remove from list
    print('{} found at location {:d}. Removing from list.'.format(to_remove,location+1))
    fruits.remove(to_remove)
else:
    print('{} not in list of fruits.'.format(to_remove))
# Display current list of fruits
print('New list of fruits:',fruits)

# Bonus: Multiply list by two and remove all instances of a fruit
double_fruits = fruits*2
print('Long list of fruits: ',double_fruits)
to_remove = input('Name a fruit to remove from this list > ')
while double_fruits.count(to_remove) > 0: # Repeat process until all instances have been removed.
    location = double_fruits.index(to_remove) # Find index of fruit
    # Display fruit and remove from list
    print('{} found at location {:d}. Removing from list.'.format(to_remove,location+1))
    double_fruits.remove(to_remove)
# Display current list of fruits
print('New long list of fruits:',double_fruits)
