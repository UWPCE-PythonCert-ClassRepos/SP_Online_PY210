import os
from datetime import datetime

donors = {
    'Adam A': [100, 200],
    'Betty B': [100, 200, 200],
    'Carl C': [100],
    'Ed E': [50, 100, 25],
    'Frank F': [50]
}

def default():
    '''Functions that prints out invalid entry when user inputs invalid entry'''
    print('Incorrect input. Try again!')
    print('*****')
    return

def thanks():
    '''
    This function sends a thank you note to donors, components include
    1> List out current list of donors and ask if user wants to add to existing donors
    2> If no to #1, then ask for new donor name and contribution amount
    3> Note to user that if they entered 'C', they can quit
    '''
    repeat = True
    while repeat:
        # name of donors
        user_input = input('''
Enter A if you like add to these existing donors.
Enter B if you like add new donors.
Enter C if you like to exit from printing thank you note.
''')
        # 3> Note to user that if they entered 'C', they can quit
        if user_input == 'C':
            repeat = False
        # user chooses to add to existing donors
        elif user_input == 'A':
            print('Existing donors: ')
            print(', '.join([k for k in donors.keys()]))
            name = input('Enter name of existing donor: ')
            amt = int(input('Enter donation amount: '))
            existing_donors(name, amt)
        # user chooses to add a new donor
        elif user_input == 'B':
            name = input('Enter name of new donor: ')
            amt = int(input('Enter donation amount: '))
            add_new_donors(name, amt)
        else:
            print('Enter only valid entries (A, B, C)')


def existing_donors(name, amt):
    '''
    Adds donation to existing donors
    '''
    if name not in donors:
        return 'Invalid entry, donor is a new one'
    elif (isinstance(amt,int) == False):
        return 'Invalid entry for donation amount'
    elif amt < 0:
       return 'Invalid entry for donation amount'
    else:
        donors[name].append(amt)
        txt = "Dear {0}, Thank you for your donation of {1}.".format(name, amt)
        return txt


def add_new_donors(name, amt):
    '''
    Adds new donor and donation amount
    '''
    if name in donors:
        return 'Invalid entry, donor is a existing one'
    elif (isinstance(amt,int) == False):
        return 'Invalid entry for donation amount'
    elif amt < 0:
       return 'Invalid entry for donation amount'
    else:
        donors[name] = [amt]
        txt = "Dear {0}, Thank you for your donation of {1}.".format(name, amt)
        return txt

def print_donors():
    donor_name = sorted([name for name in donors.keys()])
    return donor_name


def report():
    '''Computes report content'''
    report_listing = {}
    for k,v in donors.items():
        if len(v) != 0 or sum(v) != 0:
            report_listing[k] = [len(v), sum(v), sum(v)/len(v)]
        else:
            # when there are no donations
            report_listing[k] = [0, 0, 0]
    # sort report
    sorted_report = sorted(report_listing.items(), key = lambda x: x[1][1], reverse = True)
    print(report, sorted_report)
    generate_report(sorted_report)

def generate_report(donor_report):
    ''' generates report'''
    sorted_report = donor_report
    # skipping the first one for testing
    # print('Donor Name'.ljust(20, " "), 'Total Given'.ljust(15, " "), 'Num Gifts'.ljust(10, " "),
    #      "Average Gift".ljust(10, " "))
    for i in range(len(sorted_report)):
        total_given = str('{:.2f}'.format(sorted_report[i][1][1]))
        num_gifts = str(sorted_report[i][1][1])
        avg_gift = str('{:.2f}'.format(sorted_report[i][1][2]))
        # skipping printing for testing
        #print(sorted_report[i][0].ljust(20, " "),total_given.ljust(15, " "), num_gifts.ljust(10, " "), avg_gift.ljust(5, " "))
        reportline = sorted_report[i][0].ljust(20, " ") + total_given.ljust(15, " ") + num_gifts.ljust(10, " ") + avg_gift.ljust(5, " ")
        print(reportline)
    return reportline




def quit_function():
    ''' This function quits the program'''
    exit()

def letters():
    ''' This function generates letters in the folder'''
    for k,v in donors.items():
        filename1 = r"C:/Users/ravigant/UW_Python/"+ k.split(' ')[0] + "/"
        if not os.path.exists(filename1):
            os.makedirs(filename1)
            f = open(((filename1 + str(datetime.now().strftime("%Y%m%d")) +'.txt')), 'w')
            s = str(sum(v))
            f.write(report_text(k,s))
            f.close()


def report_text(name, amount):
    '''This generates text for the report'''
    thank_you_note = "Dear {0},Thank you for your donation of {1}.It will be put to very good use.".format(name, amount)
    return thank_you_note

if __name__ == '__main__':
    print(print_donors())
    options = {'Thanks': thanks, 'Report': report, 'Letters': letters, 'Quit': quit_function}
    while 1:
        request = input('Choose from following three items: \n'
                        'input Thanks to send a thank you \n'
                        'input Letters to send letters \n'
                        'input Report to create a report \n'
                        'input Quit to quit'
                        '\n')

        try:
            options[request]()
        except KeyError:
            default()
