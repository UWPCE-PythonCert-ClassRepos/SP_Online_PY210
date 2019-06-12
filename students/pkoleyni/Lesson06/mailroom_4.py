#!/usr/bin/env python3
import datetime
import sys

donor_list_dic = {'pooria koleyni': {'donation': [130]},
                  'john adams': {'donation': [200, 340, 560]},
                  'steve knot': {'donation': [50, 130]},
                  'meru cheng': {'donation': [150, 430]},
                  'maysam razm': {'donation': [25, 25]}
                  }


def check_add_name(name):
    """
    :param name: name of a donor to be added to the donor_list_dic of donors if not already there
                This function first verifies to see if name is not already in the donor_list_dic
                Then it will add name to the donor_list_dic dictionary

    """

    if name not in donor_list_dic:
        print('\"{}\" is not in the list of the donors, Adding to the list of donors'.format(name))
        donor_list_dic[name] = {'donation': []}
    else:
        print('{} is already in the list of donors'.format(name))


def donation_list(name):
    """
    :param name: name of a donor
    :return: list of all the donation made by a donor
    """
    return donor_list_dic[name]['donation']


def add_donation(name, donation):
    """
    :param name: name of a donor
    :param donation: amount of donation made
    :return:
    """
    donation_list(name).append(donation)
    update_total_donation_to_dic(name)


def update_total_donation_to_dic(name):
    total_given = sum(donation_list(name))
    donor_list_dic[name]['total_donation'] = total_given


def thank_you():
    """
    This function is taking care of the required actions when user select thank you from the menu
    :return:
    """
    usr_name_input = input('Enter full name of a donor or enter \"List\" for complete list of doors > ')
    while usr_name_input == 'List':
        print("\n".join(list(donor_list_dic)))
        usr_name_input = input('Enter full name of a donor or enter \"List\" for complete list of doors > ')
    check_add_name(usr_name_input)
    usr_donation_input = input('Enter a donation amount > ')
    try:
        usr_donation_input = int(usr_donation_input)
    except ValueError:
        print('ValueError: {} is a {}, Enter a digit for donation value'.format(usr_donation_input,type(usr_donation_input)))
    else:
        add_donation(usr_name_input, usr_donation_input)
        thank_you_message(usr_name_input, usr_donation_input)


def thank_you_message(name, donation):
    """
    :param name: name of a donor to send thank you letter
    :param donation: Amount of donation
    :return:
    """
    print()
    print("Thank you letter for {}".format(name))
    print('=' * 50)
    print("Dear {}".format(name))
    print("We r eceived your {} donation".format(donation))
    print("Thank you for your donation\n")


def sort_key(key):
    """

    :param key: Key defines the item in the list to be used for sorting
    :return:
    """
    return key[1]


def report():
    """

    :return: This function created new list with the items required in the report, sort the list and print the report
    """

    report_list = []
    for donor in donor_list_dic.keys():
        total_given = sum(donation_list(donor))
        num_of_gifts = len(donation_list(donor))
        average_gifts = total_given / num_of_gifts
        report_list.append([donor, total_given, num_of_gifts, average_gifts])
    sorted_report_list = sorted(report_list, key=sort_key, reverse=True)

    report_head = ("{:<20}{:<20}{:<20}{:<20}".format('Donor Name', '| Total Given', '| Num Gifts ', '| Average Gift'))
    print(report_head)
    print('-' * (len(report_head)))
    for item in sorted_report_list:
        print('{:<21}{:<21}{:<21}{:<21.2f}'.format(item[0], item[1], item[2], item[3]))


def send_letter_to_all():
        write_letter_to_file('pooria koleyni')


def file_name(name):
    """

    :param name: name of a donor
    :return: string that will be be used as file_name for thank you letter file
    """
    d = datetime.datetime.today()
    return name + '_{}_{}_{}'.format(d.year, d.month, d.day) + '.txt'


def write_letter_to_file(name):
    last_donation = donation_list(name)[-1]
    line1 = 'Dear {},\n'.format(name)
    line2 = '\tThank you for your very kind donation of ${:.2f}.\n'.format(last_donation)
    line3 = '\tIt will be put to very good use.\n'
    line4 = '\tSincerely,\n\t     -The Team'

    file = file_name(name)
    with open(file, 'w') as f:
        f.write(line1.format(name))
        f.write(line2.format(name))
        f.write(line3.format(name))
        f.write(line4.format(name))
    print('Letter for "{}" is saved to "{}"'.format(name, file))


def write_letter_for_everyone():
    """
    Get name of each donor from the donor_list_dic dictionary and call write_letter_to_file() function.
    :return:
    """
    for donor in donor_list_dic.keys():
        write_letter_to_file(donor)


def quit():
    sys.exit()


def menu_selection():
    """
    Display Main menu, Using a Dictionary to switch
    :return:
    """
    main_prompt = """
    Select from the following options:\n
    1. Send a Thank You to a single donor.
    2. Create a report
    3. Send letters to all donors.
    4. Quit
    """
    main_menu_dic = {'1': thank_you,
                     '2': report,
                     '3': write_letter_for_everyone,
                     '4': quit
                     }
    while True:
        try:
            response = input(main_prompt)
            if main_menu_dic[response]() == "quit":
                break
        except KeyError:
            print ("{} is not a valid option".format(response))


if __name__ == '__main__':
    menu_selection()