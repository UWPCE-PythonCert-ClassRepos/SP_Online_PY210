#!/usr/bin/env python3
# Craig Simmons
# Python 210
# mailroom.py# Created 11/23/2020 - csimmonsimport sys
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
    print(len(gifts[0]))
    print(gifts[0][0])
    print(gifts[0][1])
    print(len(gifts[1]))
    print(gifts[0:])
            
    

'''
    for i in range(len(donors)-1):
        print(donors[i] + ' ---- ')
        gift = 0
        print(len(gifts))
        for x in range(len(gifts)-1):
            print(i,x)
            gift = int(gifts[i][x])
            print(type(gift))
            print(gift)

    print(header2)
    Sum = (gifts[1][0])
    print(gifts[1])
    print(gifts[1][0])
    new = (gifts[1][0])
    newer = new + (gifts[1][1])
    print(new)
    print(newer)
'''

'''
    print(average)
    row = '{:<20s}{:1}{:<13,.2f}{:1}{:<10,.0f}{:1}{:<12,.2f}'.format('Bill Gates', '| $', 5463, '| ', 77, '| $', 1020)
    print(header1)
    print(header2)
    print(row)
    print(header2)
    print(donors)
    print(gifts)
  
row = "| {fname:<8s} | {lname:<15s} | {age:<5d} | ${price:<10,.2f} |".format
for data in table_data:
    print(row(fname=data[0], lname=data[1], age=data[2], price=data[3]))
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
            display_report()
            #print('Invalid')
            #everything_else()
display_report(donorlist)   

'''
if __name__ == '__main__':
    main()
'''