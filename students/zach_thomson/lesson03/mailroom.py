#import sys

donor_db = [('donor 1', [10000.00, 20000.00, 4500.00]),
            ('donor 2', [100.00, 500.00]),
            ('donor 3', [25.00]),
            ('donor 4', [100000.00, 50000.00, 125000.00]),
            ('donor 5', [50.00])]

#print(donor_db)
#print(donor_db[1][1])

prompt = '\n'.join(('Welcome to the mailroom',
         'Please choose from the following options:',
         '1 - Send a Thank You',
         '2 - Create a Report',
         '3 - Quit',
         '> '))

def thank_you():
    pass

#create a report functions
def sum_function(x):
    total = 0
    for i in donor_db[x][1]:
        total = total + i
    return total

def number_donations(x):
    return len(donor_db[x][1])

def average_gift(x):
    return sum_function(x)/len(donor_db[x][1])



def create_table():
    report_table = []
    i = 0
    while i < len(donor_db):
        report_table.append(donor_db[i][0])
        report_table.append(sum_function(i))
        report_table.append(number_donations(i))
        report_table.append(average_gift(i))
        i = i + 1
    return report_table

print(create_table())

header = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
table_header = "{:<20}| {} | {} | {}".format(*header) + '\n' + "-" * 60

def create_report():
    '''formats create_table into the create_report format'''
    table = create_table()
    print(table_header)
    line_format = ("{:<20}" + " $" + "{:>12.2f}" + "{:>11}" + "  $" + "{:>12.2f}" + '\n') * len(donor_db)
    print(line_format.format(*table))

#create_report()

def exit_program():
    print('Bye')
    sys.exit() # exit the interactive script

def main():
    while True:
        response = input(prompt)
        if response == '1':
            thank_you()
        elif response == '2':
            create_report()
        elif response == '3':
            exit_program()
        else:
            print('Not a valid option')

#if __name__ == "__main__":
#    main()
