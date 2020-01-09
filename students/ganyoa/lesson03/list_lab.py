#series 1 assignment

#create a list of fruit and print the list
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit_list)

#present the user an option to input an additional fruit to the end of the list
response = input("What fruit would you like to add? > ")
fruit_list.append(response)
print(fruit_list)

#have the user select one fruit based on their numbered location
fruit_location = int(input("Enter the cooresponding number for one fruit > "))
print(fruit_list[fruit_location - 1])

#add 'Bananas to the beinging of the list'
fruit_list = ["Bananas"] + fruit_list
print(fruit_list)

#insert 'Plums' to the begining of the list
fruit_list.insert(0, "Plums")
print(fruit_list)

#loop through the complete list and display fruits that begin with 'P'
for i in fruit_list:
    if i[0] == "P":
        print(i)

#series 2 assignment
print(fruit_list)

#remove the last fruit from the list
del(fruit_list[-1])
print(fruit_list)

#user enters fruit to be removed from list
remove_fruit = input("Which fruit would you like to remove? > ")
if remove_fruit in fruit_list:
    fruit_list.remove(remove_fruit)
    print(fruit_list)

#bonus
fruit_list_bonus = fruit_list[:] * 2
print(fruit_list_bonus)
remove_fruit = input("Which fruit would you like to remove? > ")

#loop until user enters a fruit in the list
while remove_fruit not in fruit_list_bonus:
    remove_fruit = input("Fruit not found, enter a different option > ")

#loops through fruit list to remove the fruit entered above
last_fruit = len(fruit_list_bonus)
i = 0
while i < last_fruit:
    if fruit_list_bonus[i] == remove_fruit:
        del(fruit_list_bonus[i])
        last_fruit -= 1
    i += 1
print(fruit_list_bonus)

#series 3 assignmet
for fruit in fruit_list[:]:
    answer = input("Do you like " + fruit.lower() + " ? (yes or no) >" + "\n")
    while not (answer == "yes" or answer == "no"):
        print("Please answer with 'yes' or 'no'")
        answer = input("  Do you like " + fruit.lower() + " ? (yes or no) >"+ "\n")
    if answer == "no":
        fruit_list.remove(fruit)
    if len(fruit_list) == 0:
        fruit_list = "you don't like these fruits"
print(fruit_list)