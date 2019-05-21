#!/usr/bin/env python3
import datetime

donor_list_dic = {'pooria koleyni': {'donation': [130]},
                  'john adams': {'donation': [200, 340, 560]},
                  'steve knot': {'donation': [50, 130]},
                  'meru cheng': {'donation': [150, 430]},
                  'maysam razm': {'donation': [25, 25]}
                  }


def list_donors():
    """
    Return list of name of donors by getting keys for the donor_list_dic dictionary
    :return:
    """
    donor_list = donor_list_dic.keys()
    return donor_list


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
        print(list_donors())
        usr_name_input = input('Enter full name of a donor or enter \"List\" for complete list of doors > ')
    check_add_name(usr_name_input)
    usr_donation_input = input('Enter a donation amount > ')
    add_donation(usr_name_input, int(usr_donation_input))
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
    print("We received your {} donation".format(donation))
    print("Thank you for your donation\n")


def sort_key(key):
    """

    :param key: Key defines the item in the list to be used for sorting
    :return:
    """
    return key[1]


def report():
    """

    :return: will call other function to get the data and print the report
    """

    report_head = ("{:<20}{:<20}{:<20}{:<20}".format('Donor Name', '| Total Given', '| Num Gifts ', '| Average Gift'))
    print(report_head)
    print('-' * (len(report_head)))
    for donor in list_donors():
        # sorted_report_list = sorted(report_list, key = sort_key, reverse = True)
        total_given = sum(donation_list(donor))
        num_of_gifts = len(donation_list(donor))
        average_gifts = total_given / num_of_gifts
        print('{:<21}{:<21}{:<21}{:<21.2f}'.format(donor, total_given, num_of_gifts, average_gifts))
    print(donor_list_dic)


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
        f.close()
    print('Letter for "{}" is saved to "{}"'.format(name, file))


def write_letter_for_everyone():
    for donor in list_donors():
        write_letter_to_file(donor)


def quit():
    print("Quitting the menu")
    return 'exit menu'


def menu_selection():
    main_prompt = """
    Select from the following options:\n
    1. Send a thank you
    2. Create a report
    3. Send_letter_to_all
    4. Quit

    """
    main_menu_dic = {'1': thank_you,
                     '2': report,
                     '3': write_letter_for_everyone,
                     '4': quit
                     }
    while True:
        response = input(main_prompt)
        if main_menu_dic[response]() == "exit menu":
            break


if __name__ == '__main__':
    # updating total donation made by each donor and add it to the dictionary
    for name in list_donors():
        update_total_donation_to_dic(name)
    menu_selection()
