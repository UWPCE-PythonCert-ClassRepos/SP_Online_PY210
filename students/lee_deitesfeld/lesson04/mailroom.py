#!/usr/bin/env python3

import sys
from operator import itemgetter

main_prompt = "\n".join(("Please choose from below mailroom options:",
          "1 - Manage Donors and Donations",
          "2 - Create a Report",
          "3 - Send letters to all donors",
          "4 - Quit",
          ">>> "))


sub_prompt = "\n".join(("Please make a selection from the following options",
                        "1 - List the Names of Donors",
                        "2 - Add a New Donation",
                        "3 - Return to Main Menu"
                        ">>> "))

dic_donors = {'donor_db':
                [
                {"name": "Bob Jones",
                 "donations": [63.00, 30.00]
                },
                {"name": "Sue Smith",
                 "donations": [50.00]
                },
                {"name": "Joe Grimes",
                 "donations": [102.00, 45.00, 70.00]
                },
                {"name": "Andrea Funk",
                 "donations": [21.00, 21.00]
                },
                {"name": "Mickey Mouse",
                 "donations": [500.00, 250.00, 100.00]
                }
                ]}

def menu_selection(prompt, main_dispatch):
    while True:
        response = input(prompt)
        if main_dispatch[response]() == "exit menu":
            break

def sub_menu():
    menu_selection(sub_prompt, sub_dispatch)

def quit():
    print("Quitting this menu")
    return "exit menu"

def report():
    '''Draws up report of names and donations'''

    #calculates sum of donations and adds new key-value pair to donor_db dict
    for x in dic_donors['donor_db']:
        ttl_amt = sum(x['donations'])
        x['sum'] = ttl_amt

    #calculates number of donations and adds new key-value pair to donor_db dict
    for x in dic_donors['donor_db']:
        numofdonations = len(x['donations'])
        x['count'] = numofdonations

    #calculates average of donations and adds new key-value pair to donor_db dict
    for x in dic_donors['donor_db']:
        average = sum(x['donations'])/len(x['donations'])
        str_average = f'{average:.2f}' #limits average to two decimal points
        x['average'] = str_average

    #sorts list of donors on total amount donated
    for x in dic_donors['donor_db']:
        int_ttl_amt = int(x['sum']) #convert ttlamt to integer so sort will work on entire digit (not just first)
        x['sum'] = int_ttl_amt
    dic_donors['donor_db'].sort(key=itemgetter('sum'), reverse = True) #sort on key='sum'
    for x in dic_donors['donor_db']:
        ttl_amt_2dec = '%.2f' % x['sum'] #limits total to two decimal points
        x['sum'] = ttl_amt_2dec

    #removes history of donations, since it's not in final report
    for x in dic_donors['donor_db']:
        del x['donations']

    #formats final report
    header = ["Name", "Donations Total", "Number of Donations", "Average Donation"]
    print('{:>10} {:>20} {:>30} {:>40}'.format(*header))
    print('---'*35)
    for line in dic_donors['donor_db']:
        print('{:>10} {:>20} {:>30} {:>40}'.format(*line.values()))

def listof_donors():
    '''Corresponds to submenu item List the Names of Donors'''
    for item in dic_donors['donor_db']:
        print(item['name'])

def add_donor():
    '''Corresponds to submenu item Add a New Donation'''
    donor_question = input("Please enter the name of a new or existing donor: ")
    for item in dic_donors['donor_db']:
        if donor_question in item["name"]:
            donation_amount = input("Please enter donation amount for donor: ")
            item["latest_donation"] = donation_amount #adds temporary key-value pair for email printout
            email = 'Dear {name}, Thank you for your generous donation of {latest_donation}. We hope you will consider donating again!'.format(**item)
            print(email)
            del item["latest_donation"] #deletes temporary key-value pair
            item['donations'].append(float(donation_amount)) #adds donation to current list of donations
        else:
            continue
    if donor_question not in item["name"]:
        dic_new_donor= {}
        dic_new_donor["name"] = donor_question
        dic_donors['donor_db'].append(dic_new_donor)
        donation_amount = input("Please enter donation amount for donor: ")
        dic_new_donor['donations'] = donation_amount
        email = 'Dear {name}, Thank you for your generous donation of {donations}. We hope you will consider donating again!'.format(**dic_new_donor)
        print(email)
        dic_new_donor['donations'] = [float(donation_amount)]

def email_all():
    for donor in dic_donors['donor_db']:
        name_unmodified = donor["name"]
        name_file = name_unmodified.replace(' ', '_')
        donation_last = donor["donations"][-1]
        donation_last = f'{donation_last:.2f}'
        with open('%s.txt' % name_file, 'w') as f:
            f.write(f"Dear {name_unmodified},\n \tThank you for your very kind donation of ${donation_last}.\n \tIt will be put to very good use.\n \t\tSincerely, \n \t\t\t-The Team")
    print("Emails created.")

main_dispatch = {"1" : sub_menu,
                 "2" : report,
                 "3" : email_all,
                 "4" : quit}

sub_dispatch = {"1" : listof_donors,
                "2" : add_donor,
                "3" : quit}

if __name__ == "__main__":
    menu_selection(main_prompt, main_dispatch)
