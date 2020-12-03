#!/usr/bin/env python3
# Craig Simmons
# Python 210
# mailroom.py# Created 11/23/2020 - csimmons

import sys

donorlist = [
    ('Craig Simmons', [10000, 2500, 300]),
    ('Allen Connell', [3000, 6000, 750, 20000]),
    ('Martin Acevedo', [2000, 5000]),
    ('Sutton Keaney', [24500, 500, 3000, 5000, 1000]),
    ('David Basilio', [750, 750, 750, 750, 5000, 750, 750]),
    ('Andrew Laughlin', [2500, 500, 40000, 50]),
    ('Hussein Saffouri', [1000, 1000, 2100, 7000, 55000]),
    ]

menu_prompt = '\n'.join(('What would you like to do?',
          'Please choose from the options below:',
          '1 - Send a Thank You letter',
          '2 - Create a report',
          '3 - Quit',
          '>>> '))

thanks_prompt = '\n'.join(('Please enter a donor name',
                '(Enter "List" for a list of current donors)',
                '>>>  '))

gift_prompt = '\n'.join(('Please enter the new donation',
                '>>>  '))

def generate_thankyou(f_response, f_gift):
    print("""
    Dear {},
    We would like to thank you for your extremely generous donation 
    of ${:.2f} to the Anonymous Charity of Seattle.\n
    Sincerely,
    CA Simmons \n""".format(f_response, f_gift))

def insert_donor(response):
    new_donor = tuple([response,[]])
    donorlist.append(new_donor)
    return donorlist
    #donorlist[7][1].append(1000)
def insert_gift(gift):
    get_index = (len(donorlist)-1)
    donorlist[get_index][1].append(gift)
    return donorlist


def send_thankyou():
    donors = list(map(lambda x:x[0], donorlist))
    response = input(thanks_prompt)
    f_response = response.title()

    if response.lower() == 'list':
        for donor in donors:
            print(donor)
        print('\n')
        main()

    elif response.title() in donors:
        gift = input(gift_prompt)
        f_gift = float(gift)
        f_response = response.title()

        for i in range(len(donorlist)-1):
            if f_response == donorlist[i][0]:
                donorlist[i][1].append(f_gift)

        generate_thankyou(f_response, f_gift)
        print(donorlist)
        main()
    else:
        f_response = response.title()
        print(('{} is a new donor!').format(f_response))

        gift = input(gift_prompt)
        f_gift = float(gift)
        
        new_donor = tuple([f_response,[]])
        donorlist.append(new_donor)

        get_length = len(donorlist)-1
        donorlist[get_length][1].append(f_gift)
        #
        generate_thankyou(f_response, f_gift)
        print(donorlist)
        main()


def display_report(seq):
    donors = list(map(lambda x:x[0], donorlist))
    gifts = list(map(lambda x:x[1], donorlist))
    all_info = []
    header1 = '{:20}{:1}{:15}{:1}{:10}{:1}{:12}'.format('\n''Donor Name ', '|', ' Total Given ', '|', ' Num Gifts ', '|', ' Average Gift ')
    header2 = ('_ ' * 31) +'\n'
    info_row = '{dname:<20s} $ {total:<13,.2f} {gifts:^10d} $ {avg:<12,.2f}'.format
    for i in range(len(donorlist)):
        total_gift = 0
        average_gift = 0
        gift_info = []
        for x in range(len(gifts[i])):
            total_gift += gifts[i][x]
        average_gift = total_gift / len(gifts[i])
        gift_info.append(donors[i])
        gift_info.append(total_gift)
        gift_info.append(len(gifts[i]))
        gift_info.append(average_gift)
        all_info.append(gift_info)
    print(header1)
    print(header2)
    for i in range(len(all_info)):
        print(info_row(dname=all_info[i][0], total=all_info[i][1], gifts=all_info[i][2], avg=all_info[i][3]))
    print('\n')
    main()


def main():
    response = input(menu_prompt)
    while(True):
        if response == '1':
            send_thankyou()
        elif response == '2':
            display_report(donorlist)
        elif response == '3':
            print('Quitting Mailroom Application')
            sys.exit()
        else:
            print('oops, you entered something bad')
            main()


if __name__ == '__main__':
    main()
