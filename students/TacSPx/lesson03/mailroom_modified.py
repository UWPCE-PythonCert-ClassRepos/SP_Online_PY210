# ---------------------------------------------------------------------------- #
# Title: mailroom part 1
# Description: A program that holds a list of donors and amounts they donated.
#              Prompt the user to choose 3 menu actions; thank you, report, quit.
#
# <05/30/2020>, Created Script, mailroom part 1
# <06/12/2020>, Clean-up to snake case, adding sorting in reporting descending totals, fix indentation error
# ---------------------------------------------------------------------------- #
#imports
import sys
from collections import defaultdict
from operator import itemgetter
# Data ---------------------------------------------------------------------- #
# Task 1: Create data
# Create a data structure that holds a list of your donors and a history of the amounts they have donated.
# Have least five donors, with between 1 and 3 donations each, store in the global namespace.


donor_info = [("Jim Zorn", [3772.32, 1201.17]),
            ("Jermaine Kearse", [877.33]),
            ("Marcus Trufant", [1563.23, 1043.87, 1.32]),
            ("K.J. Wright", [21663.23, 300.87, 100432.0]),
            ("Curt Warner", [663.23, 300.87, 10432.0]),
            ]

# Processing  --------------------------------------------------------------- #
# Task 2:  Menu choices
# Prompt the user to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”.
###############################################
#   "Menu of Choices"
###############################################

def main():
    '''
    Menu of Choices:  Thank You, Report, Create a Report
    :return:
    '''

    while (True):
        print("""
        \n**** XYZ Nonprofit Charity ****\n
        Menu of Options
        1) Send a "Thank You"
        2) Create a Report
        3) Exit Program
        """)
        str_choice = str(input("Which option would you like to perform? [1 to 3] - "))
        print()  # added a new line for spacing looks
        if (str_choice.strip() == '1'):
            thank_you()
        elif (str_choice.strip() == '2'):
            report()
        elif (str_choice.strip() == '3'):
            exit_program()
        else:
            print("\nPlease choose only 1, 2, or 3!")

###############################################
#   #1 Send a "Thank You"
###############################################
def thank_you():
    '''
    Thank You:  Will append donations to existing donors, or adds new donors with donations.
    User can see list of existing donors by typing 'list'.  Once donation is entered script will create
    custom thank you letter/ email.
    :return:
    '''
    while (True):
        donor_name = input("Type 'List' to see all names in Database or\nType First and Last Name: ").title()
        if (donor_name.lower() == 'list'):
            # define format row
            row = "{Name:<18s}".format
            print("\nDONOR REGISTRY:")
            donor_sort = (sorted(donor_info))
            for donor in donor_sort:
                donor_lst = (row(Name=donor[0]))
                print(donor_lst)
            input("Press Enter to Continue")
            print()
            continue

        if (donor_name.lower() != 'list'):
            donor_amount = int(input("Enter Amount of Donation: $"))
            # if name is in list append dollar amount to donors bucket
            for i in donor_info:
                if i[0] == donor_name:
                    i[1].append(donor_amount)
                    print(f"'{donor_name}' is in registry added new donation amount!")
                    break
                # if name not in list add new name to donor info list
            else:
                donor_info.append((donor_name, [donor_amount]))
                print(f"New donor name '{donor_name}' added to registry!")
                #print(donor_info) #- for testing
                break

            input("\nPress Enter for Thank You letter:\n")
            print(f'''Dear {donor_name},

Thank you for your donation of '${donor_amount}' to XYZ Nonprofit for children! It really makes a huge impact for the children 
in our community.

Those three hours after the end of the school day can make a crucial difference in kids’ lives.
Thanks to you, kids have a safe place to go after school. Instead of going home alone while their families are at work,
our kids are learning to play sports, create art, and improving their grades at our Homework Help Center.  All while
forming friendships with peers and relationships with adult mentors and tutors.

Thank you again {donor_name}, for your ongoing support of our kids!

Sincerely,

XYZ Nonprofit Agency Director
''')
            input("Press Enter to Continue")
            break

###############################################
#   #2 Create a Report
###############################################
def report():
    ''' Report: creates a tabular summary report of donor transactions'''
    while (True):
    # title
        donor_sort = []
        title = "*******************  XYZ Nonprofit Charity  ********************\n" \
                        "________________________________________________________________"
        heading_name = ("| Donor Name:", "| Totals $:", "| #-of-Gifts:", "| Avg Gift $: ", "|")
        header = f"{heading_name[0].upper():<20s} {heading_name[1].upper():<13s}" \
                    f" {heading_name[2].upper():<6s} {heading_name[3].upper():<14s}|"
        print(title)
        print(header)
        #define format row
        row = "| {Name:<18s} | ${Total:<10.2f} | {NumbGifts:^11d} | ${AverageGifts:<10.2f} |".format
        # revisions made below to add sorting by totals
        # step #1 set-up to sort
        for i in donor_info:
            donor_sort.append([i[0], sum(i[1]), len(i[1]), sum(i[1], 0) / len(i[1])])
        # print(donor_sort) - print for testing
        # step #2 iterate and print sorted, lambda works here but itemgetter looks cleaner
        #for i in sorted(donor_sort, key=lambda donor_sort: donor_sort[1], reverse=True): # reverse descending
        for i in sorted(donor_sort, key=itemgetter(1), reverse=True): # reverse descending
            print(row(Name=i[0], Total=i[1], NumbGifts=i[2], AverageGifts=i[3]))
        print("________________________________________________________________")
        input("Press Enter to Continue")
        break

###############################################
#   #3 Exit the Program
###############################################
def exit_program():
    '''
    Will exit the program
    :return:
    '''
    while (True):
        exit_choice = input("Would you like to Exit?\nEnter 'y' or 'n': ")
        if (exit_choice.lower() == 'y'):
            print("\nExiting!")
            sys.exit()
        elif (exit_choice.lower() == 'n'):
            main()

# Main Body of Script  ------------------------------------------------------ #

if __name__ == '__main__':
    main()