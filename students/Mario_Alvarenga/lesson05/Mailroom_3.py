#!/usr/bin/env python3
#Mario Alvarenga
#Lesson05
#Mailroom part 3


#LESSON 5 - CLEAN UP CODE

import sys
import os


#Version control for testing

i_VERSION = 3
# Creating the donor data base


#Lesson 4
dict_donors = {'Lionel Messi': [12450, 49563, 65897, 58690],
               'Cristiano Ronaldo':[65000, 98520],
               'Robert Lewandowski':[85005,48912,856940],
               'Neymar Dos Santos':[26598, 74158],
               'Karim Benzema':[865204, 58740, 15069]}

#This serves as the s_menu to initally face the user
s_menu = '\n'.join(['\n*************','Welcome to the FIFA World Donation Center ',
            'Please input the number representing the action you want taken.',
            '1 - Send a Thank You to a single donor.',
            '2 - Create a report.',
            '3 - Send letters to ALL donors',
            '4 - Quit',
            '*********', '','','Input > '])

def f_get_donor_names():
    # Generate list of donor names for lookup
    #Lesson 4
    return dict_donors.keys()

def f_get_donor_name_case(badcasing, list_dict):
    #Grabs the correct casing of the names in the list. Otherwise, return a blank string
    #Do not use list comprehension as we want to tilize the loop index to keep the correct spelling
    for name in list_dict:
        if name.lower() == badcasing.lower():
            return name

    return badcasing

def f_add_donation(donor_name, donation_amount):
    #LESSON 4 - We need to append the list in the data structure
    #Take into account case consistency
    #Take into account adding name into dictionary.
    donor_name = f_get_donor_name_case(donor_name,dict_donors.keys())
    if donor_name in dict_donors:
        dict_donors[donor_name].append(donation_amount)
    else:
        dict_donors[donor_name] = [donation_amount]

    return(True)

def f_generate_email(donor_name, donation_amount):
    # Create formatted email that can be copied & pasted
    #LESSON 4 - Use format AND dictionary

    donor_name = f_get_donor_name_case(donor_name,dict_donors.keys())
    email = 'Dear {donor[name]}, \n\tThank you for your generous donation of ${donor[amount]:.2f}!\nYour contribution will help new arrivals recieve the highest quality care possible.\nPlease know that your donation makes a world of difference.\n\nSincerly,\n\t\tThe Good Place Team'.format(donor={'name': donor_name,"amount": donation_amount})
    return(email)

def f_execute_thank_you(name):

    #User input of donation amount

    amount = input('Enter donation amount in dollars:\t$')
    # If the user wants to bail mid-entry, remove the donor that was just
    # added (if they were new) and return to main s_menu
    #avoiding dict switch because it would create too small of scope methods
    if amount.lower() == 'return':
        return
    else: # Convert donation amount to float and add name to dictionary if necessary
        amount = float(amount)

    # Add donation to database
    f_add_donation(name, amount)
    # Generate email and return to main program
    email = f_generate_email(name, amount)
    print(email)
    return


def f_write_thank_you():

    #UPDATE - Uses a dict switch
    #Add donation for new or existing donor and compose thank you message.
    #Get a current list of donors
    donor_names = f_get_donor_names()
    dict_tasks = {
        'list': print('\nCurrent list of donors: \n','\n'.join(donor_names)),
        'return': 0
        }


    response = input('\nEnter donor name:\t')
    dict_tasks.get(response,f_execute_thank_you)(response)         #yes that extra parenthesis is necessary.......

def f_send_all_letters():

    #Generates text files with thank you email templates for each donor to users desktop

    #Loop through File creations
    #
    for name in dict_donors.keys():
        #Generate text file path

        file_full_path = '{path}{subfolder}{file}.txt'.format(path = os.path.normpath(os.path.expanduser("~/Desktop")),subfolder = os.path.normpath('/'),file = name)

        #Grab amount of the latest donation
        recent_donation = dict_donors.get(name)[-1]

        #Generate email message in string
        message = f_generate_email(name,recent_donation)

        #Create file on desktop and write it with message. Save it afterwards.
        my_file = open(file_full_path,'w+')
        my_file.write(message)
        my_file.close()

        #Log Path of where text file has exported to
        print('Location of {dudes} file: {fpath}'.format(dudes = name,fpath = file_full_path))
    print('\n\n')           ##Extra whitespace
    return

def f_donor_key(donor):
    # Donor is a tuple of the form (name, total donation, number of donations, average donation)
    # Sort by total donation
    return donor[1]

def f_generate_report_data():
    donor_names = f_get_donor_names()
    # Declare and populate lists for report data
    total_donation, num_donation, avg_donation = [], [], []

    #Lesson 4 - Use dictionary structure. Do not append data structure, only calculate in new variable
    for name in donor_names:
        total_donation.append(sum(dict_donors.get(name,0)))
        num_donation.append(len(dict_donors.get(name,0)))
        avg_donation.append(total_donation[-1]/num_donation[-1])


    #LESSON 4
    report = list(zip(donor_names, total_donation, num_donation, avg_donation))
    # Sort by total donation, descending
    report.sort(key=f_donor_key, reverse=True)
    return report

def f_print_formatted_report(report):
    # Generate formatted report to be printed
    # Input 'report' is expected to be a list of lists with
    # [donor name, total donation, number of donations, average donation]
    formatted_report = ['',
    'Donor Name                    | Total Donation | Num Donations | Avg Donation |',
    '-------------------------------------------------------------------------------']
    #for donor in report:
    #    donor_name, total, number, average = donor
    #    formatted_report.append(f'{donor_name:<30} ${total:>14.2f}  {number:14d}  ${average:>12.2f}')
    #formatted_report.append('')
    #
    #LESSON 5 - ADDED LOOP COMPREHENSION
    print('\n'.join(formatted_report + [f'{donor_name:<30} ${total:>14.2f}  {number:14d}  ${average:>12.2f}' for donor_name, total, number, average in report]))
    #print('\n'.join(formatted_report))

def f_create_report():
    # Generate, format, and print report data
    report = f_generate_report_data()
    f_print_formatted_report(report)

def f_exit_program():
    print('Exiting program...')
    sys.exit()

def f_print_error():

    #Using dict switch, inputs into the switch function cannot specialize for one function. Therefore, made seperate method.
    message1 = 'Not a valid option. Please try again!'
    print(message1)

def main():
    # Main function, repeatedly display menu and react based on user input
    dict_tasks = {
        '1': f_write_thank_you,
        '2': f_create_report,
        '3': f_send_all_letters,
        '4': f_exit_program
        }
    while True:
        response = input(s_menu)
        dict_tasks.get(response,f_print_error)()         #yes that extra parenthesis is necessary.......

#
#Run main
#
if __name__ == "__main__":
    # Driver for main function
    main()

