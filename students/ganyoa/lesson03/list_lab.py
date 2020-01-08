#series 1 assignment

#create a list of fruit and print the list
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit_list)

#present the user an option to input an additional fruit to the end of the list
response = input("What fruit would you like to add?: ")
fruit_list.append(response)
print(fruit_list)

#have the user select one fruit based on their numbered location
fruit_location = int(input("Enter the cooresponding number for one fruit: "))
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
