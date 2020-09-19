fruits_list = ["pineapple", "zucchini", "apple", "banana", "cucumber", "potato",
               "lettuce", "salad", "zest", "orange", "jalapino", "yellow_fruit", "star_fruit"]


def start_series_one():
    _continue = input(
        "Would you like to add another fruit to the list (y/n)? ")
    if _continue == "y" or _continue == "Y":
        series_one_add()
    else:
        _search = input(
            "Would you like to search for a fruit instead? (y/n)? ")
        if _search == "y" or _search == "Y":
            series_one_search()
        else:
            print("Program ended. Thank you")


def series_one_add():
    _front_bool = input(
        "Would you like to insert the fruit to the front or the back of the list?  ")
    if _front_bool == "front" or _front_bool == "Front" or _front_bool == "f" or _front_bool == "F":
        print(fruits_list)
        add_fruit = input(
            "Which fruit would you like to add to the front of the list? ")
        fruits_list.insert((add_fruit))
        print(fruits_list)
        start_series_one()
    else:
        print(fruits_list)
        add_fruit = input(
            "Which fruit would you like to add to back of the list? ")
        fruits_list.append((add_fruit))
        print(fruits_list)
        start_series_one()


def series_one_search():
    print(fruits_list)
    _search_method = input(
        "Please search by index location, or by first letter of fruits name...  ")
    if int(_search_method):
        if 0 <= int(_search_method) <= len(fruits_list):
            index = int(_search_method)
            if fruits_list[index]:
                print(fruits_list[index])
                series_one_search()
            else:
                print("Sorry, that fruit index does not exist. Please try again... ")
                series_one_search()
        else:
            print("Sorry, that index is out of the range of the list.")
            series_one_search()
    else:
        print(_search_method[0])
        if fruits_list[_search_method[0]]:
            print(fruits_list[_search_method[0]])
        else:
            print(
                "Sorry, that first letter of fruit does not exist. Please try again... ")
            series_one_search()


# start_series_one()


def series_two():
    letter = input(
        "Please insert letter you wish to find first letter of fruit within contained list (ie: a == apple; b == banana):   ")
    for i in fruits_list:
        if i[0] == letter:
            print(i)
    series_two()

# works
# series_two()


def series_three():
    for i in fruits_list:
        question = input(f"Do you like {i}; 'yes' or 'no'...   ")
        if question.lower() in ("no", "n"):
            fruits_list.remove(i)
            print("You don't like {i}... deleted!")
            print(fruits_list)
        elif question.lower() in ("yes", "y"):
            print(f"You like {i}, good to know!")
        else:
            print("You didn't follow directions... start again!")
            series_three()

# Works
# series_three()


def series_four():
    i = 0
    delete_last = input(
        "Would you like to delete first and last item from list while we reverse order of all items?  ")
    if delete_last.lower() in ("Yes", "y"):
        while i < len(fruits_list[1: -1]):
            print(fruits_list[1 + i][::-1])
            i += 1
    else:
        while i < len(fruits_list):
            print(fruits_list[i][::-1])
            i += 1
    series_four()


series_four()
