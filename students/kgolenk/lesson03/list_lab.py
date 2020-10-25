#!/usr/bin/env python3
# ---------------------------------------------------------------------------- #
# Title: Lesson 03
# Description: List Lab
# ChangeLog (Who,When,What):
# Kate Golenkova, 10/16/2020, Created script
# ---------------------------------------------------------------------------- #


# Series 1 ------------------------------------------------------------------ #
fruits_list = ["Apples", "Pears", "Oranges", "Peaches"]

def series1():
    """ Returns list fruits after several changes """

    print("This is python script Series 1")
    fruits = fruits_list[:]
    print(fruits)
    add_last_fruit = input("Please add another fruit to the list: ")
    fruits.append(add_last_fruit)
    print(fruits)
    index = int(input("Please type any number from 1 to 5:  "))
    for i, name in enumerate(fruits, 1):
        if i == index:
            print(i, name)

    fruits = ["Banana"] + fruits
    print(fruits)
    fruits.insert(0, "Pineapple")
    print(fruits)

    for i in fruits:
        if i[0].lower() == 'p':
            print(i)

    return fruits

series1()

# Series 2 ------------------------------------------------------------------ #

def series2():
    """ Returns list fruits after several changes """

    print("This is python script Series 2")
    fruits = fruits_list[:]
    print(fruits)
    fruits.remove(fruits[-1])
    print(fruits)
    del_fruit = input("Please type the fruits you want to delete from list: ")
    for i in fruits:
        if i == del_fruit:
            fruits.remove(i)
    print(fruits)
    fruits = fruits*2
    for i in fruits:
        if i == del_fruit:
            fruits.remove(i)
    print(fruits)

series2()

# Series 3 ------------------------------------------------------------------ #

def series3():
    """ Returns list fruits after several changes """

    print("This is python script Series 3")
    fruits = fruits_list[:]
    print(fruits)
    for i in fruits[::-1]:
        while True:
            answer = input("Do you like " + i.lower() + "? :")
            if answer.lower() == 'yes':
                break
            elif answer.lower() == 'no':
                fruits.remove(i)
                break
            else:
                print("Please use yes or no, do you like " + i.lower() + "? :")
    print(fruits)


series3()

# Series 4 ------------------------------------------------------------------ #

def series4():
    """ Returns list fruits after several changes """

    print("This is python script Series 4")
    new_fruits = []
    for i in fruits_list:
        new_fruits.append(i[::-1])

    three_fruits = fruits_list[:]
    three_fruits.remove(three_fruits[-1])

    print("This is original list: ", fruits_list)
    print("This is copy list with letters reversed: ", new_fruits)


series4()


