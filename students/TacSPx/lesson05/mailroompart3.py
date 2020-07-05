# ---------------------------------------------------------------------------- #
# Title: mailroom part 3
# Description: A program that holds a list of donors and amounts they donated.
#              Prompt the user to choose 3 menu actions; thank you, report, quit.
#
# <05/30/2020>, Created Script, mailroom part 1
# <06/12/2020>, Clean-up to snake case, adding sorting in reporting descending totals
# <06/13/2020>, Fixed indentation error
# <06/18/2020>, mailroom part 2, Modified data struct to dicts, updated dict switch for
#               users selections, & thank you letter to write to file
# <06/22/2020>, Code clean-up, split off (report) sorting into a new function
# <06/24/2020>, Added sort_key function, simplified report sort function
# <06/27/2020>, mailroom part 3, Error handling
#
# ---------------------------------------------------------------------------- #
# imports
import sys

# Data ---------------------------------------------------------------------- #

donor_info = {"Jim Zorn": [3772.32, 1201.17],
              "Jermaine Kearse": [877.33],
              "Marcus Trufant": [1563.23, 1043.87, 1.32],
              "K.J. Wright": [21663.23, 300.87, 100432.00],
              "Curt Warner": [663.23, 300.87, 10432.00],
              }


# Processing  --------------------------------------------------------------- #

###############################################
#   "Menu of Choices"
###############################################
def main():
    '''
    Menu of Choices:  Thank You, Report, Create a Report
    :return:
    '''
    switch_choice_dict = {"1": thank_you, "2": report, "3": all_thank_you, "4": exit_program}
    while True:
        print("""
        \n**** XYZ Nonprofit Charity ****\n
        Menu of Options
        1) Send a "Thank You"
        2) Create a Report
        3) Send letters to all Donors
        4) Exit Program
        """)
        # User menu input
        menu_choice = str(input("Which option would you like to perform? [1 to 4] - "))
        print()  # added a new line for spacing looks
        # dict switch choice, if not a menu choice then run non_selection function
        switch_choice_dict.get(menu_choice, non_selection)() # error handling if not a selection


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
    while True:
        donor_name = input("Type 'List' to see all names in Database or\nType First and Last Name: ").title()
        if donor_name == "": # error handling
            input("Please enter a valid 'name'! Press 'Enter' to try again")
        elif donor_name.isnumeric(): # error handling
            input("Alphabetic characters only please. Press 'Enter' to try again")
        elif donor_name.lower() == "list":
            print("\nDONOR REGISTRY:")
            donor_sort = (sorted(donor_info.keys()))  # used .keys() to sort on key
            for key in donor_sort:
                print(key)
            input("Press Enter to Continue")
            print()

        else:
            try:
                donor_amount = int(input("Enter Amount of Donation: $"))
                if donor_amount <= 0: # error handling
                    input("\nPlease enter a number higher than '0'! Press 'Enter' to start again")
                    return
            except ValueError: # error handling
                input("please only choose a 'Number'! Press 'Enter' to start again.")
                return
            # if name is in dict append dollar amount to donors bucket, use get() to check for keys in dict
            if donor_info.get(donor_name):
                donor_info[donor_name].append(donor_amount)
                print(f"'{donor_name}' is in registry added new donation amount!")
                input("\nPress enter to continue to 'Thank You' letter:")
                print(letter(donor_name, donor_amount))
                # print(donor_info)  # - for testing
                break
            # if name not in list add new name to donor info list
            else:
                donor_info.setdefault(donor_name, []).append(donor_amount)
                print(f"New donor name '{donor_name}' added to registry!")
                input("\nPress enter to continue to 'Thank You' letter:")
                # print(donor_info)  # - for testing
                print(letter(donor_name, donor_amount))
                break


def letter(donor_name, donor_amount):
    new_letter = f'''Dear {donor_name},

Thank you for your recent donation of '${donor_amount}' to XYZ Nonprofit for children! It really makes a huge impact for
the children in our community.

Those three hours after the end of the school day can make a crucial difference in kids’ lives.
Thanks to you, kids have a safe place to go after school. Instead of going home alone while their families are at work,
our kids are learning to play sports, create art, and improving their grades at our Homework Help Center.  All while
forming friendships with peers and relationships with adult mentors and tutors.

Thank you again {donor_name}, for your ongoing support of our kids!

Sincerely,

XYZ Nonprofit Agency Director
'''
    return new_letter


###############################################
#   #2 Create a Report
###############################################
def sort_key(item):
    return sum(item[1])


def report():
    ''' report: creates a tabular summary report of donor transactions'''
    while True:
        title = "*******************  XYZ Nonprofit Charity  ********************\n" \
                "________________________________________________________________"
        heading_name = ("| Donor Name:", "| Totals $:", "| #-of-Gifts:", "| Avg Gift $: ", "|")
        header = f"{heading_name[0].upper():<20s} {heading_name[1].upper():<13s}" \
                 f" {heading_name[2].upper():<6s} {heading_name[3].upper():<14s}|"
        print(title)
        print(header)
        sorted_donors = sorted(donor_info.items(), key=sort_key, reverse=True)
        for donor, donations in sorted_donors:
            totals = sum(donations)
            numb_gifts = len(donations)
            avg_gift = totals / numb_gifts
            print(f"| {donor:<18s} | ${totals:<10,.2f} | {numb_gifts:^11d} | ${avg_gift:<10,.2f} |")
        print("________________________________________________________________")
        input("Press Enter to Continue")
        return

###############################################
#   #3 Send letters to all Donors/ download thank you files
###############################################
def all_thank_you():
    ''' Prints thank you letters for all donors'''

    print("This will create 'Thank You' letters for all donors")
    while True:
        choice = input("Are you sure?\nEnter 'y' or 'n': ")
        if choice.lower() == 'y':
            for i in donor_info:
                donor_name = i.strip()
                donor_amount = format(donor_info[i][-1], '.2f')  # last donation received
                # print(donor_name, donor_amount) # for testing
                all_letters = letter(donor_name, donor_amount)
                # creates the thank you letter in a text file
                try:  # error handling
                    with open(donor_name + ".txt", "w") as f:  # use donor name as file name
                        f.write(all_letters)
                except IOError:
                    print("'Thank you letters' could not be created in source location, possible write-protected"
                          " or read-only error")
            input("\nCompleted creating Letters! Please check program directory for files \nPress Enter to Continue!")
            break

        elif choice.lower() != 'y':
            return


###############################################
#   #4 Exit the Program/ Not a menu selection
###############################################
def exit_program():
    '''
    Will exit the program
    :return:
    '''
    while True:
        exit_choice = input("Would you like to Exit?\nEnter 'y' or 'n': ")
        if exit_choice.lower() == 'y':
            print("\nExiting!")
            sys.exit()
        elif exit_choice.lower() == 'n':
            return


def non_selection(): # error handling
    '''
    Message that selection is invalid, error handling if not a valid selection
    :return:
    '''
    print("\nNon-valid selection, please choose only: 1, 2, 3, or 4!")


# Main Body of Script  ------------------------------------------------------ #

if __name__ == '__main__':
    main()
