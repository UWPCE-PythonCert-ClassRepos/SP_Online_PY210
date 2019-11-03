#!/usr/bin/env python

"""
This is the List Lab.

Entries are case irrelevant.
All strings presented in title case.
Item removal is executed for all instances of a repeated entry.
Input for a repeated entry is presented once.
"""

def Series1():
    """
    This is Series 1.

    Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
    Display the list (plain old print() is fine…).
    Ask the user for another fruit and add it to the end of the list.
    Display the list.
    Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
    Add another fruit to the beginning of the list using “+” and display the list.
    Add another fruit to the beginning of the list using insert() and display the list.
    Display all the fruits that begin with “P”, using a for loop.
    """

    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches'] #1st and second bullets
    print(fruits)

    new_fruit1 = input("Please provide another fruit: ").title() #3rd & 4th bullets
    fruits.append(new_fruit1)
    print(fruits)

    length = len(fruits) #5th bullet
    "Please provide a number between 1 and {}: ".format(length)
    fruit_number = int(input("Please provide a number between 1 and {}: ".format(length)))
    print(fruit_number, fruits[fruit_number - 1])

    new_fruit2 = [input("Please provide another fruit: ").title()] #6th bullet
    fruits = new_fruit2 + fruits
    print(fruits)

    new_fruit3 = input("Please provide another fruit: ").title() #7th bullet
    fruits.insert(0,new_fruit3)
    print(fruits)

    P_list = [] #last bullet
    item_flag = [] #empty matrix allowing prevention of displaying repeated fruits
    for item in fruits:
        if item in item_flag: #check to see if fruit has already been queried
            continue
        if item[0].title() == 'P':
            P_list += [item.title()]
        item_flag.append(item) #list of fruits already checked
    length_P = len(P_list)
    print(("Items beginning with 'P' are " + ", ".join(["{}"] * length_P) + "\n"*2).format(*P_list))

    return fruits #additional return command for following series



def ask():
    ask = input("Do you want the default list? ('yes' or 'no'): ").lower() #option for other Series to take default list or execute Series1
    if ask == 'yes':
        return ['Apples', 'Pears', 'Oranges', 'Peaches']
    elif ask == 'no':
        print("then we must execute Series1 first\n")
        return Series1()



def Series2():
    """
    This is Series2

    Using the list created in series 1 above:

Display the list.
Remove the last fruit from the list.
Display the list.
Ask the user for a fruit to delete, find it and delete it.
(Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
    """

    fruits2 = ask() #call function to take default list or execute Series1

    print(fruits2) #first bullet

    fruits2.pop() #second bullet
    print(fruits2)

    fruits2 = 2 * fruits2 #third bullet
    print('here is the double list: {}'.format(fruits2))

    del_fruit = '' #4th & 5th bullet, not case sensitive
    while del_fruit not in fruits2:
        del_fruit = (input("Please provide a fruit to delete: ")).title()
    while del_fruit in fruits2:
        fruits2.remove(del_fruit)

    print(fruits2) #display results



def Series3():
    """
    This is Series2

Again, using the list from series 1:

Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
For each “no”, delete that fruit from the list.
For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
Display the list.
    """

    fruits3 = ask() #call function to take default list or execute Series1

    item_flag = [] #empty matrix allowing prevention of querying repeated fruits
    fruits3_copy = fruits3[:]
    for i, item in enumerate(fruits3):
        if item in item_flag: #check to see if fruit has already been queried
            continue
        query = input("Do you like {}? ".format(item)).lower()
        if query == ('yes' or 'no'):
            fruits3_copy = yes_no(query, item, fruits3_copy)
        else:
            while query not in  ['yes', 'no']:
                query = (input("""Please answer 'yes' nor 'no' (regardless of case).
                               Do you like {}? """.format(item))).lower()
            fruits3_copy = yes_no(query, item, fruits3_copy)
        item_flag.append(item) #list of fruits already checked
    print(fruits3_copy)



def yes_no(YN_query, YN_item, YN_fruits3_copy): #eliminates some repetition in Series3
    if YN_query == 'no':
        while YN_item in YN_fruits3_copy:
            YN_fruits3_copy.remove(YN_item)
    elif YN_query == 'yes':
        pass
    return YN_fruits3_copy



def Series4():
    """
    This is Series 4

    Make a new list with the contents of the original, but with all the letters in each item reversed.
Delete the last item of the original list. Display the original list and the copy.
"""

    fruits4 = ask() #call function to take default list or execute Series1

    fruits4_copy = fruits4[:]
    for i, item in enumerate(fruits4):
        item_copy = list(item)
        item_copy.reverse()
        item_copy = "".join(item_copy)
        fruits4_copy[i] = item_copy
    fruits4_copy.pop()
    print('original=',fruits4,'\n','copy=',fruits4_copy)
