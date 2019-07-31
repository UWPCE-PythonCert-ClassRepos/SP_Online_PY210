#!/usr/bin/env python3
donors = [['William Henry Harrison', 806.25, 423.10],
          ['James K. Polk', 37.67, 127.65, 1004.29],
          ['Martin van Buren', 126.47],
          ['Millard Fillmore', 476.21, 2376.21],
          ['Chester A. Arthur', 10236.91]]

def send_thank_you():
    print('Placeholder for thank you letter')
    return

def generate_report():
    print('Placeholder for report')
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
