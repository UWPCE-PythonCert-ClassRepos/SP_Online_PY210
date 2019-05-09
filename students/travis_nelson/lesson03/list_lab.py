#!/usr/bin/env python3

# Series 1


def series_1():
    """Create a list of fruit.
    Display the list.
    Ask user for another fruit, add it to the end of list.
    Display the list.
    Ask user for a number and display the number back to user
    and the fruit corresponding to that number.
    Add another fruit to the beginning of the list using "+" and display list.
    Add another fruit to the beginning of the list using insert().
    Display all fruits that begin with "P" using a for loop.
    """
    fruit = ["Apples", "Pears", "Oranges", "Peaches"]
    print(fruit)
    received_fruit = input("Another fruit, please. ---> ").title()
    fruit.append(received_fruit)
    print(fruit)
    received_number = input("What number fruit would you like to know? ---> ")
    print("Fruit number {} is ".format(received_number) +
          fruit[int(received_number)-1])
    fruit = ["Durian"] + fruit
    print(fruit)
    fruit.insert(1, "Cantaloupe")
    print(fruit)
    for i in fruit:
        if i[0].upper() == 'P':
            print(i)
    return fruit


def series_2():
    """Using the list created in series_1():
    Display the list.
    Remove the last fruit from the list.
    Display the list.
    Ask the user for a fruit to delete, find it and delete it.
    Bonus - multiplies the list twice. Keep asking until a match is found.
    Once found, delete all occurences.
    """
    fruit = series_1() * 2
    print(fruit)
    del fruit[-1:]
    print(fruit)
    deletion_request = ""
    while deletion_request.title() not in fruit:
        deletion_request = input("Which fruit should be deleted? ---> ")
    while deletion_request.title() in fruit:
        fruit.remove(deletion_request.title())
    print(fruit)


def series_3():
    """Using the list created in series_1():
    Ask the user if they like each fruit in the list.
    Delete all fruit the user doesn't like.
    For any answer that isn't 'yes' or 'no', prompt user for a new answer.
    Display the list.
    """
    fruit = series_1()
    for i in fruit[:]:
        keep_asking = True
        received_preference = ""
        while keep_asking:
            received_preference = input("Do you like {}?---> ".format(
                                        i.lower()))
            if received_preference.lower() == "yes":
                keep_asking = False
                break
            if received_preference.lower() == "no":
                fruit.remove(i)
                keep_asking = False
                break
            print("Please respond with 'yes' or 'no'.")
    return fruit


def series_4():
    """Using the list created in series_1():
    Make a new list with the contents of the original, but with all the letters
    in each item reversed.
    Delete the last item of the original list.
    Display the original list and the copy.
    """
    fruit = series_1()
    reversed_fruit = []
    for i in fruit[:]:
        reversed_fruit.append(reverse_items(i))
    del fruit[-1:]
    print(fruit, reversed_fruit)


def reverse_items(sequence):
    """Returns a passed sequence with its individual elements reversed"""
    reversed_item = sequence[::-1]
    return reversed_item
