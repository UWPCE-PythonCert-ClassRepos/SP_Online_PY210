#!/usr/bin/env python3

"""Series 1: Add fruits to a list using different methods."""
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]

print(fruit_list)

add_fruit = input("Please enter a fruit of your choosing. ")

fruit_list.append(add_fruit)

print(fruit_list)

num_response = input("Enter a number. ")

print(fruit_list[int(num_response) - 1])

list2 = []

next_fruit = input("Pick another fruit. ")

list2.append(next_fruit)

fruit_list = list2 + fruit_list

print(fruit_list)

another_fruit = input("One more fruit, please. ")

fruit_list.insert(0, another_fruit)

print(fruit_list)

for fruit in fruit_list[:]:
    if fruit[0] == 'P' or fruit[0] == 'p':
        print(fruit)

"""Series 2: Use the list from Series 1 and remove fruits from it using various methods."""
f = fruit_list[:]

print(f)

f.pop(-1)

print(f)
    
fruit_removal = input("Which fruit would you like to remove? ")

f.remove(fruit_removal)

f = f[:] * 2

fruit_removal2 = input("Choose another fruit to remove. ")

while fruit_removal2 not in f:
    print("Oops! That's not in the list. Try again!")
    fruit_removal2 = input("Choose another fruit to remove. ")
else:
    while fruit_removal2 in f:
        f.remove(fruit_removal2)

"""Series 3: Keep or remove fruits from the list in Series 1 based on the user's preference."""
f = fruit_list[:]

for fruit in f[:]:
    preference = input("Do you like {}? ".format(fruit.lower()))
    
    while preference != 'yes' and preference != 'no':
        preference = input("Please answer with yes or no. ")
        
    if preference == 'no':
        f.remove(fruit)

print(f)
 
"""Series 4: Reverse the items of the list from Series 1. Remove the last item of the original list."""
reverse_fruits = []

for fruit in fruit_list[:]:
    reverse_fruits.append(fruit[::-1])

fruit_list.pop(-1)

print(fruit_list)
print(reverse_fruits)