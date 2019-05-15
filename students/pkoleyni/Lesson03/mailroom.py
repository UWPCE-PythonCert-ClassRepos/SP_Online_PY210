#!/usr/bin/env python3

donor_list = [['pooria koleyni',1000,250],['john adams',250,400,330],['steve knot',1400],['meru cheng',1300,4200],['maysam razm',100,420]]


def list_donors():
    """
    :return: This function will return list of name of the donors
    """
    name_of_donors = []
    for i in range(0,len(donor_list)):
        name_of_donors.append(donor_list[i][0])
    return name_of_donors

def print_name_of_donors(list_donors):
    """

    :param list_donors: This is the list of name of the donors
    :return:
    """
    print("Name of donor:\n", "-" * 15)
    for i in range(0, len(list_donors())):
        print("\t", list_donors()[i])

def check_input(option):
    """

    :param option: Option is the user input to select from the options
    :return: True if user input is 1 or 2 or 3, False if user input is something else
    """
    if option == '1' or option == '2' or option =='3':
        return True
    elif option =='3':
        exit()
    else:
        return False

def check_add_name(donor_list, name):
    """

    :param donor_list: list of name of donors
    :param name: name of a existing donor or new donor
    :return: If name is not in the list of donors add it to the list
    """
    if name not in list_donors():
        print('\"{}\" is not in the list of the donors, Adding to the list of donors'.format(name))
        donor_list.append([name])
    else:
        print('{} is already in the list of donors'.format(name))


def add_donation(name, donation):
    """

    :param name: name of a donor
    :param donation: amount of donation
    :return: add donation to the list and print a message to confirm donation has been added to the list
    """
    for i in range(0, len(donor_list)):
        if donor_list[i][0] == name:
            donor_list[i].append(donation)
            print ("${} added to the list of donations made by {} donations".format(donation,name))


def thank_you():
    """
    This function is taking care of the required action when user select thank you from the menu
    :return:
    """
    usr_input = input('Enter full name of a donor or enter \"List\" for complete list of doors > ')
    while usr_input == 'List':
        print_name_of_donors(list_donors)
        usr_input = input('Enter full name of a donor or enter \"List\" for complete list of doors > ')
    check_add_name(donor_list, usr_input)
    usr_donation_input = input('Enter a donation amount > ')
    add_donation(usr_input, int(usr_donation_input))
    thank_you_message(usr_input, usr_donation_input)

def thank_you_message(name,donation):
    """
    :param name: name of a donot to send thank you letter
    :param donation: Amount of donation
    :return:
    """
    print()
    print("Thank you letter for {}".format(name))
    print('=' * 50)
    print("Dear {}".format(name))
    print("We received your {} donation".format(name, donation))
    print("Thank you for your donation\n")


def total_donation(name):
    """

    :param name: name of a donor
    :return: will return total donation made by a donor
    donor_donation[1:] is list of all the donation made by a donor
    """
    total = 0
    for donor_donation in donor_list:
        if name in donor_donation:
            for donation in donor_donation[1:]:
                total = total + donation
    return total

def num_gifts(name):
    """

    :param name: is name of a donor
    :return: will return total number of gifts from a donor
    """
    for donor_donation in donor_list:
        if name in donor_donation:
            total_num_gifts = len(donor_donation[1:])
    return total_num_gifts

def average_gifts(name):
    for donor_donation in donor_list:
        if name in donor_donation:
            avarage = sum(donor_donation[1:]) / len(donor_donation[1:])
    return avarage

def report():
    """

    :return: will call other function to get the data and print the report
    """
    print()
    report_head = ("{:<20}{:<20}{:<20}{:<20}".format('Donor Name','| Total Given', '| Num Gifts ', '| Average Gift' ))
    print (report_head)
    print ('-'*(len(report_head)))
    for donor_name in list_donors():
        print(f"{donor_name:<20}{total_donation(donor_name):<20f}{num_gifts(donor_name):<20f}{average_gifts(donor_name)}")

def display_options():
    user_input = ''
    while user_input != '3':
        print("Select from the following options:")
        print("-" * 50, "\n")
        print("\t1. \"Send a Thank You\"")
        print("\t2. \"Create a Report\"")
        print("\t3. \"Quit\"\n")
        user_input = input("Enter here > ")
        while not check_input(user_input):
            print("Not a valid option, please select/enter 1,2, or 3 >")
            user_input = input("Enter here > ")
        if user_input == '1':
            thank_you()
        if user_input == '2':
            report()
        if user_input == '3':
            exit()

if __name__ == '__main__':
    display_options()






