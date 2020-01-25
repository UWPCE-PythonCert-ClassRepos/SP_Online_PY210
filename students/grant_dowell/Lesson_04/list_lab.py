#!/usr/bin/env python3
"""
Grant Dowell
Excercise 3.2 - List Lab
"""

# ---- Series 1 ----

# Create and show a list of fruit
fruit_list = ['Apples','Pears','Oranges','Peaches']
print(fruit_list)

# Ask the user for a fruit and add it to the end of the list
new_fruit = input("Fruit to add to list: ")
fruit_list.append(new_fruit)
print(fruit_list)

# Ask the user for a number and display the number and corresponding fruit
ask_num = input("Enter the item number you would like to see: ")
print(ask_num + ': ' + fruit_list[int(ask_num)])

# Add to the beginning of the list using '+'
new_fruit_2 = input("Another Fruit to add to the list: ")
fruit_list = [new_fruit_2] + fruit_list
print(fruit_list)

# Add to the beginning of list using 'insert()'
new_fruit_3 = input("Another Fruit to add to the list: ")
fruit_list.insert(0, new_fruit_3)
print(fruit_list)

# Display all the fruits that begin with "P", using a loop
print('\nDisplaying all fruits that start with "P":')
for item in fruit_list:
    if item[0] == 'P' or item[0] == 'p':
        print(item)
        
# ---- Series 2 ----

# Display the list from above, then remove the last item and display it again
fruit_list2 = fruit_list[:]
print(fruit_list2)
fruit_list2.pop()
print(fruit_list2)

# Ask the user for a fruit to delete, find it and delete it
fruit_for_del = input('Input a fruit to delete from the list:')
if fruit_for_del in fruit_list:
    fruit_list2.remove(fruit_for_del)
else:
    print("That's not in the list!")
    
print(f"Here's the final list: {fruit_list2}")


# ---- Series 3 ----
    
fruit_list3 = fruit_list[:]
# Ask the user for input about each item in the list and delete if necessary
for fruit in fruit_list3[:]:
    while True:
        user_pref = input(f"Do you like {fruit.lower()}? (yes/no): ")
        if user_pref == 'yes':
            break
        elif user_pref == 'no':
            fruit_list3.remove(fruit)
            break
        else:
            continue
print(f"Here's the final list: {fruit_list3}")

# ---- Series 4 ----
# Copy the list with the letters reversed, delete the last item, display
fruit_list4 = []
for fruit in fruit_list:
    fruit_list4.append(fruit[::-1])
    
fruit_list4.pop()
print(f"Here's the original list: {fruit_list}")
print(f"Here's the modified list: {fruit_list4}")

    
    
