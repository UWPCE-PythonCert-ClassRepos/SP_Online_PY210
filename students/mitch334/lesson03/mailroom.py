"""Lesson 03 | Mailroom Part 1"""

"""You work in the mail room at a local charity. Part of your job is to write incredibly boring,
repetitive emails thanking your donors for their generous gifts. You are tired of doing this over and over again,
so you’ve decided to let Python help you out of a jam and do your work for you."""

# The Program: Part 1
# Write a small command-line script called mailroom.py. This script should be executable. The script should accomplish the following goals:
# 1. It should have a data structure that holds a list of your donors and a history of the amounts they have donated.
#    This structure should be populated at first with at least five donors, with between 1 and 3 donations each.
#    You can store that data structure in the global namespace.
# 2. The script should prompt the user (you) to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”.

""" Initial Donor List
    Data: Donor Name, Total Donated, Number of Donations, and Average Donation Amount"""
# donor_db = [("William Gates, III", [10000.00, 1, 10000.00]),
#             ("Jeff Bezos", [30000.00, 3, 10000.00]),
#             ("Paul Allen", [1000.00, 2, 500.00]),
#             ("Mark Zuckerberg", [20.00, 1, 20.00]),
#             ("Warren Buffet", [600.00, 2, 300.00]),
#             ]

donor_db = [["William Gates, III", [10.00, 1.00]],
            ["Jeff Bezos", [30000.00, 3.00, 10000.00]],
            ["Mark Zuckerberg", [20.00, 20.00]],
            ["Warren Buffet", [600.00, 300.00]],
            ["Paul Allen", [1000.00, 2.00, 500.00, 25.00]],
            ]
# Send a Thank You
# If the user (you) selects “Send a Thank You” option, prompt for a Full Name.
# If the user types list show them a list of the donor names and re-prompt.
# If the user types a name not in the list, add that name to the data structure and use it.
# If the user types a name in the list, use it.
# Once a name has been selected, prompt for a donation amount.
# Convert the amount into a number; it is OK at this point for the program to crash if someone types a bogus amount.
# Add that amount to the donation history of the selected user.
# Finally, use string formatting to compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.
# It is fine (for now) for the program not to store the names of the new donors that had been added, in other words, to forget new donors once the script quits running.
def get_donor_names():
    donor_names = []
    for donor in donor_db:
        donor_names.append(donor[0])
    return donor_names

    # print(donor_names)
def create_donation(name):
    donor_names = get_donor_names()
    position = donor_names.index(name)

    donation_amount = round(float(input('Enter donation amount: ')),2)
    donor_db[position][1].append(donation_amount)

    create_email(name,donation_amount)

def create_email(name,amount):
    print()
    print(f'Dear {name},\n\nThank you for the generous donation of ${amount:.2f}.\n\n'
      'Sincerely,\nMatthew Mitchell')

def send_thankyou():

    donor_name = ''
    while donor_name != 'exit':
        donor_name = input('Thank-You Menu:\n'
                            '\tOptions:\n'
                            "\t\tEnter 'list' for donor list\n"
                            "\t\tEnter 'exit' to return to the main menu\n"
                            '\tEnter full name of donor: ')

        donor_names = get_donor_names()

        if donor_name.lower() == 'list':
            print('\nDonor List:')
            for donor in donor_db: print('\t',f'{donor[0]}')

        elif donor_name.lower() == 'db':
            print('\n',donor_db)

        elif donor_name.lower() == 'exit':
            break

        elif donor_name.title() in donor_names:
            create_donation(donor_name.title())

        else:
            confirm = None
            while confirm != 'no':
                confirm = input("Donor name '"f'{donor_name}'"' was not found.\n"
                                            "\tWould you like to add this donor?\n"
                                            "\tEnter 'yes' or 'no': ")
                if confirm.lower() == 'yes':
                    donor_db.append([donor_name.title(),[] ])

                    create_donation(donor_name.title())
                    break
                elif confirm.lower() == 'no':
                    print('Donor not added.')
                    break
                else:
                    print('Invalid entry.')





# Create a Report
# If the user (you) selected “Create a Report,” print a list of your donors, sorted by total historical donation amount.
# Include Donor Name, total donated, number of donations, and average donation amount as values in each row. You do not need to print out all of each donor’s donations, just the summary info.
# Using string formatting, format the output rows as nicely as possible. The end result should be tabular (values in each column should align with those above and below).
# After printing this report, return to the original prompt.
# At any point, the user should be able to quit their current task and return to the original prompt.
# From the original prompt, the user should be able to quit the script cleanly.
# Your report should look something like this:
#
# Donor Name                | Total Given | Num Gifts | Average Gift
# ------------------------------------------------------------------
# William Gates, III         $  653784.49           2  $   326892.24
# Mark Zuckerberg            $   16396.10           3  $     5465.37
# Jeff Bezos                 $     877.33           1  $      877.33
# Paul Allen                 $     708.42           3  $      236.14
def create_report():
    pass

send_thankyou()

if __name__ == '__main__':

    option = None
    while option != '3':
        option = input('Main Menu:\n'
                    '\t1: Send a Thank You\n'
                    '\t2: Create a Report\n'
                    '\t3: Quit\n'
                    '\tSelect an option: ')
        if option == '1':
            send_thankyou()
        elif option == '2':
            create_report()
        elif option == '3':
            print('Enjoy! :)')
            break
        else:
            print('Invalid option. Select 1, 2, or 3.')
