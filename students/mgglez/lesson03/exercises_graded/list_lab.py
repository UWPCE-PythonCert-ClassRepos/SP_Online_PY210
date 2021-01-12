#!/usr/bin/env python

# ---------------------------------------------------------------------------- #
# Title: Lesson 3
# Description: Exercise 3.2 - List Lab (Graded Exercise)
# ChangeLog (Who,When,What):
# Mercedes Gonzalez Gonzalez,01-10-2021, Created List Lab Functions
# ---------------------------------------------------------------------------- #

def series1(fruit_list):
    """
    Implement all the instructions from List Lab Series 1
    :param fruit_list: (list) Original list of fruits
    :return: (list) Modified list of fruits
    """
    # Display the list (plain old print() is fine…).
    print(fruit_list)
    # Ask the user for another fruit and add it to the end of the list.
    another_fruit = input("Please, which other fruit do you want to add to this list? : ")
    fruit_list.append(another_fruit)
    # Display the list.
    print(fruit_list)
    # Ask the user for a number and display the number back to the user and the fruit corresponding
    # to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you
    # will need to correct.
    f_index = int(input("Select the index for the fruit you want to display [1-{}] :".format(len(fruit_list))))
    print("Fruit #{} is: {}".format(f_index, fruit_list[f_index - 1]))
    # Add another fruit to the beginning of the list using “+” and display the list.
    another_fruit = 'Bananas'
    fruit_list = [another_fruit] + fruit_list
    print(fruit_list)
    # Add another fruit to the beginning of the list using insert() and display the list.
    another_fruit = 'Grapes'
    fruit_list.insert(0, another_fruit)
    print(fruit_list)
    # Display all the fruits that begin with “P”, using a for loop.
    for fruit in fruit_list:
        if fruit.startswith('P'):
            print(fruit)
    return fruit_list

def series2(fruit_list):
    """
    Implement all the instructions from List Lab Series 2 + Bonus
    :param fruit_list: (list) Original list of fruits
    :return: (list) Modified list of fruits
    """
    # Display the list.
    print(fruit_list)
    # Remove the last fruit from the list.
    print("Removed item from the fruit list: {}".format(fruit_list.pop()))
    # Display the list.
    print(fruit_list)
    # Ask the user for a fruit to delete, find it and delete it.
    # (Bonus: Multiply the list times two. Keep asking until a match is found. Once found,
    # delete all occurrences.)
    fruit_list *= 2
    while True:
        print(fruit_list)
        fruit_to_delete = input("Enter the name of the fruit you want to delete: ")
        if fruit_to_delete not in fruit_list:
            print("The fruit you provided was not found in the fruit list. Please try again.")
        else:
            for i in range(fruit_list.count(fruit_to_delete)):
                fruit_list.remove(fruit_to_delete)
            break
    print(fruit_list)
    # Turning the list into a set to remove duplicate items, and then returning a list
    new_fruit_list = list(set(fruit_list))
    print(new_fruit_list)
    return new_fruit_list

def series3(fruit_list):
    """
    Implement all the instructions from List Lab Series 3
    :param fruit_list: (list) Original list of fruits
    :return: (list) Modified list of fruits
    """
    # Ask the user for input displaying a line like “Do you like apples?”
    # for each fruit in the list (making the fruit all lowercase).
    # For each “no”, delete that fruit from the list.
    # For any answer that is not “yes” or “no”, prompt the user to answer with
    # one of those two values (a while loop is good here)
    # Display the list.

    for fruit in fruit_list[:]:
        while True:
            choice = input("Do you like {}? [yes/no]".format(fruit.lower()))
            if choice.lower().strip() == 'no':
                # Fruit will be removed
                while fruit in fruit_list:
                    fruit_list.remove(fruit)
                break
            elif choice.lower().strip() == 'yes':
                # Fruit will not be removed
                break
            else:
                # Keep asking until a valid answer is provided
                print("Your answer is invalid. Respond with 'yes' or 'no'")
    print(fruit_list)
    return fruit_list

def series4(fruit_list):
    """
    Implement all the instructions from List Lab Series 4
    :param fruit_list: (list) Original list of fruits
    :return: (list) Modified list of fruits
    """
    # Make a new list with the contents of the original, but with all the letters in each item reversed.
    new_fruit_list = [fruit[::-1] for fruit in fruit_list[:]]
    # Delete the last item of the original list. Display the original list and the copy.
    fruit_list.pop()
    print(fruit_list)
    print(new_fruit_list)

if __name__ == '__main__':
    # Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
    fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
    fruit_list = series1(fruit_list)
    fruit_list = series2(fruit_list)
    fruit_list = series3(fruit_list)
    series4(fruit_list)