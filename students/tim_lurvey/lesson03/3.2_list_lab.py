#!/usr/bin/env python
__author__ = 'Timothy Lurvey'

import sys
import copy

base_list = ["Apples", "Pears", "Oranges", "Peaches"]

def series1():
    """Create a list that contains "Apples", "Pears", "Oranges" and "Peaches".
    - Display the list (plain old print() is fine…).
    - Ask the user for another fruit and add it to the end of the list.
    - Display the list.
    - Ask the user for a number and display the number back to the user and the fruit
        corresponding to that number (on a 1-is-first basis). Remember that Python uses
        zero-based indexing, so you will need to correct.
    - Add another fruit to the beginning of the list using "+" and display the list.
    - Add another fruit to the beginning of the list using insert() and display the list.
    - Display all the fruits that begin with "P", using a for loop"""
    print("Running Series 1")
    #
    global base_list
    fruit_list = copy.copy(base_list)
    print("Fruits", fruit_list)
    #
    while True:
        x = input("Type anther fruit to be added to the list.  'q' to proceed\n> ")
        if x == 'q': break
        #
        if x: fruit_list.append(x.strip())
    # print user index
    while True:
        i = input("Choose between 1 and {n} to display the corresponding fruit.  'q' to proceed\n> ".format(n=len(fruit_list)))
        if i == 'q': break
        #
        try:
            assert len(fruit_list) >= int(i) >= 1
            print("Fruit[{i}]: {f}".format(i=i, f=fruit_list[int(i) - 1]))
        except ValueError:
            print("You didnt enter an integer! Error: {}".format(i))
        except AssertionError:
            print("Your integer was not with range")
    #
    fruit_list = ["Bananas"] + fruit_list
    print(fruit_list)
    #
    fruit_list.insert(0, "Nectarines")
    print(fruit_list)
    #
    print("'P' fruits:")
    for f in fruit_list:
        if f.startswith('P'):
            print(f)
    #
    return True


def detele_from_list(val:str, lst:list):
    while True:
        try:
            lst.pop(lst.index(val))
        except ValueError:
            break
    return True


def series2():
    """Using the list created in series 1 above:
    -Display the list.
    -Remove the last fruit from the list.
    -Display the list.
    -Ask the user for a fruit to delete, find it and delete it.
    -(Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)"""
    #
    global base_list
    fruit_list = copy.copy(base_list)
    #
    fruit_list2 = fruit_list * 2
    print(fruit_list2)
    #
    fruit_list2.pop()
    print(fruit_list2)
    #
    while True:
        x = input("Type a fruit to be deleted.  'q' to Quit\n> ")
        if x == 'q': break
        #
        detele_from_list(val=x, lst=fruit_list2)
        print(fruit_list2)
    #
    return True


def series3():
    """Again, using the list from series 1:
    - Ask the user for input displaying a line like “Do you like apples?” for each
        fruit in the list (making the fruit all lowercase).
    - For each “no”, delete that fruit from the list.
    - For any answer that is not “yes” or “no”, prompt the user to answer with one
        of those two values (a while loop is good here)
    - Display the list."""
    #
    global base_list
    fruit_list = copy.copy(base_list)
    #
    for i in range(len(fruit_list), 0, -1):
        f = fruit_list[i - 1]
        x = input("Do you like {}?  [ yes, no, 'q' to Quit]\n> ".format(f))
        if x=='q': break
        #
        if 'no' in x.lower():
            detele_from_list(val=f, lst=fruit_list)
        elif 'yes' in x.lower():
            continue
        else:
            print("Invalid entry! Error: {}".format(x))
        #
        print(fruit_list)
    #
    return True


def series4():
    """Once more, using the list from series 1:
    - Make a new list with the contents of the original, but with all the letters in each item reversed.
    - Delete the last item of the original list. Display the original list and the copy."""
    #
    global base_list
    fruit_list = copy.copy(base_list)
    #
    fruit_reversed = [f[::-1] for f in fruit_list]
    #
    fruit_list.pop()
    print(fruit_list)
    print(fruit_reversed)
    return True


def main(args):
    while True:
        x = input("\nSelect a series to run: 1, 2, 3, 4, or 'q' to quit\n> ")
        if 'q' == x.lower():
            break
        elif int(x) == 1:
            series1()
        elif int(x) == 2:
            series2()
        elif int(x) == 3:
            series3()
        elif int(x) == 4:
            series4()
        else:
            print("Error.  Select a value.")
    return True


if __name__ == '__main__':
    main(sys.argv[1:])