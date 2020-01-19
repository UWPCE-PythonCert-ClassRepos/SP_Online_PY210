#Isabella Kemp
#1/19/2020
#list lab

# Series 1
# Create a list that displays Apples, Pears, Oranges, Peaches and display the list.
List = ["Apples", "Pears", "Oranges", "Peaches"]
print(List)
# Ask user for another fruit, and add it to the end of the list
Question = input("Would you like another fruit? Add it here: ")
if Question not in List:
    List.append(Question)
print(List)

# Asks user for a number, and displays the number as well as the fruit corresponding
# to the number.
List = ["Apples", "Pears", "Oranges", "Peaches"]
num = int(input("Please enter a number: "))
print(num)
if num < len(List):
    print (List[num-1])

# Adds new fruit (Strawberries) to the beginning of the original fruit list, using +.
new_list = ["Strawberries"] + List
print(new_list)

# Adds new fruit (Strawberries) to beginning of List using insert()
List = ["Apples", "Pears", "Oranges", "Peaches"]
List.insert(0, "Strawberries")
print(List)

# Display all fruits that begin with "P" using a for loop
List = ["Apples", "Pears", "Oranges", "Peaches"]
for fruit in List:
    if "P" in fruit:
        print(fruit)

# Series 2
# Display the List
List = ["Apples", "Pears", "Oranges", "Peaches"]
print(List)
# Removes last fruit in the list
List.pop()
print(List)

# Deletes the fruit the user wants you to delete
delete_fruit = input("Which fruit would you like to delete? ")
for fruit in List:
    if delete_fruit == fruit:
        List.remove(delete_fruit)
        break # exits loop
print(List)

# Series 3
# Asks the user what fruit they like, and if they say no it deletes the fruit, if neither, it will continue to ask.
List = ["Apples", "Pears", "Oranges", "Peaches"]
def find_fav_fruits(List):
    for fruit in List:
        ask_user = input("Do you like " + fruit + "? yes/no?")
        if ask_user == "no":
            List.remove(fruit)
        elif ask_user == "yes":
            continue
        else:
            ask_user = input("Please enter yes or no.")

    print(List)

find_fav_fruits(List)

# Series 4
# Creates a new list with the contents of the original, but all letters in each item reversed.
List = ["Apples", "Pears", "Oranges", "Peaches"]
new_list = [fruit[::-1] for fruit in List][::-1]
print(new_list)

print("Deletes last item of the original list")
List.pop()
print(List)
