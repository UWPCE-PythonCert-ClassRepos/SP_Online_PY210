#!/usr/bin/env python3

"""
Lesson 3: List Lab
Course: UW PY210
Author: Jason Jenkins
"""


def series_1(list=[]):
    """
    Practicing using lists
    """

    # Make a copy of list
    list = list[:]

    print()
    print("Starting series_1:")
    print()
    Display_List(list)

    # Add to list
    list.append(input("Input another fruit to the list: "))
    Display_List(list)

    # Find and output an item
    loc = input("Input fruit number to print (Starting at 1): ")
    loc = int(loc) - 1
    if (0 <= loc < len(list)):
        print(list[loc])

    # Add to beginning of the list using "+" creating a local object
    response = input("Input another fruit to the list: ")
    list = [response] + list
    Display_List(list)

    # Add to beginning of the list using "insert"
    response = input("Input another fruit to the list: ")
    list.insert(0, response)
    Display_List(list)

    # Display all the fruits that begin with “P”, using a for loop
    for item in list:
        if(item[0] == "P"):
            print(item)

    return list


def series_2(list=[]):
    """
    Practicing using lists
    """

    # Make a copy of list
    list = list[:]

    print()
    print("Starting series_2:")
    print()
    Display_List(list)

    # Remove last item on list
    print("Removing last items")
    list.pop()
    Display_List(list)

    # Remove requested item from list
    loc = input("Input fruit number to remove (Starting at 1): ")
    loc = int(loc) - 1
    if (0 <= loc < len(list)):
        list.pop(loc)
    Display_List(list)

    return list


def series_3(list=[]):
    """
    Practicing using lists
    """

    # Make a copy of list
    list = list[:]

    print()
    print("Starting series_3:")
    print()
    Display_List(list)

    # Make all items in list lowercase
    for i in range(len(list)):
        list[i] = list[i].lower()

    # Create a tmplist
    new_list = []

    # Ask used if they like item and remove if no
    print("For the following questions input yes or no.")
    for item in list:
        while(True):
            response = input(f"Do you like {item}? ")

            if(response.lower() == "yes"):
                new_list.append(item)
                break
            elif(response.lower() == "no"):
                break

    Display_List(new_list)

    return new_list


def series_4(list=[]):
    """
    Practicing using lists
    """

    print()
    print("Starting series_4:")
    print()
    Display_List(list)

    # Make a copy of list
    list = list[:]

    # Make a new list
    new_list = []

    # reverse all item leters
    for i, item in enumerate(list):
        new_list.append(str(item)[::-1])

    print(f"New List: {new_list}")

    # Remove Last Item
    list.pop()
    print(f"Orignial list after removing last item: {list}")

    return new_list


def Display_List(list=[]):
    """
    Print the list as a list
    """

    print(f"Current List: {list}")


if __name__ == "__main__":
    # Create a list
    tmp_list = ["Apples", "Pears", "Oranges", "Peaches"]

    series_1_list = series_1(tmp_list)
    series_2_list = series_2(series_1_list)
    series_3_list = series_3(series_1_list)
    series_4_list = series_4(series_1_list)
