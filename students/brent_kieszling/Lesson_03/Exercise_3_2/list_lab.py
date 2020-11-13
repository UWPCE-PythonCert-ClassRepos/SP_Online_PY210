#!/usr/bin/env python3
#-------------------------------------------#
#Tittle: list_lab, PYTHON210 - Exercise 3.2
#Desc: List Exercises
#Change Log: (Who, When, What)
#Brent Kieszling, <2020-Nov-4>, created file
#-------------------------------------------#

#DATA---------------------------------------

fruits = ["Apples", "Pears", "Oranges", "Peaches"]


#PROCESS------------------------------------
def series_1(lst_fruits):
    """Perform a series of operations on a list.
    
    Args:
        lst_fruits (list): list to be manipulated.
    """
    mod_fruits = lst_fruits[:]
    print(mod_fruits)
    new_fruit = input("What fruit would you like to add? ")
    mod_fruits.append(new_fruit)
    print("The new list is: \n {}".format(mod_fruits))
    select_fruit = int(input("Please select a fruit to inspect (1-{}) ".format(len(mod_fruits))))
    print(mod_fruits[select_fruit-1])
    print()
    
    print("Adding Kiwi to the front of the list")
    a = ["Kiwi"]
    mod_fruits = a + mod_fruits
    print(mod_fruits)
    print()
    
    print("Adding Melon to the front of the list")
    mod_fruits.insert(0, "Melon")
    print(mod_fruits)
    print()
    
    print("Displaying all elements that start with P")
    for item in mod_fruits:
        if item[0] == "P":
            print(item)

def series_2(lst_fruits):
    """Perform a series of operations on a list.
    
    Args:
        lst_fruits (list): list to be manipulated.
    """
    mod_fruits = lst_fruits[:]
    print(mod_fruits)
    print("Removing last item.")
    mod_fruits.pop()
    print(mod_fruits)
    while True:
        select_fruit = input("Please enter the fruit you would like to delete: ")
        if select_fruit in mod_fruits:
            for item in mod_fruits[:]:
                if item == select_fruit:
                    mod_fruits.remove(item)
            break
        else:
            print("The fruit you provided was not recognized, doubling the list")
            mod_fruits = mod_fruits * 2
            print(mod_fruits)
    print(mod_fruits)

def series_3(lst_fruits):
    """Loop through list and delete specific entries
    
    Args:
        lst_fruits (list): list to be manipulated.
    """
    mod_fruits = lst_fruits[:]
    print(mod_fruits)
    for item in mod_fruits:
        while True:
            a = input("Do you like {}? ".format(item.lower()).lower())
            if a == "yes":
                break
            elif a == "no":
                print("Removing {}.".format(item.lower()))
                mod_fruits.remove(item)
                break
            else:
                print("Please use 'yes' or 'no'.")
    print(mod_fruits)

def series_4(lst_fruits):
    """Reverse the order of items inside of a list
    
    Args:
        lst_fruits (list): list to be manipulated.
    """
    mod_fruits = lst_fruits[:]
    a = 0
    for item in mod_fruits[:]:
        reverse = item[::-1]
        mod_fruits[a] = reverse
        a += 1
    lst_fruits.pop()
    print(mod_fruits)
    print(lst_fruits)


#PRESENTATION INPUT/OUTPUT------------------

print("Series 1:")
series_1(fruits)
print()

print("Series 2:")
series_2(fruits)
print()

print("Series 3:")
series_3(fruits)
print()

print("Series 4:")
series_4(fruits)









