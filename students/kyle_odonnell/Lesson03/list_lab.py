#!/usr/bin/env python3

# Series 1
print("********* Series 1 ************")
# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]


# Display the list
print(fruit_list)


# Ask the user for another fruit and add it to the end of the list.
new_fruit = input("What else would you like to add to your Fruit List? ")
fruit_list.append(new_fruit.title())
print(fruit_list)

# Ask the user for a number and display the number back to the user and the fruit corresponding to that number
num = int(input("Please choose an integer number "))
try:
    print(F'Item {num} is {fruit_list[num-1]}')
except IndexError:
    print("Number outside list range")


# Add another fruit to the beginning of the list using “+” and display the list
fruit_list = fruit_list + ["Blueberries"]
print("Added blueberries using concatenate:")
print(fruit_list)

# Add another fruit to the beginning of the list using insert() and display the list
fruit_list.insert(0, "Raspberries")
print("Added Raspberries using insert method:")
print(fruit_list)

print("Fruits in list that start with p: ")
for f in fruit_list:
    if f[0].lower() == "p":
        print(f)


print("********* Series 2 *********")

fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
# Display the list
print("Fruit List:")
print(fruit_list)


# Remove the last fruit from the list
del fruit_list[-1]

# Display the list
print("List with last item removed:")
print(fruit_list)


# Ask the user for a fruit to delete, find it and delete it.
remove_fruit = input("What would you like to remove? ").title()
fruit_list.remove(remove_fruit)
print("Removed {} from list:".format(remove_fruit))
print(fruit_list)


# Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
print("** Bonus **")
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"] * 2

while True:
    print("Fruit list:", fruit_list)
    fruit = input("Enter a fruit to remove from list: ").title()
    if fruit in fruit_list:
        for f in fruit_list:
            if f == fruit:
                fruit_list.remove(f)
        break
    else:
        print("Please select fruit from the list.")

print("Removed {} from list".format(fruit))
print(fruit_list)


print("********* Series 3 *********")
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
likes = []

for f in fruit_list:
    while True:
        taste = input("Do you like {}? ".format(f.lower()))
        if taste.lower() == "no":
            break
        elif taste.lower() == "yes":
            likes.append(f)
            break
        else:
            print("Please enter yes or no")

fruit_list = likes
print("New list with only liked fruit:", fruit_list)


print("********* Series 4 *********")
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
print("Original List:", fruit_list)
fruit_list_reverse = []
for f in fruit_list:
    fruit_list_reverse.append(f[::-1].title())
fruit_list.pop(-1)
print("Original List without last item", fruit_list)
print("New list with items spelled backwards:", fruit_list_reverse)