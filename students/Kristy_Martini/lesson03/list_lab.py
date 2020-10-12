#!/usr/bin/env python3
from slicing_lab import reverse

if __name__ == "__main__":
    # Series 1
    # Create the initial list
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]   
    # Ask the user for a new fruit and add it to the list
    new_fruit = input("Please enter the name of a fruit: ")
    fruits.append(new_fruit)
    # Dispaly the list
    print("List of fruits: ", fruits)
    # Ask the user for a number
    number_display = input("Please enter a number between 1 and 5 (inclusive): ")
    # Display the numbered fruit in the list
    print("Fruit at that value:", fruits[int(number_display)-1])
    # Add a fruit to the beginning of the list using the '+' operator
    fruits = ["Grapes"] + fruits
    print("Newly added fruit:", fruits[0])
    # Add another fruit using the insert() method, then display list
    fruits.insert(0, "Bananas")
    print("Updated list of fruit: ", fruits)
    for item in fruits:
        if item.startswith("P"):
            print(item)

    # Series 2
    # Display the list
    fruits2 = fruits
    print("Displaying the list of fruits: ", fruits2)
    # Remove the last fruit and display list
    fruits2.pop(len(fruits2)-1)
    print("Updated list of fruits: ", fruits2)
    # Ask the user for a fruit to delete, find it, and delete it
    fruit_delete = input("Please enter the name of a fruit you wish to delete from the list: ")
    i = 0
    #fruits *= 2
    while i < len(fruits2):
        if (fruits2[i] == fruit_delete):
            fruits2.pop(i)
        i += 1

    # Series 3
    # Ask the user for their preference on each entry in the list
    fruits3 = fruits
    i = 0
    while i < len(fruits3):
        input_string = "Do you like " + fruits3[i] + "? Please enter 'Yes' or 'No': "
        response = input(input_string)
        while (response != "No") & (response != "Yes"):
            response = input(input_string)
        if response == "No":
            fruits3.pop(i)
        i += 1
    print(fruits3)

    # Series 4
    # Make a new list with the contents of the original but with each item reversed
    fruits4 = []
    for item in fruits:
        reverse_item = reverse(item)
        fruits4.append(reverse_item)
    # Delete the last item of the original list 
    fruits.pop(len(fruits)-1)
    # Display original list
    print("Original fruits list: ", fruits)
    #Display copied (reversed) list
    print("Reversed list: ", fruits4)

            