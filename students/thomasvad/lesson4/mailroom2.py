import sys
import os

donors = {
'William Gizzard': [1.00, 1234.12, 8000],
'Mark Zhophone': [120000.00],
'Jeff Binsue': [80.00, 200.00, 50.00],
'Prince luis': [666],
'Paul Alad': [56743, 300000, 10000000, 88743],
'mike mixer': [309000, 10000000]}



def thank():
    name = input("Please enter the donors full name. To check the list of previous donors type list: ")
    print('\n')
    while name.lower() == 'list':
        print('Past Donors:')
        for donor in donors.keys():
            print(donor)
        print('\n')
        name = input('Please enter the full name of the donor. If it is a new donor enter their name: ')
        print('\n')

    # compares each donor name with what was inputed as a set to get the correct key if donor is in list
    decide = sorted([(i, set(i.lower()) == set(name.lower())) for i in donors.keys()], key= lambda x: x[1])
    decide2 =  [bool[1] for bool in decide]
#    print(decide, decide2)

    if True not in decide2:
        donors[name] = []
        donation = input('How much did {} donate? '.format(name))
        if donation.isnumeric():
            donors[name].append(int(donation))

    else:
        name = decide[-1][0]
        donation = input('How much did {} donate? '.format(name))
        if donation.isnumeric():
            donors[name].append(int(donation))
    print('\n')

    email = '''Dear {},

Thank you for your donation of ${}.

Best,
The Foundation'''.format(name,donation)
    return print(email,'\n')

def report():
    donor_record = [[i, sum(donors[i]), len(donors[i]), sum(donors[i])/len(donors[i])] for i in donors]
    sorted_donor_record = sorted(donor_record, key=lambda x:-x[1])

    print(f"\n\n{'Name':<16}{'Total Given':<12} {'Num Gifts':<10} {'Average Gift':<14}")
    print("-" * 15 + " " + "-" * 11 + "  " + "-" * 9 + "  " + "-" *13)
    for i in sorted_donor_record:
        print(f"{i[0]:<16}{i[1]:<12.2f} {i[2]:<10} {i[3]:<14.2f}")
    print('\n')


def letters():
    for i in donors:
        with open('{}.txt'.format(i),'w') as f:
            f.write('''Dear {},

Thank you for your total donation of ${:.2f}.
It will be put to good use.

Thanks,
The Foundation'''.format(i,sum(donors[i])))


def quit():
    print('Quitting...')
    sys.exit()


prompt = '\n'.join(('Please select what you want to do.',
'type 1 to Send a Thank You',
'type 2 to Create a Report',
'type 3 to send letters to all donors',
'type 4 to quit','>>> '))

options ={"1": thank,
          "2": report,
          "3": letters,
          "4": quit}


def menu():
    while True:

        response = input(prompt)
        print('\n')
        if response in options:
            options[response]()
        else:
            print('Not a valid option')
            print('\n')



if __name__ == '__main__':

    menu()
