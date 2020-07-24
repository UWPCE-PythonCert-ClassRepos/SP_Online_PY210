#!/usr/bin/env python3

#Christine Kim

#Series 1
print("Series 1")
print()
#Create and display a list of fruits
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits)

#Request input from user for list addition
fruits.append(input("Input a fruit to add to the list: "))
print(fruits)

#Request input from user for a number and display the number and corresponding fruit
fruit_num = int(input("Input a number for a fruit to display: "))
print(str(fruit_num) + ": " + fruits[(fruit_num - 1)])

#Add to the beginning of the list with '+'
fruits = [input("Input a fruit to add to the beginning of the list: ")] + fruits
print(fruits)

#Add to the beginning of the list with 'insert()'
fruits.insert(0, input("Input a fruit to add to the beginning of the list: "))
print(fruits)

#Use a for loop to display all fruits beginning with "P"
print("Displaying all fruits which starts with a 'P': ")
for item in fruits:
    if item[0] == "P" or item[0] == "p":
        print(item)

#Series 2
print()
print("Series 2")
print()

#Display list
fruits2 = fruits[:]
print(fruits2)

#Remove the last item on the list and display
fruits2.pop()
print(fruits2)

#Request input for fruit to delete
del_fruit = input("Input a fruit to remove from the list: ")
if del_fruit in fruits2:
    fruits2.remove(del_fruit.)
else:
    print("Entry not found.")

#Display updated list
print(fruits2)

#Series 3
print()
print("Series 3")
print()

#Use list from Series 1
fruits3 = fruits[:]
print(fruits3)

#Perform action for every item in the list
sadfruits = []
for item in fruits3:
    while True:
        #Request user prefrence input
        answer = input("Do you like " + item.lower() + "? ")
        #Next
        if answer == "yes":
            break
        #mark disliked fruits
        elif answer == "no":
            sadfruits.append(item)
            break
        #prompt user for proper entry
        else:
            print("Please respond in either 'yes' or 'no'")

#Remove disliked fruits
for fruit in sadfruits:
    fruits3.remove(fruit)
            
#Display updated list
print(fruits3)

#Series 4
print()
print("Series 4")
print()

#New list with contents of the original reversed
fruits4 = []
for item in fruits:
    item = item[::-1]
    fruits4.append(item)

#Delete last item of the original list
fruits4.pop()

#Display original list and the copy
print(fruits)
print(fruits4)