#!/usr/bin/env python3
donors = [('William Henry Harrison', [806.25, 423.10]),
          ('James K. Polk', [37.67, 127.65, 1004.29]),
          ('Martin van Buren', [126.47]),
          ('Millard Fillmore', [476.21, 2376.21]),
          ('Chester A. Arthur', [10236.91])]

def send_thank_you():
    while True:
        donor = input('Please enter a donor name: ')
        if donor == 'quit':
            break
        elif donor == 'list':
            for item in donors:
                print(item[0])
        else:
            for index, item in enumerate(donors):
                if item[0] == donor:
                    donorindex = index
                    break
            else:
                donors.append((donor, []))
                donorindex = len(donors) - 1
            amount = input('Please enter a donation amount: ')
            try:
                donors[donorindex][1].append(float(amount))
            except ValueError:
                break
            print("""



Dear {},
On behalf of all of us at Save the Marmots, thank you for your generous gift of ${:.2f}.  When it comes to ensuring marmots have loving homes, every dollar goes a long way.

Your gift will help us provide food and shelter for all of the rescued marmots, and ensure our staff have the resources to train them for placement.

Warmest regards,

Sean Hodges


""".format(donor, float(amount)))
            break
    return

def generate_report():
    print('{:24} | {:10} | {:10} | {:12}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print('-'*68)
    for item in donors:
        total = 0
        for amount in item[1]:
            total += amount
        print('{:24}  ${:10.2f}   {:10d}   ${:12.2f}'.format(item[0], total, len(item[1]), total/len(item[1])))
    print('')

if __name__ == '__main__':
    while True:
        print("""Mailroom -- Main Menu

Options:
  1 Send a Thank You
  2 Generate a Report
  3 Quit
""")
        option = input('Please select an option (1, 2, 3): ')
        if option == '1':
            send_thank_you()
        elif option == '2':
            generate_report()
        elif option == '3':
            quit()
