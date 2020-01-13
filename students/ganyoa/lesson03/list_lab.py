#series 1 assignment

#create a list of fruit and print the list
print("--- Series01 ---" + "\n")
original_fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
print(original_fruit_list)

series01_list = original_fruit_list[:]
#present the user an option to input an additional fruit to the end of the list
response = input("What fruit would you like to add? > ")
series01_list.append(response)
print(series01_list)

#have the user select one fruit based on their numbered location
fruit_location = int(input("Enter the cooresponding number for one fruit > "))
print(series01_list[fruit_location - 1])

#add 'Bananas to the beinging of the list'
series01_list = ["Bananas"] + series01_list
print(series01_list)

#insert 'Plums' to the begining of the list
series01_list.insert(0, "Plums")
print(series01_list)

#loop through the complete list and display fruits that begin with 'P'
for i in series01_list:
    if i[0] == "P":
        print(i)

#series 2 assignment
print("\n" + "--- Series02 ---" + "\n")
series02_list = original_fruit_list[:]
print(series02_list)

#remove the last fruit from the list
del(series02_list[-1])
print(series02_list)

#user enters fruit to be removed from list
remove_fruit = input("Which fruit would you like to remove? > ")
if remove_fruit in series02_list:
    series02_list.remove(remove_fruit)
    print(series02_list)

#bonus
print("\n" + "--- Series02_Bonus ---" + "\n")
fruit_list_bonus = series02_list[:] * 2
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
print("\n" + "--- Series03 ---" + "\n")
series03_list = original_fruit_list[:]

for fruit in series03_list[:]:
    answer = input("Do you like " + fruit.lower() + " ? (yes or no) >" + "\n")
    while not (answer == "yes" or answer == "no"):
        print("Please answer with 'yes' or 'no'")
        answer = input("  Do you like " + fruit.lower() + " ? (yes or no) >"+ "\n")
    if answer == "no":
        series03_list.remove(fruit)
    if len(series03_list) == 0:
        series03_list = "you don't like these fruits"
print(series03_list)

#series 4 assignmet
#copy the original list and reverse the letters of each word
print("\n" + "--- Series04 ---" + "\n")
series04_list = original_fruit_list[:]
rev_list = []
for fruit in series04_list:
    rev_list.append(fruit[::-1])
print(rev_list)

#remove last item from original list and print
original_fruit_list.pop()
print(original_fruit_list)