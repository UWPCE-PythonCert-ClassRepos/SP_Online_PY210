#!/usr/bin/env python3

"""

"""

donors = [['Katherine Elmhurst','David Anderson','Edward Hoffstein','Rebecca Manriquez','Callum Foxbright'],
           [40.25,15.50,5.75]           , [8.50,55.]         , [20.,20.,20.]       , [75.,25.]           , [3.75]]


def send_thank_you(donors):

    response = input('\nEnter the full name of the donor > ')
    
    if response == 'list':
        print(donors[0])
        send_thank_you(donors)
    elif response.capitalize() not in donors[0]:
        donors[0].append(response)
    elif response.capitalize() in donors[0]:
        thank_you_recipient = response

    amt = float(input('Enter a donation amount > $'))
    #print(f'${amt:.2f}')


if __name__ == "__main__":    
   
    #print(donors[0][0])
    print('\n Choose one of the following options:')
    print('   1 - Send a Thank You ')
    print('   2 - Create a Report  ')
    print('   3 - Quit             ')
    opt = input(' > ')

    while opt not in ['1','2','3']:
        opt = input(" Choose option '1', '2', or '3' > ")

    if opt == '1':
        send_thank_you(donors)