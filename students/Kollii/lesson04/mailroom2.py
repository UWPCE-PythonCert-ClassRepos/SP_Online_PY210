#!/usr/bin/env python3

# Mailroom PART - 1
import sys


donor_dict = {'William Gates, III' : [653772.32, 12.17],
            'Jeff Bezos': [877.33],
            'Paul Allen': [663.23, 43.87, 1.32],
            'Mark Zuckerberg' : [1663.23, 4300.87, 10432.0]}


def options_menu():
    print("\n".join(("\nWelcome to the XYZ Charity!",
          "Please choose from below options:",
          "1 - Send a Thank you Note",
          "2 - Create a Report",
          "3 - Send Letters to All",
          "4 - Quit"
          ">>> ")))
    option = input('')
    return option


   
def send_thankyou():
    donor = input ("Enter the donor's FULL NAME "
                        "or 'List' - to see ALL Donors Names ")

    while donor.lower() == "list":
       for names in donor_dict:
            print(names)
       donor = input ("Please enter a  FULL Name ").title()
    
    donation_Amt = float(input ("Enter the Amount for donation "))      

    if donor not in donor_dict:
        donor_dict[donor] = [donation_Amt]
    else:
        donor_dict[donor] +=[donation_Amt]
    
    print(print_thanksnote(donor))    
   # print(thankyou_note(donor))
   

def create_report():
    """Generate a tabular report of donation history"""

    header ='\n{:<20}|{:^13}|{:^13}|{:>13}'.format("Donor Name", "Total Given",
                                                   "Num Gifts", "Average Gift")
    print("XYZ Charity: Donation history report")
    print(header)
    print('-'*len(header))
    donor_sort = sorted(donor_dict, key = sort_key, reverse = True)
    for entry in donor_sort:
        total = sum(donor_dict.get(entry))
        num = len(donor_dict.get(entry))
        average = total/num
        print('{:<18} ${:>10,.2f}{:>13}  ${:>12,.2f}'.format(entry,total,num,average))
    print('')

def sort_key(entry):
    return sum(donor_dict.get(entry))

def send_letters_all():
    for entry in donor_dict:
        #print(entry)
        filename = entry + '.txt'
        with open(filename, 'w') as f:
            f.write(print_thanksnote(entry))

def print_thankyou(name):
    print(f'\nDear {name},')
    print(f'Thank you for your generous donation of ${sum(donor_dict.get(name)):,.2f}' +
          '\nWe appreciate your support.' +
          '\n\nRegards,\nXYZ Charity Team\n')  

def print_thanksnote(name):
    note = (f'\nDear {name},'
            f'\nThank you for your generous donation of ${sum(donor_dict.get(name)):,.2f}'
            '\nWe appreciate your support.'
            '\n\nRegards,\nXYZ Charity Team\n')
    return note


def thankyou_note(entry):
    note = (f'Dear {entry},\n\n\tThank you for your generous donation of '
            f'${sum(donor_dict.get(entry)):,.2f}!\n\tWe appreciate the '
            f'{len(donor_dict.get(entry)):d} total donation(s) that you have made.'
            '\n\tYour donation will be put to good use.'
            '\n\n\tSincerely,\n\t-The Mailroom Team')
    return note


def quit_menu():
    print("Good bye")
    sys.exit()

def main_menu():
     switch_dict = {1: send_thankyou, 2: create_report, 3: send_letters_all, 4: quit_menu }
     while True:
        option = int(options_menu())
        if option not in switch_dict:
            print('enter valid option number\n')
        else:
            switch_dict.get(option)()

if __name__ == "__main__":
    main_menu()
