#!/usr/bin/env python3
# Russell Felts
# Assignment 3 - List Lab Exercise


# Series 1

def series1():
    """
    Create a list and modify it by:
    Asking the user for another fruit and adding it to the end of the list
    Adding another fruit to the beginning of the list using “+”
    Adding another fruit to the beginning of the list using insert().
    Also print out the every item in the list that start with the letter P.
    :return list - the modified list
    """
    print("Start series 1...\n")

    fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
    print("List:", fruit_list, "\n")

    response = input("Please enter another fruit: ")
    fruit_list.append(response)
    print(fruit_list, "\n")

    list_size = len(fruit_list)
    num_request = "Please enter a number between 1 and " + str(list_size) + ": "
    response = input(num_request)

    # Validate the user input
    while int(response) > list_size or int(response) <= 0:
        print("\nThe number entered is not in the list range of 1 to ", list_size, ".\n")
        response = input(num_request)

    print("\nThe number " + str(response) + " item in the list is: " +
          fruit_list[int(response) - 1] + "\n")

    fruit_list = ["Pineapples"] + fruit_list[:]
    print(fruit_list, "\n")

    fruit_list.insert(0, "Cherries")
    print(fruit_list, "\n")

    # Display all the fruits that begin with “P”
    print("Printing all fruits in the list that start with the letter P:\n")
    for x in fruit_list:
        if x[:1] == "P":
            print(x)
    return fruit_list


def series2(fruit_list):
    """
    Receives a list and modifies it by:
    Removing the last item from the list then asking the user for an item to delete
    :param fruit_list - The list to modify
    """
    print("\nStart series 2...\nList:", fruit_list, "\n")

    del fruit_list[len(fruit_list)-1]
    print("The list after deleting the last item:\n", fruit_list, "\n")

    request_string = "What fruit would you like to delete from the list? "
    response = input(request_string)

    # Verify the requested fruit is in the list.
    while not any(s.lower() == response.lower() for s in fruit_list):
        print("\n", response, "is not in the list.\n", fruit_list, "\n")
        response = input(request_string)

    fruit_list.remove(response)
    print("\nNew list after removing ", response, ":\n", fruit_list, "\n")


def series3(fruit_list):
    """
    Receives a list and modifies it by asking the user if they like the items in the list and removing the ones they
    don't like.
    :param fruit_list - The list to modify
    """
    print("Start series 3...\nList:", fruit_list, "\n")

    for x in fruit_list:
        response = input("Do you like " + x.lower() + ": ")

        # For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values
        while response.lower() != "yes" and response.lower() != "no":
            response = input("\nPlease respond with yes or no:\nDo you like " + x.lower() + ": ")

        # For each “no”, delete that fruit from the list.
        if response.lower() == "no":
            fruit_list.remove(x)

    print("\nHere is the new list without the items you don't like:",
          fruit_list, "\n")


def series4(fruit_list):
    """
    Receives a list of strings and reverses the individual letters in each item. Then deletes the last item in the
    original list and displays both lists.
    :param fruit_list - The list to modify
    """
    print("Start series 4...\nOriginal List:", fruit_list, "\n")

    # Make a copy of the list and reverse the letters in each item in the copy. Use enumerate to get the subscript
    # value of each individual string in the list.
    fruit_list_copy = fruit_list[:]
    for i, x in enumerate(fruit_list_copy):
        fruit_list_copy[i] = x[::-1]

    # Delete the last item of the original list.
    del fruit_list[len(fruit_list)-1]

    print("Here's the original list with the last item deleted:\n", fruit_list)
    print("Here is a copy of the original list with each item reversed:\n", fruit_list_copy)


# Execute the functions
fruit_list_2 = series1()

series2(fruit_list_2)

series3(fruit_list_2)

series4(fruit_list_2)
