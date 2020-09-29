#! python

#----------------------------------------------
# Lesson 3 - Exercise 3.2: List Lab
#----------------------------------------------

# Series 1
#	Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
#	Display the list (plain old print() is fine…).
#	Ask the user for another fruit and add it to the end of the list.
#	Display the list.
#	Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
#	Add another fruit to the beginning of the list using “+” and display the list.
#	Add another fruit to the beginning of the list using insert() and display the list.
#	Display all the fruits that begin with “P”, using a for loop.

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)
response = input("Please enter a fruit: > ")
fruits.append(response)                      # add new fruit to the end
print(fruits)
response = input("Please enter a number: > ")
print("Number "+response+" is "+fruits[int(response) - 1])
fruits = ["Lemons"] + fruits
print(fruits)
fruits.insert(0, "Watermelons")
print(fruits)
for name in (fruits):
    if name[0] == 'P':
        print(name)

#Series 2
#Using the list created in series 1 above:
#	Display the list.
#	Remove the last fruit from the list.
#	Display the list.
#	Ask the user for a fruit to delete, find it and delete it.
#	(Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)

print(fruits)
del fruits[-1]
print(fruits)
response = input("Please enter a fruit to delete: > ")
if fruits.count(response):
    fruits.remove(response)
## Bonus:
fruits *= 2
print(fruits)
fruit_found = False
while not fruit_found:
    response = input("Please enter a fruit to delete: > ")
    if fruits.count(response):
        fruit_found = True
        count = fruits.count(response)
        for i in range(count):
            fruits.remove(response)
print(fruits)

#Series 3
#Using the list from series 1:
#	Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
#	For each “no”, delete that fruit from the list.
#	For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
#	Display the list.

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)
i = 0
while i < len(fruits):
    response = input("Do you like {}? > ".format(fruits[i].lower()))
    while not response in ("yes", "no"):
        response = input("Please answer with 'yes' or 'no' > ")
    if response == "no":
        del fruits[i]
    else:
        i += 1
print(fruits)

#series 4
#Using the list from series 1:
#	Make a new list with the contents of the original, but with all the letters in each item reversed.
#	Delete the last item of the original list. Display the original list and the copy.

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
new_list = fruits
for i in range(len(new_list)):
    new_list[i] = new_list[i][::-1]
del fruits[-1]
print(fruits)
print(new_list)
