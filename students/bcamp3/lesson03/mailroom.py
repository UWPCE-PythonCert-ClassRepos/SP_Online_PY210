#!/usr/bin/env python3

"""
Mailroom script

This script accepts user input to perform the following donation database tasks:
    1 - Display the donor database list or update the donation database with a new donation.  
        Then display a 'Thank You' message to the donor of the new donation.
    2 - Display a donation database report
    3 - Quit out of the script
"""

#creating the donor database using nested lists:
donors = [['Katherine Elmhurst','David Anderson','Edward Hoffstein','Rebecca Manriquez','Callum Foxbright'],
          [[1000.,1500.,1900.]   , [10865.,5750.]     , [200.,200.,200.]    , [1750.,1500.]         , [130.75]]]

def send_thank_you():
    
    name = input('\nEnter the full name of the donor > ')
    
    if name == 'list':
        print('\nPrinting list of current donors :\n')
        for donor in donors[0]:
            print('  ',donor)
        send_thank_you(donors)
    else:
        proper_name = ' '.join([word.capitalize() for word in name.split(" ")])
        if proper_name not in donors[0]:
            print('\nAdding donor to database :',proper_name)
            donors[0].append(proper_name)
            donors[1].append([])
        else:
            print(f'\nFound donor {proper_name} in database.')
        
        amt = input('\nEnter a donation amount > $ ')    
        famt = float(amt)
        index = donors[0].index(proper_name)
        donors[1][index].append(famt)
        
        print( '\nEMAIL MESSAGE :')
        print( ' ___________________________________________________________')
        print( '  Subject:  THANK YOU !!!                                   ')
        print( '                                                            ')
        print(f'  Dear {proper_name},                                       ')
        print( '                                                            ')
        print(f'  Thank you for your generous donation of ${famt:.2f}.      ')
        print( '  Your donation will help our foundation achieve our goals. ')
        print( '                                                            ')
        print( '  Regards,\n    Foundation Leadership Team                  ')
        print( ' ___________________________________________________________')

def create_report():
    #       1234567890123456789012345 $12345678901  1234567890  $123456789012
    print('\nREPORT :\n')
    print(' Donor Name               | Total Given | Num Gifts | Average Gift')
    print(' -----------------------------------------------------------------')
    for i in range(len(donors[0])):
        total_given = sum(item for item in donors[1][i])
        num_gifts = len(donors[1][i])
        avg_gift = total_given/num_gifts
        print(f' {donors[0][i]:<25} ${total_given:>11.2f}  {num_gifts:>10d}  ${avg_gift:>12.2f}')


if __name__ == "__main__":    
   
    print('\n Choose one of the following options:')
    print('   1 - Send a Thank You ')
    print('   2 - Create a Report  ')
    print('   3 - Quit             ')
    
    opt = input(' > ')

    while opt not in ['1','2','3']:
        opt = input(" Please choose option '1', '2', or '3' > ")

    if opt == '1':
        send_thank_you()
    elif opt == '2':
        create_report()
    elif opt == '3':
        print('Quitting...')
    