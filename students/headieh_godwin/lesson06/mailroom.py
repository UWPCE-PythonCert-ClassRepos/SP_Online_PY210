#!/usr/bin/env python3
import inquirer
import os
import time
import sys
import re

donors = {
  "Karen": [20,20,100],
  "Susan": [20],
  "Larry": [40,50],
  "Curly": [20.99,20,100],
  "Mo": [2]
}

def menu():
    """ Main function """
    while True:
        try:
            resp = original_prompt()
            if int(resp) in options:
                options.get(int(resp))()
            else:
                print(' Input is invalid, please input a valid option. ')
        except ValueError:
            print(' Input is invalid, please input a valid option. ')


#def original_prompt():
#    """ Prompt for a user selection """
#    questions = [
#        inquirer.List('action',
#                      message="What would you like to do? ",
#                      choices=['Send a Thank You', 'Create a Report', 'quit'])]
#    answers = inquirer.prompt(questions)
#    return(answers['action'])


def original_prompt():
    answers = input(f"""
Choose an action:

1 - Send a Thank You to a single donor.
2 - Create a Report.
3 - Send letters to all donors.
4 - Quit
""")
    return(answers)

def email(donor_name, donation_amt, freq):
    if freq == 0: # case for new donor
        return(f"""
Dear {donor_name},

Thank you for your very kind donation of ${donation_amt:.2f}

It will be put to very good use.

                       Sincerely,
                          -The Team""")
    elif freq == 1: #case for sending emails to all who have donated one time
        return(f"""
Dear {donor_name},

Thank you for your very kind donation of ${donation_amt:.2f}

It will be put to very good use.

                       Sincerely,
                          -The Team""")

    else: #case for sending emails to all who have donated multiple times
       return(  f"""
Dear {donor_name},

Thank you for your very kind donations totaling ${donation_amt:.2f}

It will be put to very good use.

                       Sincerely,
                          -The Team""")

# Get money
def valid_money():
    while True:
        r = input("Please enter a donation amount ")
        try:
            amount = float(r)
            if amount < 0.01 or amount > 10000:
                print("Invalid value")
            else:
                return amount
        except ValueError:
            print("Invalid value")

# Get name
def valid_name():
    while True:
        r = input("Please enter a full name ")
        r2= re.sub(r'[^a-zA-Z]+', '', r)
        if r == '':
            print('No name entered')
        elif r2 == '':
            print('Not a valid name')
        else:
            return r

#quits
def quits():
    print("Bye!")
    sys.exit()

#Thanks!
def thanks():
    """ Prompt for a donor name and amount - then prints email"""
    response1 = valid_name()
    names = list(donors)
    if response1 == 'list':
        print(names)
    elif response1 not in names:
        response2 = valid_money()
        donors.update( {response1 : (response2,)} )
        print(email(response1, response2, freq=0))
    #elif response1 in names:
    else:
        response2 = valid_money()
        wo_d = donors.get(response1)
        w_d = (wo_d) + (response2,)
        donors.update( {response1 : (w_d)} )
        print(email(response1, response2, freq=0))

def thanks_all():
    parent = os.getcwd()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    os.mkdir(timestr)
    for k, v in donors.items():
        filename = os.path.join(parent, timestr + "/" + k + '.txt')
        freq = len(v) # email cases of freq=1 or freq>1
        tot = sum(v)
        letter = email(k, tot, freq)
        print(k)
        with open(filename, 'w') as file:
            file.write(letter)
    print("Letters have been outputted for all donors")

#Report
def report(donors=donors):
    raw = []
    """ prints a report of donors """
    col_labels = ["Donor Name",
                  "Total Given",
                  "Num Gifts",
                  "Average Gift"]
    for k, v in donors.items():
        tot = sum(v)
        n = len(v)
        avg = round(tot/n,2)
        raw.append({'name': k,
                    'total': tot,
                    'number': n,
                    'average': avg})
    sort_data = (sorted(raw, key = lambda i: i['total'], reverse=True))
    print(f"{col_labels[0]:<30}{col_labels[1]:<15}{col_labels[2]:<15}{col_labels[3]:<5}")
    print("-"*72)
    for i in sort_data:
        print(f"{i['name']:<30}${i['total']:>10.2f}{i['number']:>12}   ${i['average']:>15.2f}")

options = {
    1: thanks,
    2: report,
    3: thanks_all,
    4: quits
}

if __name__ == '__main__':
    menu()
