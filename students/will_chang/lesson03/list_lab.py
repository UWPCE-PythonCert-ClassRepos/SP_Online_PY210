# Series 1

fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits)

user_fruit = input("\nPlease enter the name of a fruit: ")
fruits.append(user_fruit)
print(fruits)

user_number = int(input("\nPlease enter a number between 1 and {}: ".format(len(fruits))))
print("The number {} corresponds to {}.".format(user_number, fruits[user_number-1]))

fruits = ["Pineapple"] + fruits
print("\nPineapple has been added to the beginning of the list.")
print(fruits)


fruits.insert(0, "Dragon Fruit")
print("\nDragon Fruit has been added to the beginning of the list.")
print(fruits)

print("\nThese are all the fruits in the list that begin with the letter 'P':")
for i in fruits:
    if i[0].lower() == "p":
        print(i)

        
# Series 2
fruits_series2 = fruits[:] # Copy of list from Series 1.
print("\n")
print(fruits_series2)
fruits_series2.pop()
print("\nThe last fruit in the list has been removed.")
print(fruits_series2)

delete_fruit = input("\nPlease enter a fruit to delete from the list: ")
fruits_series2.remove(delete_fruit)
print(fruits_series2)

# Series 2 (Bonus)
fruits_series2 = fruits_series2 * 2
print("\nThe whole list has been multiplied by 2.")
print(fruits_series2)
delete_fruit_occurrences = input("\nPlease enter a fruit to delete from the list: ")
while(delete_fruit_occurrences not in fruits_series2):
    delete_fruit_occurrences = input("Fruit specified not in list. Please enter a fruit to delete from the list: ")
fruits_series2.remove(delete_fruit_occurrences)
fruits_series2.remove(delete_fruit_occurrences)
print(fruits_series2)


# Series 3
print("\nThis is the original list from Series 1.")
print(fruits)
fruits_series3 = fruits[:]
for fruit in fruits:
    ask_fruit = input("\nDo you like {}? ".format(fruit))
    while(ask_fruit.lower() != "yes" and ask_fruit.lower() != "no"):
        ask_fruit = input("\nDo you like {}? (Please give a 'Yes' or 'No' answer.) ".format(fruit))
    if(ask_fruit.lower() == 'no'):
        fruits_series3.remove(fruit)
print(fruits_series3)


# Series 4
print("\nThis is the original list from Series 1.")
print(fruits)
fruits_series4 = fruits[:]
for i in range(len(fruits_series4)):
    fruits_series4[i] = fruits_series4[i][::-1]
print("\nThis is a copy of the original list with each fruit's letters reversed.")
print(fruits_series4)

fruits.pop()
print("\nThe last item has been removed from the original Series 1 list.")
print(fruits)