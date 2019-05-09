#!/usr/bin/env python3

# Series 1


def series_1():
    """Returns a list of fruit"""
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
