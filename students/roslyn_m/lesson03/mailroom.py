#!/usr/bin/env python3
# Title: Mailroom Part 1 (Lesson 3)
# Dev: Roslyn Melookaran
# Date: 9/15/20
# Change Log: (Who, When, What)
# R. Melookaran, 9/15/20, created script)
# --------------------------------------------------------------
#----------Functions----------#
def options_menu():
    """ Show menu of options to user.
            :return: nothing
            """
    print("Menu of actions:"+'\n \t1) Send a Thank You \n \t2) Create a Report \n \t3) Quit')
    return
def option_input():
    """ Gather input from user on what action they want.
                :return: user_selection (string)
                """
    user_selection=input('Please select option 1-3:')
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
    user_input = input('Please type the FULL NAME of the donor who you would like to write a thank you note to. If you would like to see a complete donor list, type "list": ')
    existing = False
    while user_input.title() == "List":
        for person in donor_all:
            print(person)
        user_input = input('Please type the FULL NAME of the donor who you would like to write a thank you note to. If you would like to see a complete donor list, type "list": ')
    for person in donor_all:
        for item in person:
            if user_input.title() == item:
                donation_amt = float(input("Please enter the donation amount: "))
                person[1] = person[1] + donation_amt
                person[2] = person[2] + 1
                person[3] = round(person[1] / person[2], 2)
                existing = True
                person_to_thank = person
    if existing != True:
        donation_amt = float(input("Please enter the donation amount: "))
        person_add = [user_input.title(), donation_amt, 1, donation_amt]
        donor_all.append(person_add)
        person_to_thank = person_add
    print("The following thank you note will be emailed to the donor: ")
    print('"Dear {}, \n Thank you so much for your gracious donation of ${:.2f}. We are so thankful for your strong support!! \nCheers,\nRoslyn Melookaran'.format(person_to_thank[0], donation_amt))
def create_report(donor_all):
    """ Create a report of donors to show user.
                :param: donor_all (list of list)
                :return: nothing
                """
    title = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    print(f'{title[0]:20}|{title[1]:^12}|{title[2]:^10}|{title[3]:^142}|')
    print("-" * 60)
    for person in donor_all:
        print(f'{person[0]:20} ${person[1]:^12}{person[2]:9}   ${person[3]:^12}')
def order_list(donor_all):
    """ Sort list of donors by donation amount total.
            :param: donor_all (list of list)
            :return: sorted_list (list of lists)
            """
    sorted_list = sorted(donor_all, key=lambda x: -(x[1]))
    return sorted_list

#----------Variables----------#
person1=['William Gates',653784.49,2,326892.24]
person2=['Mark Zuckerberg',16396.10,3,5465.37]
person3=['Jeff Bezos',877.33,1,877.33]
person4=['Paul Allen',708.42,3,236.14]
person5=['John Smith',899.98,5,399.21]
donor_list=[person1,person2,person3,person4,person5]
user_input=""

#----------Main----------#
if __name__ == '__main__':
    options_menu()
    user_input=option_input()
    while user_input!='3':
        if user_input=='1':
            thank_you_note(donor_list)
        elif user_input == '2':
            donor_list = order_list(donor_list)
            create_report(donor_list)
        else:
            print('Your input was not valid...')
        options_menu()
        user_input = option_input()
    exit_input=input('Thanks for using the program. Hit enter to exit.')