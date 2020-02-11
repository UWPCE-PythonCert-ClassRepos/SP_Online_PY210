#!/usr/bin/env python3
"""
Jack Anderson PY210
Exercise 3.2:  List Lab
02/11/20

Overview: Four series covering the basic ins and outs of Python lists.

"""

fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]


def series_1_start():
    print_item(fruit_list)
    ask = input("Please enter a new fruit:  ")
    fruit_list.append(ask)
    print_item(fruit_list)
    ask_number(fruit_list)

def ask_number(fruit_list):
    ask_num_prompt = input("Please enter a number:  ")

    if ask_num_prompt.isnumeric():
        x = int(ask_num_prompt)
        max = len(fruit_list)
        if x > max or x < 0:
            print_item("That number is out of range!!!")
            print_item(fruit_list)
            ask_number(fruit_list)
        else:
            y = x - 1
            print_item("{} = {}".format(x, fruit_list[y]))
            add_fruit(fruit_list)
    else:
        print("Please enter a numerical value")
        print_item(fruit_list)
        ask_number(fruit_list)


def add_fruit(fruit_list):
    ask = [input("Please enter another fruit:  "),]
    x = ask + fruit_list
    fruit_list = x
    print_item(fruit_list)
    add_more_fruit(fruit_list)


def add_more_fruit(fruit_list):
    ask = input("Please enter another fruit:  ")
    fruit_list.insert(0, ask)
    print_item(fruit_list)
    sort_fruit(fruit_list)


def sort_fruit(fruit_list):
    ask = input("Please enter a single letter from A - Z: ")
    if ask.isalpha():
        x = len(ask)
        if x > 1 or x < 0:
            print_item("You muster enter a single character")
            sort_fruit(fruit_list)
        else:
            z = str(ask.upper())
            q = z.lower()
            sorted_fruit_list = []
            for fruit in fruit_list:
                if fruit.startswith(z) or fruit.startswith(q):
                    sorted_fruit_list.append(fruit)

            if sorted_fruit_list is not None:
                print_item(sorted_fruit_list)
            else:
                print_item("There are no fruits that start with " + q + " or " + z)
    else:
        sort_fruit(fruit_list)




def print_item(x):
    print()
    print(x)
    print()















series_1_start()







