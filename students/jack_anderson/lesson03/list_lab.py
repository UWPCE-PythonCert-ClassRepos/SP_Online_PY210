#!/usr/bin/env python3
"""
Jack Anderson PY210
Exercise 3.2:  List Lab
02/11/20

Overview: Four series covering the basic ins and outs of Python lists.

"""

fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]


def series_1_start():
    series_1_list = []

    for items in fruit_list:
        series_1_list.append(items)
    print_item(series_1_list)
    ask = input("Please enter a new fruit:  ")
    series_1_list.append(ask)
    print_item(series_1_list)
    ask_number(series_1_list)

def ask_number(series_1_list):
    ask_num_prompt = input("Please enter a number:  ")

    if ask_num_prompt.isnumeric():
        x = int(ask_num_prompt)
        max = len(series_1_list)
        if x > max or x <= 0:
            print("That number is out of range!!!")
            ask_number(series_1_list)
        else:
            y = x - 1
            print_item("{} = {}".format(x, series_1_list[y]))
            add_fruit(series_1_list)
    else:
        print("Please enter a numerical value")
        print_item(series_1_list)
        ask_number(series_1_list)


def add_fruit(series_1_list):
    ask = [input("Please enter another fruit:  "),]
    x = ask + series_1_list
    series_1_list = x
    print_item(series_1_list)
    add_more_fruit(series_1_list)


def add_more_fruit(series_1_list):
    ask = input("Please enter another fruit:  ")
    series_1_list.insert(0, ask)
    print_item(series_1_list)
    sort_fruit(series_1_list)



def sort_fruit(series_1_list):
    ask = input("Please enter a single letter from A - Z: ")
    if ask.isalpha():
        x = len(ask)
        if x > 1 or x < 0:
            print_item("You muster enter a single character")
            sort_fruit(series_1_list)
        else:
            z = str(ask.upper())
            q = z.lower()
            sorted_fruit_list = []
            for fruit in series_1_list:
                if fruit.startswith(z) or fruit.startswith(q):
                    sorted_fruit_list.append(fruit)

            if sorted_fruit_list is not None:
                print_item(sorted_fruit_list)
                series_2_start()
            else:
                print_item("There are no fruits that start with " + q + " or " + z)
                series_2_start()
    else:
        sort_fruit(series_1_list)




def series_2_start():
    series_2_list = []
    for items in fruit_list:
        series_2_list.append(items)

    print("Starting series 2.....")
    print(series_2_list)
    series_2_list.pop()
    print_item(series_2_list)
    ask = input("Please enter a fruit to remove from this list: ")
    series_2_list.remove("{}".format(ask))
    print_item(series_2_list)
    series_3_start()


def series_3_start():
    series_3_list = []
    for items in fruit_list:
        series_3_list.append(items)

    print("Starting series 3.....")
    print(series_3_list)
    items_to_delete = []

    for item in series_3_list:
        ask = input("Do you like {}?   ".format(item.lower()))
        while ask not in {'yes', 'no'}:
            print("Please enter 'yes' or 'no' ")
            ask = input("Do you like {}?   ".format(item.lower()))

        if ask == 'no':
            items_to_delete.append(item)

    for items in items_to_delete:
        series_3_list.remove(items)

    print_item(series_3_list)
    series_4_start()

def series_4_start():
    series_4_list = []
    print("Starting series 4.....")
    for items in fruit_list:
        series_4_list.append(items[::-1])
    fruit_list.pop()
    print("Original list: ", fruit_list)
    print("Copied list: ",  series_4_list)
    print()


def print_item(x):
    print(x)
    print()



series_4_start()


