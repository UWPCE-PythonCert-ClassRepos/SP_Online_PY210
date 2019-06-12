#!/usr/bin/env python3

def series1():
    # Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”
    l = ['Apples', 'Pears', 'Oranges', 'Peaches']
    # Display the list
    print(l)

    # Ask the user for another fruit and add it to the end of the list
    fruit = input('Enter another fruit > ')
    l.append(fruit)
    # Display the list
    print(l)

    # Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis)
    number = input('Enter a number > ')
    print(f'{number}. {l[int(number) - 1]}')

    # Add another fruit to the beginning of the list using “+” and display the list
    l = ['Watermelon'] + l
    print(l)

    # Add another fruit to the beginning of the list using insert() and display the list
    l.insert(0, 'Kiwi')
    print(l)

    # Display all the fruits that begin with “P”, using a for loop
    for item in l:
        if item[0] == 'P':
            print(item)

    return l

def series2(a_list):
    # Display the list
    print(a_list)

    # Remove the last fruit from the list and display the list
    a_list.pop()
    print(a_list)

    # Ask the user for a fruit to delete, find it and delete it
    fruit = input('Enter a fruit name > ')
    if fruit in a_list:
        a_list.remove(fruit)
    print(a_list)

    # Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences
    a_list *= 2
    print(a_list)
    fruit = input('Enter a fruit name > ')
    while fruit not in a_list:
        fruit = input('Enter a fruit name > ')
    while fruit in a_list:
        a_list.remove(fruit)
    print(a_list)

def series3(a_list):
    # Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase)
    for fruit in a_list[:]:
        answer = input(f'Do you like {fruit.lower()}?(yes/no) > ')
        # For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values
        while not (answer == 'yes' or answer == 'no'):
            answer = input(f'Do you like {fruit.lower()}?(yes/no) > ')
        # For each “no”, delete that fruit from the list
        if answer == 'no':
            a_list.remove(fruit)
    # Display the list
    print(a_list)

def series4(a_list):
    # Make a new list with the contents of the original, but with all the letters in each item reversed
    new_list = []
    for item in a_list:
        new_list.append(item[::-1])
    
    # Delete the last item of the original list
    a_list.pop()

    # Display the original list and the copy
    print(f'a_list = {a_list}')
    print(f'new_list = {new_list}')

if __name__ == "__main__":

    l1 = series1()

    series2(l1)

    series3(l1)

    series4(l1)
