#!/usr/bin/env python3
donors = {'William Henry Harrison' : [806.25, 423.10],
          'James K. Polk' : [37.67, 127.65, 1004.29],
          'Martin van Buren' : [126.47],
          'Millard Fillmore' : [476.21, 2376.21],
          'Chester A. Arthur' : [10236.91]}

def send_thank_you():
    while True:
        donor = input('Please enter a donor name: ')
        if donor == 'quit':
            break
        elif donor == 'list':
            for item in donors.keys():
                print(item)
        else:
            if not donor in donors.keys(): donors[donor] = []
            amount = input('Please enter a donation amount: ')
            try:
                donors[donor].append(float(amount))
            except ValueError:
                break
            print("""Dear {},
Thank you for your generous gift of ${:.2f}.  Your donation will be put to excellent use doing thing.

Something something something.

Warmest regards,

Sean Hodges""".format(donor, float(amount)))
            break
    return

def generate_report():
    print('{:24} | {:10} | {:10} | {:12}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print('-'*68)
    for donor in donors.keys():
        total = 0
        for amount in donors[donor]:
            total += amount
        print('{:24}  ${:10.2f}   {:10d}   ${:12.2f}'.format(donor, total, len(donors[donor]), total/len(donors[donor])))
    return

if __name__ == '__main__':
    while True:
        print('')
        print('Mailroom -- Main Menu')
        print('')
        print('Options:')
        print('  1 Send a Thank You')
        print('  2 Generate a Report')
        print('  3 Quit')
        print('')
        option = input('Please select an option (1, 2, 3): ')
        if option == '1':
            send_thank_you()
        elif option == '2':
            generate_report()
        elif option == '3':
            quit()
        else:
            continue
