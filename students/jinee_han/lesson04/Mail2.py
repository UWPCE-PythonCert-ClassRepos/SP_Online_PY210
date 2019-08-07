# --------------------------------
# 07/14/19 Jinee Han
# Python Programming Lesson 4
# Mailroom Part 2
# ---------------------------------

'''
update
1. Use dicts for the doner_db
2. Use a dic to switch between the users selections.
3. use a dic and .format() to produce the letter
4. Write a full letter to all donors to individual files on disk.
'''

import sys, datetime

# Donor List
donor_db = {"Kim Kardasian": [653772.32, 12.17],
            "Kendal Jenner": [877.33],
            "Gigi Hadid": [663.23, 43.87, 1.32],
            "Justin Bieber": [1663.23, 4300.87, 10432.0],
            "Will Smith": [43.23, 4000.07, 183423.2]
            }

# Display options
prompt = "\n".join(("Welcome to the donor list!",
          "Please choose from below options:",
          "1 - Send a Thank you",
          "2 - Create a Report",
          "3 - Exit",
          ">>> "))

def send_thank_you_note():
    '''
    Check for the user input and send a thank you once user entered
    :return: nothing
    '''
    inputValue = input("Enter a full name. (Type 'list' to see the donor list)")  # Ask the name
    while inputValue == 'list':
        display_list()
        inputValue = input("Enter a full name. (Type 'list' to see the donor list)")

    if not donor_present(inputValue):
        add_donor(inputValue)

    donation_name = inputValue
    donation_amount = float(input("Please enter the donation amount: "))
    add_donation_amount(donation_name, donation_amount)
    format_thank_you_note(donation_name, donation_amount)

def add_donation_amount(donation_name, donation_amount):
    '''
    Add the donation amount for the current donator
    :param donation_name:
    :param donation_amount:
    :return: nothing
    '''
    donor_db[donation_name].append(donation_amount)

def donor_present(donor_name):
    '''
    Check if the donor name is present in the dictionary
    :param donor_name:
    :return: True if donor present, False if not
    '''
    donor_present = False
    if donor_name in donor_db.keys():
        donor_present = True

    return donor_present

def display_list():
    '''
    Display the list of current donors
    :return: prints donor names
    '''
    for keys in donor_db:
        print(keys)

def add_donor(donor_name):
    '''
    Add donor name to the dictionary
    :param donor_name:
    :return: nothing
    '''
    donation_history = []
    donor_db.update({donor_name:donation_history})

def save_thank_you_to_file(donor_name, donation_amount, thank_you_note_formatted):
    '''
    Save the thank you note to file
    :param donor_name: The current donor
    :param donation_amount: The donation amount
    :param thank_you_note_formatted: The formatted note to write to file
    :return: nothing
    '''
    filename = "{}_{}_{}.txt".format(donor_name, donation_amount, len(donor_db[donor_name]))
    f = open("{}".format(filename), "w")
    f.write(thank_you_note_formatted)
    f.close()

def format_thank_you_note(donator, donation_amount):
    '''
    Format the thank you note before writing to file
    :param donator: The current donator
    :param donation_amount: The donation amount
    :return: nothing
    '''
    lstObj = []
    lstObj.append("Dear {},\n\n".format(donator.title())  )
    lstObj.append("\tThank you for your very kind donation of  ${:10.2f}!\n".format(donation_amount)  )
    lstObj.append("\tIt will be put to very good use.\n\n")
    lstObj.append("\t\t\tSincerely,\n")
    lstObj.append("\t\t\t\t\t - The Team")

    thank_you_note_formatted = " ".join(lstObj)
    save_thank_you_to_file(donator.title(), donation_amount, thank_you_note_formatted)

def create_report():
    '''
    Create a report of all donators, and amounts in sorted order with most donations first
    :return: Prints values to console
    '''
    """Generate a tabular report of donation history"""
    header ='\n{:^18}|{:^13}|{:^13}|{:>13}'.format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print(header)
    print('-'*len(header))
    sorted_list = sorted(donor_db.items(), key=lambda x: sum(x[1]), reverse = True)
    for donor in sorted_list:
        total = sum(donor[1])
        num = len(donor[1])
        average = total/num
        print('{:^18} ${:>12,.2f}{:^13}  ${:>12,.2f}'.format(donor[0],total,num,average))
    print('')

def exit_program():
    '''
    Exit the program
    :return: nothing
    '''
    print("Thank you for your donations!")
    sys.exit()  # exit the interactive script

input_dict = {1: send_thank_you_note, 2: create_report, 3: exit_program}

def main():
    while True:
        response = int(input(prompt))  # continuously collect user selection
        input_dict.get(response)()

if __name__ == "__main__":
    main()