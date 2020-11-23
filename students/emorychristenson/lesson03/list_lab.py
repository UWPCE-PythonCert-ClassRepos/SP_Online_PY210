#!/usr/bin/env python3

def new_fruit():
    # Takes input from user, ensures input doesn't already exist in list
    new_fruit = input("Please add another fruit: ")
    while new_fruit in fruits:
        new_fruit = input("That fruit is already in the list, please choose another: ")
    return new_fruit


# Series 1
# Create list of fruits
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)

# Add a new fruit to the list using append method
add_fruit = new_fruit()
fruits.append(add_fruit)
print(fruits)

# Prompt user for a number, removes that item from the fruit list
number = int(input("Please pick a number from 1 to 5: "))
while number < 0 or number > 5:
    number = int(input("Number is out of range, please choose another number: "))    
fnumber = number - 1
print(f"You chose {number}, which is {fruits[fnumber]}.")

# Add a new fruit to the list using + method
add_fruit = new_fruit()
fruits = [add_fruit] + fruits
print(fruits)

# Add a new fruit list using insert method
add_fruit = new_fruit()
fruits.insert(0, add_fruit)
print(fruits)

# Print all fruits that start with P
print("The fruits that start with 'P' are:")
for fruit in fruits:
    if "P" in fruit[0]:
        print(fruit)

# Series 2
print("\nStarting Series 2!\n\n")

# Copy list from Series 1 and display
s2_copy = fruits.copy()
print(s2_copy)

# Remove last fruit from the list, print remaining list
print("Removing last fruit from the list...")
del s2_copy[-1]
print("Remaining fruit list:")
print(s2_copy)

# Choose a fruit to delete from the list, ensures item exists in list
delete_fruit = input("Please choose a fruit to delete: ")
while delete_fruit not in s2_copy:
   delete_fruit = input("That fruit is not in the list, please choose another: ")
print(f"Removing {delete_fruit}...")
s2_copy.remove(delete_fruit)

# Series 3
print("\nStarting Series 3!\n\n")

# Copy fruit list from Series 1
s3_copy = fruits.copy()
liked_fruits = []
print(s3_copy)
# Loop that asks if user likes fruit in list, remove fruits they respond 'no' to
for fruit in s3_copy:
    answer = input(f"Do you like {fruit.lower()}? ")
    while answer.lower() not in ['yes','no']:
        answer = input(f"Do you like {fruit.lower()}? Please answer yes or no. ")
    if answer.lower() == "yes":
        liked_fruits += [fruit]
# Is there a way to do this via removing items from the list while iterating? Every attempt at using 'fruits.remove'
# returned wonky results.

print(f"You like these fruits: {liked_fruits}")

# Series 4
print("\nStarting Series 4!\n\n")

# Copy fruit list from Series 1
s4_copy = fruits.copy()

# Reverse letters in copy
reverse_copy = []
for fruit in s4_copy:
    reverse_copy.append(fruit[::-1])

# Remove last item in original list
del fruits[-1]

# Display both lists
print(f"{fruits}\n {reverse_copy}")
    