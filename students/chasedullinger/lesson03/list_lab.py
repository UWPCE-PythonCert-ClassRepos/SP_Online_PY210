#!/usr/bin/env python3

### Series 1 ###

#Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
list_of_fruit = ["Apples","Pears","Oranges", "Peaches"]

#Display the list (plain old print() is fine…).
print(list_of_fruit)

# Ask the user for another fruit and add it to the end of the list.
response = input("Enter a new item for the list > ")
list_of_fruit.append(response)

#Display the list.
print(list_of_fruit)

# Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
display_number_string = input("Enter number of item to display >")

display_number = int(display_number_string) #convert string to int for indexing

if display_number < 1 or display_number > len(list_of_fruit):
    print("The number entered is out of range for the list")
else:
    print(list_of_fruit[display_number-1])

# Add another fruit to the beginning of the list using “+” and display the list.
list_of_fruit = ["Grapes"] + list_of_fruit
print(list_of_fruit)

# Add another fruit to the beginning of the list using insert() and display the list.
list_of_fruit.insert(0, "Pineapple")
print(list_of_fruit)

# Display all the fruits that begin with “P”, using a for loop.
for fruit in list_of_fruit:
    if fruit.startswith("P"):
        print(fruit)

### Series 2 ###

# Display the list.
print(list_of_fruit)
# Remove the last fruit from the list.
list_of_fruit.pop()
# Display the list.
print(list_of_fruit)
# Ask the user for a fruit to delete, find it and delete it.
response = input("Enter an item in the list to remove > ")
list_of_fruit.remove(response)
print(list_of_fruit)


# (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
double_list_of_fruit = list_of_fruit * 2
print(double_list_of_fruit)
found_item = False
while not found_item:
    response = input("Enter an item in the list to remove >")
    if response not in double_list_of_fruit:
        continue
    else:
        while response in double_list_of_fruit:
                double_list_of_fruit.remove(response)
        found_item = True
print(double_list_of_fruit)


### Series 3 ###
# Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
print(list_of_fruit)
duplicate_list_of_fruit = list_of_fruit[::] # need to iterate over a copy of the list to avoid removing the wrong item
for fruit in duplicate_list_of_fruit:
    print(fruit)
    acceptable_response=False
    while not acceptable_response:
        response = input("Do you like {}? >".format(fruit.lower()))
# For each “no”, delete that fruit from the list.
        if response == "no":
            list_of_fruit.remove(fruit)
# For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
        if response == "yes" or response == "no":
            acceptable_response = True

# Display the list.
print(list_of_fruit)

### Series 4 ###
# Make a new list with the contents of the original, but with all the letters in each item reversed.
new_list_of_fruit = []
for fruit in list_of_fruit:
    new_list_of_fruit.append(fruit[::-1])

# Delete the last item of the original list. Display the original list and the copy.
list_of_fruit.pop()
print(list_of_fruit)
print(new_list_of_fruit)
