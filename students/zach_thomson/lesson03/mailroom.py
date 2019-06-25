import sys

donor_db = [('donor 1', [10000.00, 20000.00, 4500.00]),
            ('donor 2', [100.00, 500.00]),
            ('donor 3', [25.00]),
            ('donor 4', [100000.00, 50000.00, 125000.00]),
            ('donor 5', [50.00])]


prompt = '\n'.join(('Welcome to the mailroom',
         'Please choose from the following options:',
         '1 - Send a Thank You',
         '2 - Create a Report',
         '3 - Quit',
         '> '))

#send a thank you tasks
def donor_in_list(x):
    i = 0
    result = False
    while i < len(donor_db):
        if x == donor_db[i][0]:
            result = True
            break
        else:
            i = i + 1
    return result

def donor_idx(x):
    i = 0
    while i < len(donor_db):
        if x == donor_db[i][0]:
            return i
        else:
            i += 1

def donor_names():
    i = 0
    donors = []
    while i < len(donor_db):
        donors.append(donor_db[i][0])
        i += 1
    return donors

donation_email = "Dear {},\nThank you for your generous donation of ${:.2f}!"

def thank_you():
    ty_prompt = input('Please enter a full name or type list to see all the current donors: ')
    while ty_prompt.lower() == 'list':
        print(donor_names())
        ty_prompt = input('Please enter a full name or type list to see all the current donors: ')
    else:
        if donor_in_list(ty_prompt) == True:
            donation_amount = float(input('Please enter a donation amount: '))
            donor_db[donor_idx(ty_prompt)][1].append(float(donation_amount))
        else:
            donation_amount = float(input('Please enter a donation amount: '))
            new_entry = (ty_prompt, [donation_amount])
            donor_db.append(new_entry)
    print(donation_email.format(ty_prompt, donation_amount))


#create a report functions
donor_db_copy = donor_db[:]

def sum_function(x):
    total = 0
    for i in donor_db_copy[x][1]:
        total = total + i
    return total

def number_donations(x):
    return len(donor_db_copy[x][1])

def average_gift(x):
    return sum_function(x)/len(donor_db_copy[x][1])

def sum_second(elem):
    total = 0
    for i in elem[1]:
        total = i + total
    return total

donor_db_copy.sort(key = sum_second, reverse = True)
#print(donor_db_copy)

def create_table():
    report_table = []
    i = 0
    while i < len(donor_db_copy):
        report_table.append(donor_db_copy[i][0])
        report_table.append(sum_function(i))
        report_table.append(number_donations(i))
        report_table.append(average_gift(i))
        i = i + 1
    return report_table

#print(create_table())

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

if __name__ == "__main__":
    main()
