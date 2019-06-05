#!/usr/bin/env python3

import sys
from operator import itemgetter

lst_donors = [["Bob Jones", [63.00, 30.00]],
            ["Sue Smith", [50.00]],
            ["Joe Grimes", [102.00, 45.00, 70.00]],
            ["Andrea Funk", [21.00, 21.00]],
            ["Mickey Mouse", [500.00, 250.00, 100.00]]
            ]

prompt = "\n".join(("Please choose from below mailroom options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Quit",
          ">>> "))

def listof_donors():
    '''Displays list of donor names in donor list'''
    for name in lst_donors:
        print(name[0])

def report():
    '''Draws up report of names and donations'''
    lst_ttl_amt = []

    #calculates sum of donations
    for donations in lst_donors:
        ttl_amt = sum(donations[1])
        donations.append(ttl_amt)

    #calculates number of donations
    for donations in lst_donors:
        donations.append(len(donations[1]))

    #calculates average of donations
    lst_avg_donations = []
    for donations in lst_donors:
        average = sum(donations[1])/len(donations[1])
        str_average = f'{average:.2f}' #limits average to two decimal points
        donations.append(str_average)

    #sorts list of donors on total amount donated
    lst_donors_sorted = sorted(lst_donors, key=itemgetter(2), reverse = True)
    for ttl_donation in lst_donors_sorted:
        ttl = ttl_donation[2]
        str_ttl = '%.2f' % ttl #limits total to two decimal points
        ttl_donation[2] = str_ttl

    #removes history of donations, since it's not in final report
    for donations in lst_donors_sorted:
        donations.pop(1)

    #creates header and horizontal rule for top of final report
    header = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    rule = '-'* len(header)
    lst_donors_sorted.insert(0, header) #adds header to existing list of donors
    lst_donors_sorted.insert(1, rule) #adds rule to existing list of donors

    #formats final report
    longest_cols = [
        (max([len(str(row[i])) for row in lst_donors_sorted]) + 3)
        for i in range(len(lst_donors_sorted[0]))
    ]
    row_format = "".join(["{:>" + str(longest_col) + "}" for longest_col in longest_cols])
    for row in lst_donors_sorted:
        print(row_format.format(*row))

def main():
    '''Main action of program'''
    while True:
        response = input(prompt) #prompts user with menu of options
        if response =='1':
            donor_question = input("Please type 'list' to see existing list of donors or enter the name of a donor: ")
            if donor_question == 'list':
                listof_donors()
            elif donor_question not in lst_donors: #if donor entered is not already in list
                lst_new_donor = []
                lst_donors.append(lst_new_donor) #appends empty list to donor list
                lst_donors[-1].append(donor_question) #adds donor name to empty list
                prompt_amt = input("Please enter new donation amount: ")
                flt_prompt_amt = float(prompt_amt) #converts to float to match other amount values in list
                lst_amount = []
                lst_donors[-1].append(lst_amount)#appends empty list to final element in list
                lst_amount.append(flt_prompt_amt)#adds amount to final element in list
                #creates email to be sent to user
                email = f'Dear {donor_question}, Thank you for your generous donation of ${prompt_amt}. We hope you will consider donating again!'
                print(email)
            else:
                for name in lst_donors: #if donor entered is in list
                    if donor_question == name[0]: #checks if name already in list
                        donations = name[1] #list of existing donations
                        prompt_amt = input("Please enter new donation amount: ")
                        flt_prompt_amt = float(prompt_amt)#converts to float to match other amount values in list
                        donations.append(flt_prompt_amt)#adds amount to desired name in list
                        #creates email to be sent to user
                        email = f'Dear {donor_question}, Thank you for your generous donation of ${prompt_amt}. We hope you will consider donating again!'
                        print(email)
                    else:
                        continue #loops through list of donors to find name entered

        elif response == '2':
            report() #prints report
        elif response == '3':
            break #exits program
        else:
            print("Not a valid option")

if __name__ == "__main__":
    main()
