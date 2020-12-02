#!/usr/bin/env python3
# Craig Simmons
# Python 210
# mailroom.py# Created 11/23/2020 - csimmons

import sys
# mailroom(donorlist)
#[donor, gifts]
donorlist = [
    ('Craig Simmons', [10000, 2500, 300]),
    ('Allen McConnell', [3000, 6000, 750, 20000]),
    ('Martin Acevedo', [2000, 5000]),
    ('Sutton Keaney', [24500, 500, 3000, 5000, 1000]),
    ('David Basilio', [750, 750, 750, 750, 5000, 750, 750]),
    ('Andrew McLaughlin', [2500, 500, 40000, 50]),
    ('Hussein Saffouri', [1000, 1000, 2100, 7000, 55000]),
    ]

userprompt = '\n'.join(('What would you like to do',
          'Please choose from the options below:',
          '1 - Send a Thank You letter',
          '2 - Create a report',
          '3 - Add new donation data',
          '4 - Quit',
          '>>> '))

def option_one():
    print('in option_one')
    sys.exit()

def option_two():
    print('in option_two')
    sys.exit()

def option_three():
    print('in option_three')
    sys.exit()

def option_exit():
    print('Thank you and goodbye!')
    sys.exit()

def everything_else():
    print('in catch-all function')
    sys.exit()

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



def main():
    response = input(userprompt)
    while(True):
        if response == '1':
            print("option 1 selected")
            option_one()
        elif response == '2':
            display_report(donorlist)
        elif response == '3':
            print("option 3 selected")
            option_three()
        elif response == '4':
            print("option 4 selected")
            option_exit()
        else:
            display_report(donorlist)
            #print('Invalid')
            #everything_else()



if __name__ == '__main__':
    main()
