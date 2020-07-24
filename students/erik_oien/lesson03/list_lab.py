#!/usr/bin/env python3

# Series 1

def series1(fruits):
    # Display the list (plain old print() is fine…).
    print(fruits)

    # Ask the user for another fruit and add it to the end of the list.
    new_fruit = input("What fruit would you like to add? > ")
    fruits.append(new_fruit)

    # Display the list.
    print(fruits)

    # Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
    new_number = input("Please pick a number. > ")
    print(new_number, fruits[int(new_number)-1])

    # Add another fruit to the beginning of the list using "+" and display the list.
    new_fruit = input("Please add another fruit > ")
    fruits = [new_fruit] + fruits
    print(fruits)

    # Add another fruit to the beginning of the list using insert() and display the list.
    new_fruit = input("Please add another fruit > ")
    fruits.insert(0, new_fruit)
    print(fruits)

    # Display all the fruits that begin with "P", using a for loop.
    p_fruits = []
    for fruit in fruits:
        if fruit[0].upper() == "P":
            p_fruits.append(fruit)
    print(p_fruits)
    return fruits

# Series 2

def series2(fruits):
    # Using the list created in series 1 above:
    # Display the list.
    print(fruits)

    # Remove the last fruit from the list.
    fruits = fruits[0:-1:]

    # Display the list.
    print(fruits)

    # Ask the user for a fruit to delete, find it and delete it.
    delete_fruit = input("What fruit would you like to delete? > ")
    fruits.remove(delete_fruit)
    print(fruits)

    # (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
    # multiplied_fruit = fruits * 2
    # delete_fruit = input("What fruit would you like to delete? > ")
    # print(multiplied_fruit)

# Series 3

def series3(fruits):
    # Ask the user for input displaying a line like "Do you like apples?" for each fruit in the list (making the fruit all lowercase).
    # For each "no", delete that fruit from the list.
    # For any answer that is not "yes" or "no", prompt the user to answer with one of those two values (a while loop is good here)
    # Display the list.
    liked_fruits = fruits[:]
    for fruit in fruits:
        fruit_opinion = input("Do you like " + fruit.lower() + "? > ")
        while fruit_opinion.lower() not in ['yes', 'no']:
            fruit_opinion = input("Do you like " + fruit.lower() + "?" + " Please answer with yes or no. > ")
        if fruit_opinion == "no":
            liked_fruits.remove(fruit)
    print(liked_fruits)

# Series 4

def series4(fruits):
    # Once more, using the list from series 1:
    # Make a new list with the contents of the original, but with all the letters in each item reversed.
    reverse_fruit = []
    for fruit in fruits:
        reverse_fruit.append(fruit[len(fruit)::-1])
    print(reverse_fruit)

    # Delete the last item of the original list. Display the original list and the copy.
    print(fruits)
    print(reverse_fruit[0:-1:])

if __name__ == "__main__": 
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    new_fruit_list = series1(fruits)
    series2(new_fruit_list)
    series3(new_fruit_list)
    series4(new_fruit_list)