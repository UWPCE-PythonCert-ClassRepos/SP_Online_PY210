#!/usr/bin/env python3
"""
Jack Anderson PY210
Exercise 3.2:  List Lab
02/11/20

Overview: Four series covering the basic ins and outs of Python lists.

"""

def ask_number(list):
    """
    Action to prompt user for a number and then return the nth item listed. Checks for out of range numbers
    are included in this function.
    :param list: List of items to evaluate
    :return: Display nth item in list
    """
    ask_num_prompt = input("Please enter a number:  ")

    if ask_num_prompt.isnumeric():
        x = int(ask_num_prompt)
        max = len(list)
        if x > max or x <= 0:
            print("That number is out of range!!!")
            ask_number(list)
        else:
            y = x - 1
            print_item("{} = {}".format(x, list[y]))
    else:
        print("Please enter a numerical value")
        print_item(list)
        ask_number(list)




def add_fruit(list):
    """
    Action to prompt user for a fruit to add to the fruit_list. Uses "+" to add item
    :param list: List for item to be added
    :return: Display list with new item
    """
    ask = [input("Please enter another fruit to add to this list:  "),]
    x = ask + list
    list = x
    print_item(list)




def add_more_fruit(list):
    """
    Action to prompt user for a fruit to add to the fruit_list. Uses .insert() to add item
    :param list: List for item to be added
    :return: Display list with new item
    """
    ask = input("Please enter one more fruit to add to this list:  ")
    list.insert(0, ask)
    print_item(list)


def sort_fruit(list):
    """
    Action to find all list items starting with "P" or "p", add these items to a list and then display these items
    :param list: List of items to iterate through during the sorting
    :return: sorted list containing all items starting with "P" or "p".
    """
    letter = 'P'
    z = str(letter.lower())
    sorted_fruit_list = []
    for fruit in list:
        if fruit.startswith(z) or fruit.startswith(letter):
            sorted_fruit_list.append(fruit)
    if sorted_fruit_list is not None:
        print_item(sorted_fruit_list)


def series_1_start():
    """
    Action to call all functions needed to complete the series 1 assignment of the list_lab.py
    :return: Various list items based on user input
    """
    fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
    print()
    print_item(fruit_list)
    ask = input("Please add a fruit to the list:  ")
    fruit_list.append(ask)
    print_item(fruit_list)
    ask_number(fruit_list)
    add_fruit(fruit_list)
    add_more_fruit(fruit_list)
    sort_fruit(fruit_list)


def series_2_start():
    """
    Action to display a list and then remove last item in list. Then continueally prompt user for an item to remove
    until a valid item is entered. Then remove item enter by user
    :return: List with last item removed and item entered by user prompt removed
    """
    fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
    print("Starting series 2.....")
    print(fruit_list)
    fruit_list.pop()
    print_item(fruit_list)
    ask = input("Please enter a fruit to remove from this list: ")
    x = ask.title()
    while x not in fruit_list:
        print("This item is not listed")
        ask = input("Please enter a fruit to remove from this list: ")
        x = ask.title()

    while x in fruit_list:
        fruit_list.remove("{}".format(x))
    print(fruit_list)



def series_3_start():
    """
    Action to prompt user with yes/no for each item in list. A seperate list of items marked 'no' is created.
    Function then iterates through both lists and removes items matching.
    :return: List with items containing the 'yes' response from user input
    """
    fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
    print("Starting series 3.....")
    print(fruit_list)
    items_to_delete = []

    for item in fruit_list:
        ask = input("Do you like {}?   ".format(item.lower()))
        while ask not in {'yes', 'no'}:
            print("Please enter 'yes' or 'no' ")
            ask = input("Do you like {}?   ".format(item.lower()))

        if ask == 'no':
            items_to_delete.append(item)

    for items in items_to_delete:
        fruit_list.remove(items)

    print_item(fruit_list)


def series_4_start():
    """
    Action to create a new list and copy items in provided list in reverse order. Action also removed last item
    in provided list
    :return: List with items containing the 'yes' response from user input
    """
    fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
    series_4_list = []
    print("Starting series 4.....")
    for items in fruit_list:
        series_4_list.append(items[::-1])
    fruit_list.pop()
    print("Original list: ", fruit_list)
    print("Copied list: ",  series_4_list)
    print()


def print_item(x):
    # Simple print formatting
    print(x)
    print()




def start_list_lab():
    # Calls a series for the list_lab.py assignment
    series_1_start()
    series_2_start()
    series_3_start()
    series_4_start()



start_list_lab()


