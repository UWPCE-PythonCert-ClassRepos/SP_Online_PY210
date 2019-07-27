from donor_models import *

import datetime
import sys


db = DonorCollection()
db.add_donation('pooria', 100)


def thank_you():
    """
    This function is taking care of the required actions when user select thank you from the menu
    :return:
    """
    usr_name_input = input('Enter full name of a donor or enter \"List\" for complete list of doors > ')
    if usr_name_input == 'List':
        print("\n", db.list_of_donors)
        usr_name_input = input('Enter full name of a donor or enter \"List\" for complete list of doors > ')

    if usr_name_input in db.list_of_donors:
        donation = input('Donor \"{}\" already exists, add new donation ...'.format(usr_name_input))
    else:
        print("{} is not in the list of donors,Adding {} to the list".format(usr_name_input, usr_name_input))
        donation = input('Enter Donation amount ...')
    db.add_donation(usr_name_input, int(donation))

    thank_you_message(usr_name_input, donation)

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


def report():
    report_list = []
    for donor in db.donor_dic.keys():
        report_list.append([db.donor_dic[donor].name, db.donor_dic[donor].max_donation, db.donor_dic[donor].num_of_donation, db.donor_dic[donor].avr_donation])

    sorted_report_list = sorted(report_list, key=DonorCollection.sort_key, reverse=True)
    report_head = ("{:<20}{:<20}{:<20}{:<20}".format('Donor Name', '| Total Given', '| Num Gifts ', '| Average Gift'))
    print(report_head)
    print('-' * (len(report_head)))
    for item in sorted_report_list:
        print('{:<21}{:<21}{:<21}{:<21.2f}'.format(item[0], item[1], item[2], item[3]))
    print('-' * (len(report_head)))


def file_name(name):
    """

    :param name: name of a donor
    :return: string that will be be used as file_name for thank you letter file
    """
    d = datetime.datetime.today()
    return name + '_{}_{}_{}'.format(d.year, d.month, d.day) + '.txt'


def write_letter_to_file(name):
    line1 = 'Dear {},\n'.format(name)
    line2 = '\tThank you for your very kind donation'
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
    for donor in db.list_of_donors:
        write_letter_to_file(donor)

def quit():
    sys.exit()

def main_menu():

    while True:
        prompt = input("""Select from the following options
        1: Send a Thank You
        2: Create a Report
        3: Send letters to all donors
        4: Quit
        >>>""")
        main_menu_dic = {'1': thank_you,
                         '2': report,
                         '3': write_letter_for_everyone,
                         '4': quit
                         }

        try:
            main_menu_dic[prompt]()
        except KeyError:
            print("Invalid selection\n")
            continue


if __name__ == "__main__":
    main_menu()


