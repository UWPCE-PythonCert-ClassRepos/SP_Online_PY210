#!/usr/bin/env python

# Series 1
# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
# Display the list (plain old print() is fine…).
# Ask the user for another fruit and add it to the end of the list.
# Display the list.
# Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
# Add another fruit to the beginning of the list using “+” and display the list.
# Add another fruit to the beginning of the list using insert() and display the list.
# Display all the fruits that begin with “P”, using a for loop.

fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]

print(fruit_list)

response = input("add another fruit > ")

fruit_list.append(response.capitalize())

print(fruit_list)

two_fruit = int(input("pick a number > "))

print(fruit_list[(two_fruit - 1)])

prepend_fruit = input("prepend a fruit > ")

fruit_list.insert(0, prepend_fruit.capitalize())

print(fruit_list)

for item in fruit_list:
   if item[0] == "P":
      print(item)

# Series 2
# Using the list created in series 1 above:
# Display the list.
# Remove the last fruit from the list.
# Display the list.
# Ask the user for a fruit to delete, find it and delete it.
# (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
fruit_list.pop(-1)
print(fruit_list)
print(fruit_list)
fruit_list = fruit_list * 2
delete_fruit = input("search and destroy a fruit > ").capitalize()
delete_fruit.capitalize()
while delete_fruit not in fruit_list:
  delete_fruit = input("Select a different fruit > ")
fruit_list.remove(delete_fruit)
while delete_fruit in fruit_list:
    fruit_list.remove(delete_fruit)
print(fruit_list)

# Series 3
# Again, using the list from series 1:
# Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
# For each “no”, delete that fruit from the list.
# For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
# Display the list.

for item in fruit_list:
    like_fruit = input("Do you like " + item + "? ").lower()
    if like_fruit == "no":
        while item in fruit_list:
            fruit_list.remove(item)
    elif like_fruit == "yes":
        continue
    else:
        print("enter a damn yes or no")
print(fruit_list)

# Series 4
# Once more, using the list from series 1:
# Make a copy of the list and reverse the letters in each fruit in the copy.
# Delete the last item of the original list. Display the original list and the copy.

new_fruits = [x[::-1] for x in fruit_list]

print(new_fruits)
new_fruits.pop()

print(fruit_list)
print(new_fruits)
