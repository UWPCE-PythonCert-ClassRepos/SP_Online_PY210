#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Lesson 3, Excercise 2

@author: Matt Casari

Link: https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/list_lab.html

Tasks:
    Series 1:
        - Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
        - Display the list (plain old print() is fine…).
        - Ask the user for another fruit and add it to the end of the list.
        - Display the list.
        - Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
        - Add another fruit to the beginning of the list using “+” and display the list.
        - Add another fruit to the beginning of the list using insert() and display the list.
        - Display all the fruits that begin with “P”, using a for loop.

    Series 2:
        Using the list created in series 1 above:
        - Display the list.
        - Remove the last fruit from the list.
        - Display the list.
        - Ask the user for a fruit to delete, find it and delete it.
        - (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
    
    Series 3:
        Again, using the list from series 1:
        - Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
        - For each “no”, delete that fruit from the list.
        - For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
        - Display the list

    Series 4:
        Once more, using the list from series 1:
        - Make a new list with the contents of the original, but with all the letters in each item reversed.
        - Delete the last item of the original list. Display the original list and the copy.

"""

def create_list():
    return ["Apples", "Pears", "Oranges", "Peaches"]

def display_list(list):
    print(list)
    return

def get_new_fruit(list):
    list.append(input("Enter a new fruit: "))
    display_list(list)
    return list

def display_list_by_number(list):
    index = int(input("Enter a number:" ))
    display_list(list[index-1])

def prepend_new_fruit(list):
    list = [input("Enter a new fruit: ")] + list
    display_list(list)
    return list

def prepend_with_insert(list):
    list.insert(0, input("Enter a new fruit: "))
    display_list(list)
    return list

def display_fruits_with_p(list):
    for fruit in list:
        if fruit.lower().find('p') == 0:
            print(fruit)
    return

def remove_last_fruit(list):
    list.pop()
    display_list(list)
    return list

def remove_fruit(list, fruit_to_remove):
    remove_idx = []
    for idx, fruit in enumerate(list):
        if fruit.lower().find(fruit_to_remove.lower())==0:
            remove_idx.append(idx)
    
    if len(remove_idx):
        for idx in remove_idx[::-1]:
            del list[idx]

    return list

def remove_user_fruit(list):

    user_fruit = input("Enter fruit to remove: ").lower()
        
    list = remove_fruit(list, user_fruit)

    display_list(list)
    return list

def prompt_user_dislikes(list):
    for fruit in list[:]:
        result = input("Do you like {}? ".format(fruit.lower()))
    
        while result.lower() != 'yes' and result.lower() != 'no':
            result = input("yes or no >")

        if result == "no":
            list = remove_fruit(list, fruit)

    display_list(list)

def reverse_item_characters(list):
    temp = []
    for fruit in list[:]:
        temp.append( fruit[::-1] )
    return temp

def series_1():
    # Series 1
    print("Start Series 1")
    list = create_list()
    display_list(list)
    list = get_new_fruit(list)
    display_list_by_number(list)
    list = prepend_new_fruit(list)
    list = prepend_with_insert(list)
    display_fruits_with_p(list)

def series_2():
    # Series 2
    print("\nStart Series 2")
    list = create_list()
    display_list(list)
    remove_last_fruit(list)
    list = remove_user_fruit(list*2)

def series_3():
    # Series 3
    print("\nStart Series 3")
    list = create_list()
    prompt_user_dislikes(list)

def series_4():
    # Series 4
    print("\nStart Series 4")
    list1 = create_list()
    list2 = reverse_item_characters(list1[:])
    del list1[-1]
    display_list(list1)
    display_list(list2)

def main():
    series_1()
    series_2()
    series_3()
    series_4()


 



if __name__ == "__main__":
    main()