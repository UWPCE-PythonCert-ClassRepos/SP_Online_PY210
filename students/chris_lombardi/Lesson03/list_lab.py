#UWPCE PY210
#Lesson03, List Lab

#!/usr/bin/env python3

def series_1():
    print('{}Series 1{}'.format('-'*6,'-'*6))
    l1 = ['Apples', 'Pears', 'Oranges', 'Peaches']
    print(l1)
    fruit_add = input("Enter a new fruit to add to the list.")
    l1.append(fruit_add.title())

    #Print the value at the user entered index.
    num = int(input("Enter a number between 1 and " + str(len(l1))))
    #Test to make sure user entry is within range.
    while num > len(l1):
        print("The number is out of the range.")
        num = int(input("Enter a number between 1 and " + str(len(l1))))
    print(str(num) + ": " + l1[num-1])

    #Add a new fruit to the list using the + operand.
    print("Adding 'Strawberries' to the list.")
    l2 = ['Strawberries']
    l1 = l2 + l1
    print(l1)

    #Add a new fruit to the list using insert().
    print("Adding 'Grapefruits' to the list.")
    item = 'Grapefruits'
    l1.insert(0, item)
    print(l1)

    #Display all fruits containing a 'P'.
    print("Displaying all fruits containg a 'P':")
    for fruit in l1:
        if 'p' in fruit.lower():
            print(fruit.title())

    return l1

def series_2(list_test):
    print('{}Series 2{}'.format('-'*6,'-'*6))
    l2 = list_test[:]
    print(l2)
    del l2[-1:]
    print(l2)

    user_value = input('What fruit would you like to delete?')
    for fruit in l2:
        if user_value.lower() == fruit.lower():
            l2.remove(user_value.title())
    print(l2)

    #Series 2 Bonus
    print('{}Series 2 Bonus{}'.format('-'*6,'-'*6))
    list_doubled = l2 * 2
    print(list_doubled)
    #Keep asking for input until the user entered value is in the list.
    user_value = input('Enter a fruit to delete.')
    while user_value.title() not in list_doubled:
        print('The fruit you entered is not in the list.')
        user_value = input('Enter a fruit to delete.')
    while user_value.title() in list_doubled:
        list_doubled.remove(user_value.title())

    print(list_doubled)

def series_3(list_test):
    print('{}Series 3{}'.format('-'*6,'-'*6))
    l3 = list_test[:]
    print(l3)
    for fruit in list_test:
        print(fruit) #Test Line DELETE
        response = input('Do you like ' + fruit.lower() + '?')
        while response.lower() not in ('yes', 'no'):
            print('Please enter either "Yes" or "No"')
            response = input('Do you like ' + fruit.lower() + '?')
        if response.lower() == 'no':
            l3.remove(fruit)

    print(l3)

def series_4(list_test):
    print('{}Series 4{}'.format('-'*6,'-'*6))
    l4 = list_test[:]
    print(l4)
    for i, fruit in enumerate(l4):
        fruit_rev = fruit[::-1]
        l4[i] = fruit_rev

    print("Original list with last fruit removed:")
    del list_test[-1:]
    print(list_test)
    print("Original list with letter's reversed:")
    print(l4)

def main():
    list_test = series_1()
    series_2(list_test)
    series_3(list_test)
    series_4(list_test)

main()