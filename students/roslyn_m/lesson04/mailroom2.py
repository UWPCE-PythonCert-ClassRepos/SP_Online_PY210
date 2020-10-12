#!/usr/bin/env python3
# Title: Mailroom Part 2 (Lesson 4)
# Dev: Roslyn Melookaran
# Date: 10/2/20
# Change Log: (Who, When, What)
# R. Melookaran, 10/2/20, created script)
# --------------------------------------------------------------

# ----------Functions----------#


def options_menu():
    """ Show menu of options to user.
            :return: nothing
            """
    print("\nMenu of actions:" + '\n \t1) Send a Thank You \n \t2) Create a report \n \t3) Create Thank You files for all donors \n \t4) Quit\n')
    return


def option_input():
    """ Gather input from user on what action they want.
                :return: user_selection (string)
                """
    user_selection = input('Please select option 1-3: ')
    return user_selection


def thank_you_note(donor_all):
    """ User will be prompted for a Full Name.
            -If the user type list show them a list of the donor names and re-prompt.
            -If the user types a name not in the list, it will be added to data structure and used
            -If the user types a name in the list, it is used.
        -Once a name has been selected, user will be prompted for a donation amount to be added to donation history
        -Thank you note will be generated
                  :param: donor_all (list of lists)
                  :return: donor_all (list of lists)
                  """
    user_input = input(
        'Please type the FULL NAME of the donor who you would like to write a thank you note to. If you would like to see a complete donor list, type "list": ')
    existing = False
    while user_input.title() == "List":
        for person in donor_all:
            print(person)
        user_input = input(
            'Please type the FULL NAME of the donor who you would like to write a thank you note to. If you would like to see a complete donor list, type "list": ')
    for person in donor_all:
        for item in person:
            if user_input.title() == item:
                donation_amt = float(input("Please enter the donation amount: "))
                person["Total"] = person["Total"] + donation_amt
                person["Qty"] = person["Qty"] + 1
                person["Avg"] = round(person["Total"] / person["Qty"], 2)
                existing = True
                person_to_thank = person
    if existing != True:
        donation_amt = float(input("Please enter the donation amount: "))
        person_add = {"Name": user_input.title(), "Total": donation_amt, "Qty": 1, "Avg": donation_amt}
        donor_all.append(person_add)
        person_to_thank = person_add
    print("The following thank you note will be emailed to the donor: ")
    print(
        '"Dear {}, \n Thank you so much for your gracious donation of ${:.2f}. We are so thankful for your strong support!! \nCheers,\nRoslyn Melookaran"'.format(
            person_to_thank["Name"], donation_amt))


def create_report(donor_all):
    """ Create a report of donors to show user.
                :param: donor_all (list of list)
                :return: nothing
                """
    title = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    print(f'{title[0]:20}|{title[1]:^12}|{title[2]:^10}|{title[3]:^14}|')
    print("-" * 60)
    for person in donor_all:
        print(f'{person["Name"]:20} ${person["Total"]:^12}{person["Qty"]:9}   ${person["Avg"]:^12}')
    print("\n")


def order_list(donor_all):
    """ Sort list of donors by donation amount total.
            :param: donor_all (list of list)
            :return: sorted_list (list of lists)
            """
    sorted_list = sorted(donor_all, key=lambda x: -(x["Total"]))
    return sorted_list


def send_all_thank_you(donor_all):
    """ Function will print a .txt file thank you note for each donor in list
            :param: donor_all (list of lists)
            :return: nothing
            """
    for person in donor_all:
        string = "Dear {Name}, \n\n \t Thank you so much for your support! You have donated a total of ${Total}, which is so very appreciated. We hope to have your continued support through these times. \n\nThanks, \nRoslyn".format(**person)
        print(string)
        filename = person["Name"]
        filename = filename.replace(" ", "")
        filename = filename + ".txt"
        with open(filename, 'w') as f:
            f.write(string)
    return


# ----------Variables----------#
person1 = {"Name": 'William Gates', "Total": 653784.49, "Qty": 2, "Avg": 326892.24}
person2 = {"Name": 'Mark Zuckerberg', "Total": 16396.10, "Qty": 3, "Avg": 5465.37}
person3 = {"Name": 'Jeff Bezos', "Total": 877.33, "Qty": 1, "Avg": 877.33}
person4 = {"Name": 'Paul Allen', "Total": 708.42, "Qty": 3, "Avg": 236.14}
person5 = {"Name": 'John Smith', "Total": 899.98, "Qty": 5, "Avg": 399.21}
donor_list = [person1, person2, person3, person4, person5]
user_input = ""
dict = {
    1: thank_you_note,
    2: create_report,
    3: send_all_thank_you
}

# ----------Main----------#
if __name__ == '__main__':
    options_menu()
    user_input = option_input()
    user_input = int(user_input)
    while user_input != 4:
        dict.get(user_input)(donor_list)
        options_menu()
        user_input = option_input()
        user_input = int(user_input)
    exit_input = input('Thanks for using the program. Hit enter to exit.')

