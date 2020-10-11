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
    print('Incorrect input. Try again!')
    print('*****')
    return

def thanks():
    repeat = True
    while repeat:
        name = input('Enter full name: ')
        if name == 'list':
            print(donors.keys(), end = " ")
        elif name in donors.keys():
            amt = int(input('Enter a amount to donate: '))
            donors[name].append(amt)
            # email
            print('''
                    Dear {0},
                    Thank you for your donation
                    '''.format(name))
            repeat = False
        else:
            repeat = False
            donors[name] = []
    return

def report():
    report_listing = {}
    for k,v in donors.items():
        if len(v) != 0 or sum(v) != 0:
            report_listing[k] = [len(v), sum(v), sum(v)/len(v)]
        else:
            # when there are no donations
            report_listing[k] = [0, 0, 0]
    # sort report
    sorted_report = sorted(report_listing.items(), key = lambda x: x[1][1], reverse = True)
    print('Donor Name'.ljust(20, " "), 'Total Given'.ljust(15, " "), 'Num Gifts'.ljust(10, " "),
          "Average Gift".ljust(10, " "))
    for i in range(len(sorted_report)):
        total_given = str('{:.2f}'.format(sorted_report[i][1][1]))
        num_gifts = str(sorted_report[i][1][1])
        avg_gift = str('{:.2f}'.format(sorted_report[i][1][2]))
        print(sorted_report[i][0].ljust(20, " "),total_given.ljust(15, " "), num_gifts.ljust(10, " "), avg_gift.ljust(5, " "))
    return

def quit_function():
    exit()

def letters():
    for k,v in donors.items():
        filename1 = r"C:/Users/ravigant/UW_Python/"+ k.split(' ')[0] + "/"
        if not os.path.exists(filename1):
            os.makedirs(filename1)
            f = open(((filename1 + str(datetime.now().strftime("%Y%m%d-%H%M%S")) +'.txt')), 'w')
            s = str(sum(v))
            f.write('''
                        Dear {0},
                        Thank you for your donation of {1}.
                        It will be put to very good use.
                        '''.format(k,s))
            f.close()

if __name__ == '__main__':
    options = {'Thanks': thanks, 'Report': report, 'Letters': letters, 'Quit': quit_function}
    while 1:
        request = input('Choose from following three items: \n'
                        'input Thanks to send a thank you \n'
                        'input Letters to send letters'
                        'input Report to create a report \n'
                        'input Quit to quit \n'
                        '')

        try:
            options[request]()
        except KeyError:
            default()
