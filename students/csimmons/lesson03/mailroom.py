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
    header1 = '{:20}{:1}{:15}{:1}{:10}{:1}{:12}'.format('\n''Donor Name ', '|', ' Total Given ', '|', ' Num Gifts ', '|', ' Average Gift ')
    header2 = ('_ ' * 32) +'\n'
    #row = '{:<20s}{:1}{:<13,.2f}{:1}{:<10,.0f}{:1}{:<12,.2f}'.format('Bill Gates', '| $', 5463, '| ', 77, '| $', 1020)
    #row = '{:<20s}{:1}{:<13,.2f}{:1}{:<10,.0f}{:1}{:<12,.2f}'.format('Bill Gates', '| $', 5463, '| ', 77, '| $', 1020)
    donors = list(map(lambda x:x[0], donorlist))
    gifts = list(map(lambda x:x[1], donorlist))
    
    print(donors)
    print(gifts)
    print(header2)
    donor_name = []
    all_info = [[],]
    gift_info = [[],]

    

    print(gifts)
    for gift in gifts:
        print(gift)
        gift_total = 0
        gift_num = 0
        #total gifts
        for i in range(len(gift)):
            gift_amount = gift[i]
            gift_total = gift_amount + gift_total
            
        gift_num = len(gifts[i])
        gift_info.append(gift_total)
        gift_info.append(gift_num)
        gift_info.append(gift_total/gift_num)
        print(gift_info)
    all_info.append(gift_info)
    print(all_info)
display_report(donorlist)
'''    
def main():
    response = input(userprompt)
    while(True):
        if response == '1':
            print("option 1 selected")
            option_one()
        elif response == '2':
            print("option 2 selected")
            option_two()
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
'''