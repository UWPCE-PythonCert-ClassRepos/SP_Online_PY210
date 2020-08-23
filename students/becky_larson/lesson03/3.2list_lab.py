#!/usr/bin/env python3
"""Done except for the bonus """


def ask_user(question):
    print('question asked is ', question)
    response = input(question)
    return response


def add_fruit(fruits, new_fruit):
    new_fruits = list(fruits)
    new_fruits.append(new_fruit)
    return new_fruits


def get_number(length):
    response = int(0)
    updated_q = "Enter a number less than " + str(length) + " > "
    response = input(updated_q)
    # belarson text this and check the number entered
    return response


def add_fruit_with_insert(fruit_list, fruit):
    fruit_list.insert(0, fruit)
    return fruit_list


def display_fruits_starting_with(fruit_list, starting_letter):
    print("Fruits starting with letter ", starting_letter)
    for item in fruit_list:
        if(item[0] == starting_letter):
            print(item)


def series1(fruit_list):
    print('1 series1 starting List: ', fruit_list)

    """Ask  user for another fruit and add it to the end of the list."""
    new_fruit = ask_user("Enter name of fruit to add > ")
    updated_fruit = add_fruit(fruit_list, new_fruit)

    """Display the list."""
    print('2 Updated List: ', updated_fruit)

    """Ask  user for a number """
    """Display number and fruit for  number"""
    num_in = get_number(len(updated_fruit))
    text = "Fruit number {num} is {fruit}"
    the_display = text.format(num=num_in, fruit=updated_fruit[(int(num_in)-1)])
    print("3 " + the_display)

    """Add another fruit to beginning of list using “+” . Display list."""
    updated_with_plus = ['Lemons'] + updated_fruit
    print("4")
    print(updated_with_plus)

    """Add another fruit to beginning of list using insert(). Display list"""
    updated_with_insert = add_fruit_with_insert(updated_with_plus, 'Mango')
    print("5")
    print(updated_with_insert)

    """Display all fruits that begin with “P”, using a for loop"""
    display_fruits_starting_with(updated_with_insert, 'P')
    print('Final List: ', updated_with_insert)
    return updated_with_insert


def do_series2_bonus(doubledList):
    print('do_series2_bonus Starting List: ', doubledList)
    deleteFruit = ask_user("Enter name of fruit to delete for Bonus > ")
    print('do_series2_bonus delete fruit: ', deleteFruit)
    if deleteFruit in the_list:
        print(deleteFruit, " was found in List")
#        the_list.remove(deleteFruit)
    else:
        print(deleteFruit, " was not found in List")


def series2(the_list):
    print('Series 2 Starting List: ', the_list)
    '''Remove last fruit from list.  Display updated list'''
    the_list.pop()
    print('After removing the last fruit: ', the_list)

    '''Ask user for fruit to delete, find and delete it.'''
    deleteFruit = ask_user("Enter name of fruit to delete > ")
    print('Series 2 delete fruit: ', deleteFruit)
    if deleteFruit in the_list:
        print(deleteFruit, " was found in list and deleted")
        the_list.remove(deleteFruit)
    else:
        print(deleteFruit, " was not found in List")
    return the_list


def series3(the_list):
    # print('Series 3 Starting List: ', the_list)
    '''Ask user if they like each fruit (in lowercase)'''
    cnt = len(the_list)
    print('cnt ', cnt)
    
    for fruit in reversed(the_list):
        print('fruit ', fruit)
        question = "1 Do you like " + fruit.lower() + " (y or n) > "
        # print(lower(fruit))
        answer = ask_user(question)
        print('++++++++++++++++== answer ', answer)
        # For any answer that is not “yes” or “no”, 
        #    prompt user to answer with one of those two values 
        if not ((answer.lower() == 'n') or (answer.lower() == 'y')):
            valid = False
            while not valid:
                question = "Do you like " + fruit.lower() + " (y or n) > "
                answer = ask_user(question)
                if (answer == 'n') or (answer == 'y'):
                    valid = True
                    break
        else:
            # if they don't like, delete from list
            if(answer == 'n'):
                print('Delete ', fruit)
                the_list.remove(fruit)
            else:
                continue

    return the_list


def series4(the_list):
    # print('Series 4 Starting List: ', the_list)
    new_list = []
    for fruit in the_list:
        # print('fruit: ', fruit [::-1])
        new_list.append(fruit[::-1])
    the_list.pop()
    print('Original List: ', the_list)
    return new_list


fruit_tuple = ('Apples', 'Pears', 'Oranges', 'Peaches')
fruits_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
fruits_set = {'Apples', 'Pears', 'Oranges', 'Peaches'}
print(fruits_list)

series1_list = series1(fruit_tuple)
print('series1_list: ', series1_list)

series2_list = series2(series1_list)
print('series2_list: ', series2_list)
# #do_series2_bonus(series2_list*2)

series3_list = series3(series1_list)
print('series3_list: ', series3_list)

# series4_list = series4(series1_list)
# print('series3_list: ', series3_list)
'''
series3_list = series3(fruits_list)
print('series3_list: ', series3_list)
'''