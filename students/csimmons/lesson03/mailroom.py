#!/usr/bin/env python3
# Craig Simmons
# Python 210
# mailroom.py
# Created 11/23/2020 - csimmons

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
    donor_names = []
    gifts = []
    for i in range(len(donorlist)):
        #print(str(donorlist[i]))
        #print(str(donorlist[i][0]))
        #print(str(donorlist[i][1]))
        donor_names.append(donorlist[i][0])
        gifts.append(donorlist[i][1])
    print(donor_names)
    print(gifts)

    

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
            display_report()
            #print('Invalid')
            #everything_else()
display_report(donorlist)   

'''
if __name__ == '__main__':
    main()
'''