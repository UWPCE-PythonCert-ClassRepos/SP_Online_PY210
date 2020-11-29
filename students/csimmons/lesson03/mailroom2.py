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

donorlist2 = [ 
    ['Craig Simmons', 10000, 2500, 300],
    ['Allen McConnell', 3000, 6000, 750, 20000],
    ['Martin Acevedo', 2000, 5000],
    ['Sutton Keaney', 24500, 500, 3000, 5000, 1000],
    ['David Basilio', 750, 750, 750, 750, 5000, 750, 750],
    ['Andrew McLaughlin', 2500, 500, 40000, 50],
    ['Hussein Saffouri', 1000, 1000, 2100, 7000, 55000] 
    ]
userprompt = '\n'.join(('What would you like to do',
          'Please choose from the options below:',
          '1 - Send a Thank You letter',
          '2 - Create a report',
          '3 - Add data',
          '4 - Quit',
          '>>> '))

def exit_option():
    print('Thank you and goodbye!')
    sys.exit()

def option_one():
    print('1 was selected')
    sys.exit()

def option_two():
    print('2 was selected')
    sys.exit()

def option_three():
    print('3 was selected')
    sys.exit()

def option_four():
    print('4 was selected')
    sys.exit()

donorlist = [
    ('Craig Simmons', [10000, 2500, 300]),
    ('Allen McConnell', [3000, 6000, 750, 20000]),
    ('Martin Acevedo', [2000, 5000]),
    ('Sutton Keaney', [24500, 500, 3000, 5000, 1000]),
    ('David Basilio', [750, 750, 750, 750, 5000, 750, 750]),
    ('Andrew McLaughlin', [2500, 500, 40000, 50]),
    ('Hussein Saffouri', [1000, 1000, 2100, 7000, 55000]),
    ]

def unpack(seq):
    new_donors =[]
    sum_this =[]
    global total
    for i in range(len(seq)):
        #new_donors.append((seq[i][0])
        print(seq[i][0])
        x = (seq[i][0])
        new_donors.append(x)

        print(seq[i][1])
        y = (seq[i][1])
        total = total + y
        sum_this.append(y)
    print(total)

unpack(donorlist)
#print(mailroom_data1)

def mailroom(seq):
    new_donors =[]
    cash_only = []
    for i in range(len(seq)):
        print((seq[i][0]))
        print((seq[i][1:]))
        new_donors.append(seq[i][0])
        cash_only.append(seq[i][1:])
    print(new_donors)
    print(cash_only)
    print(cash_only[1])

def main():
    response = input(userprompt)
    while(True):
        if response == '1':
            option_one()
        elif response == '2':
            option_two()
        elif response == '3':
            option_three()
        elif response == '4':
            exit_option()
        else:
            print('Invalid')
            break

#main()
#mailroom(donorlist2)




'''
if _name_ == '_main_':
    main()
'''
