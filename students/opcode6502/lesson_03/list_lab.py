# list_lab.py
# opcode6502: SP_Online_PY210


def main():

    # - - Series 1 - - - - - -
    # REQ-01: Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
    fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]

    # REQ-02: Display the list (plain old print() is fine…).
    print(fruit_list)

    # REQ-03: Ask the user for another fruit and add it to the end of the list.
    fruit_list.append(input("[ INPUT ]: Please enter a [ fruit ]: "))

    # REQ-04: Display the list.
    print(fruit_list)

    # REQ-05: Ask the user for a number and
    # display the number back to the user and
    # the fruit corresponding to that number (on a 1-is-first basis).
    # Remember that Python uses zero-based indexing, so you will need to correct.

    # TO-DO: Add input sanitization and exception handling.
    user_number = input("[ INPUT ]: Please enter a [ number ]: ")
    index = int(user_number)
    print(fruit_list[index-1])

    # REQ-06: Add another fruit to the beginning of the list using “+” and display the list.
    fruit_list = ['Blueberry'] + fruit_list
    print(fruit_list)

    # REQ-07: Add another fruit to the beginning of the list using insert() and display the list.
    fruit_list.insert(0, 'Grape')
    print(fruit_list)

    # REQ-08: Display all the fruits that begin with “P”, using a for loop.
    for fruit in fruit_list:
        if fruit[0]=="P":
            print("[ DEBUG ]: Fruit: " + fruit)

    # - - Series 2 - - - - - -
    # Using the list created in series 1 above:

    # REQ-09: Display the list.
    print(fruit_list)

    # REQ-10: Remove the last fruit from the list.
    fruit_list.pop()

    # REQ-11: Display the list.
    print(fruit_list)

    # REQ-12: Ask the user for a fruit to delete, find it and delete it.
    # (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
    fruit_to_be_deleted = input("[ INPUT ]: Please enter a fruit to remove: ")
    fruit_list.remove(fruit_to_be_deleted)

    # - - Series 3 - - - - - -
    # Again, using the list from series 1:

    # REQ-13: Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
    # REQ-14: For each “no”, delete that fruit from the list.
    # REQ-15: For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
    for fruit in fruit_list:
        print(fruit)
        print("Do you like {}? ".format(fruit.lower()))
        # TO-DO: Add input sanitization and exception handling.
        user_response = input("Yes or No: ")
        if user_response == 'no':
            print(fruit)
            fruit_list.remove(fruit)

    # REQ-16: Display the list.
    print(fruit_list)

    # - - Series 4 - - - - - -
    # Once more, using the list from series 1:

    # REQ-17: Make a new list with the contents of the original
    reverse_fruits_list = []

    # REQ-18: but with all the letters in each item reversed.
    for fruit in fruit_list:
        reverse_fruits_list.append(fruit[::-1])

    # REQ-19: Delete the last item of the original list.
    fruit_list.pop()

    # REQ-20: Display the original list
    print(fruit_list)

    # REQ-21: and the copy.
    print(reverse_fruits_list)


if __name__=='__main__':
    main()
