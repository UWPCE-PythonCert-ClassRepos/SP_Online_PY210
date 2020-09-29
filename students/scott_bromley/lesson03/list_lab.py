#!/usr/bin/env python3

# instructions:
# create a list that contains "Apples", "Pears", "Oranges", and "Peaches"
# display the list
# ask the user for another fruit and add it to the end of the list
# display the list
# ask user for a number, display number back to user and the fruit corresponding to number (1-is-first basis)
# add another fruit to the beginning of the list using "+" and display the list
# add another fruit to the beginning of the list using insert() and display the list
# display all the fruits that begin with "P" using a for loop


def main():
    series_one()
    series_two()
    series_three()
    series_four()


def series_one():
    '''
    creates and displays list of fruits and interacts w/ user to change list
    :return: list created from instructions
    '''

    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    print_list(fruits)

    fruit = get_user_input("Please enter a fruit to add to the list > ")
    fruits.append(fruit.capitalize())
    print_list(fruits)

    fruit_no = get_user_input("Please enter the number of the fruit to display > ")
    print(f"You chose the number {fruit_no}: {fruits[int(fruit_no) - 1]}")

    fruits = ["Raspberries"] + fruits
    print_list(fruits)

    fruits.insert(0, "Quince")
    print_list(fruits)

    print_list([item for item in fruits if item.startswith('P') is True])

    return fruits


def series_two():
    '''
    use list from series_one; remove last item in that list; display list; ask user for fruit to delete, delete fruit
    :return: list from series_one w/ last item removed and user-selected item removed
    '''
    fruits = series_one()
    del fruits[-1]
    print_list(fruits)
    fruit_delete = get_user_input("Enter the name of the fruit you wish to remove > ")
    fruits.remove(fruit_delete)
    print_list(fruits)
    return fruits


def series_three():
    '''
    use series_one list and delete fruits user does not like; display list
    '''
    fruits = series_one()
    for item in fruits[:]:
        while True:
            response = get_user_input(f"Do you like {item.lower()}? ").casefold()
            if response == "no":
                fruits.remove(item)
                break
            elif response == "yes":
                break
            else:
                print("Please only enter 'yes' or 'no'")
                continue

    print_list(fruits)
    return None


def series_four():
    '''
    use series_one list, make copy of list, reverse letters in each fruit in copy, delete last item of original list,
    display original list and copy
    :return: None
    '''

    fruits = series_one()
    fruits_copy = fruits[:]
    fruits_copy = [item[::-1] for item in fruits_copy]
    del fruits[-1]
    print_list(fruits)
    print_list(fruits_copy)
    return None


def get_user_input(prompt):
    '''
    :param prompt: prompt for user to respond to
    :return: response to question/prompt
    '''
    response = input(prompt).strip()
    return response


def print_list(display_list):
    '''
    :param display_list:
    :return: prints display_list
    '''
    if display_list is None:
        display_list = []
    print(f"{' '.join(item for item in display_list)}")
    return None


if __name__ == "__main__":
    print("Running", __file__)
    main()
else:
    print("Running %s as imported module", __file__)