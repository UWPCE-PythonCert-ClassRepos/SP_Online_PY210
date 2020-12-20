#!/usr/bin/env python3
# Mailroom Part 4

import sys

donors = {"Bill Gates": [539000, 235642],
          "Jeff Bezos": [108356, 204295, 897345],
          "Satya Nadella": [236000, 305352],
          "Mark Zuckerberg": [153956.35],
          "Mark Cuban":[459035, 369.50, 570.89]}

prompt = "\n".join(("Please Select from Items Below:",
                    "1 - Send A Thank You",
                    "2 - Create A Report",
                    "3 - Send Letters to All Donors",
                    "4 - Quit",
                    " "))

def donor_verify(donor_name, amount, donor_list):
    # Donor name found in list. Add amount to entry.
    if donor_name in donor_list:
          donors[donor_name].append(amount)
          print('\n')

    # not found in list. Add new donor entry
    else:
        new_entry = []
        new_entry.append(amount)
        donors[donor_name] = new_entry

    return donors

def thank_you_note(donor_name, amount):

    thanks_dict = {'donor_name': donor_name, 'amount': amount}

    # Formatted Thank You Note
    message = ('Dear {donor_name}, \n\nThank you for your show of support and generosity. '
      'Your Donation of ${amount} will contribute to saving Olympic Marmots '
      'in Washington State. These Marmota are special and a unique gift to the Olympic '
      'National Park ecosystem. As a way of saying thank you. '
      'You will be receiving your very own Olympic Marmot t-shirt in the mail!\n\n'
      'Sincerely,\n\nThe Olympic Marmot Wildlife Foundation\n').format(**thanks_dict)

    return message

def send_thanks():
    print('\n', "For A Complete Donor List Type 'List'\n ")

    # Create a unique list of donor names
    donor_list = [names for names in donors.keys()]

    while True:
        donor_name = input("What donor(s) are you looking for?\n ").title()
        if donor_name == 'List':
            print('\n', "Here is A Complete List of Donor Names\n ")
            print(donor_list)
        else:
            break

    # prompt for donation amount
    try:
        amount = float(input("How Much Did This Person Donate?\n "))

    except ValueError: #start prompt over again if exception occurs
        print('Please input the amount donated')
        send_thanks()

    # updates donor database by checking existing donors and adding new ones if they don't exist
    donor_verify(donor_name, amount, donor_list)

    # formats message thanking the individual donor
    message = thank_you_note(donor_name, amount)

    print(message)

# function for sorting key
def sum_value(donations):
    item = donations[1]
    return sum(item)

def report_rows(name, amounts):
    total_given = sum(amounts)
    num_gift = len(amounts)
    avg_gift = total_given/num_gift

    total_given = '{:,.0f}'.format(total_given)
    avg_gift = '{:,.0f}'.format(avg_gift)
    row = '{:<25}${:^15}{:^15}${:^15}'.format(name, total_given, num_gift, avg_gift)

    return row

def print_report(report_lines):
    '''
    Prints the output of the donor report using data generated from report_rows function & report_lines list
    '''
    # prints the header of the report
    print('{:<25}{}{:^15}{}{:^15}{}{:^15}'.format('Donor Name', '|', 'Total Given', '|', 'Num Gifts', '|', 'Average Gift'))
    str_len = len('{:<25}{}{:^15}{}{:^15}{}{:^15}'.format('Donor Name', '|', 'Total Given', '|', 'Num Gifts', '|', 'Average Gift'))
    print('-' * str_len)

    # prints name, total, num of gifts, and avg gift
    for row in report_lines:
        print(row)

def create_report():
    '''
    Creates the data used in donor reports
    '''
    # create a sorted donations dict by total amount
    sorted_donations = sorted(donors.items(), key = sum_value, reverse=True)

    report_lines = []

    for k, v in sorted_donations:
        report_lines.append(report_rows(k, v))

    print_report(report_lines)

def write_file(name, message):
    '''
    Creates a text file of each thank you message for each donor
    '''
    fname = name + '.txt'
    with open(fname, 'w') as f:
        f.write(message)

def create_message(name, amount):
    '''
    Creates a personalized & formatted message for each donor
    '''
    tmt_amount = sum(amount)

    message = ('Dear {}, \n\nThank you for your show of support and generosity. '
        'Your donations of ${:,.1f} will contribute to saving Olympic Marmots '
        'in Washington State. These Marmota are special and a unique gift to the Olympic '
        'National Park ecosystem. As a way of saying thank you. '
        'You will be receiving your very own Olympic Marmot t-shirt in the mail!\n\n'
        'Sincerely,\n\nThe Olympic Marmot Wildlife Foundation\n').format(name, tmt_amount)

    return message

def send_letters():
    '''
    creates and writes a letter to each donor in the donor database
    '''
    for name, amount in donors.items():

        message = create_message(name, amount)

        write_file(name, message)

def exit_from():
    print('Work Completed. Good Bye!')
    sys.exit()

response_dict = {"1": send_thanks, "2": create_report, "3": send_letters, "4": exit_from}

def main():
    while True:
        try:
            response = input(prompt)
            response_dict.get(response)()

        except TypeError:
            print('The choice you have selected is not an option. Please select from the menu.')
            continue

if __name__ == "__main__":
    main()
