#!/usr/bin/env python3
#Mario Alvarenga
#Lesson05
#Mailroom Part 4



#Version control for testing

i_VERSION = 4


import sys
import os


#Declare initial global list of donors
GLOBE_dict_donors = {'Lionel Messi': [12450, 49563, 65897, 58690],
          'Cristiano Ronaldo':[65000, 98520],
          'Robert Lewandowski':[85005,48912,856940],
          'Neymar Dos Santos':[26598, 74158],
          'Karim Benzema':[865204, 58740, 15069]
          }

def f_get_donor_name_case(badcasing, list_dict = GLOBE_dict_donors):
    
    #Grabs the correct casing of the names in the list. Otherwise, return a blank string
    return(''.join([name for name in list_dict if name.lower() == badcasing.lower()]))

def f_add_donation_2_list(name, amount, dict_data = GLOBE_dict_donors):
    
    #Appends to the list containing a donors amount of donations.
    #returns the data entire new data structure. Must take in original data structure.
    #data structure must be dictionary with key == donor names, values == lists of donation integers
    #Incorrect spelled names will be added as new names. Because of requirement to add new donor through this, nothing can be done about misspelled names
    
    #Take into account character casing
    name_corrected = f_get_donor_name_case(name,dict_data.keys())
    if name_corrected == '':
        dict_data[name] = [amount]
    else:
        dict_data[name_corrected].append(amount)

    return(dict_data)

def f_generate_email(name, amount, dict_data = GLOBE_dict_donors):
    # Create formatted email that can be copied & pasted
    
    #LESSON 4 - Use format AND dictionary
    name_corrected = f_get_donor_name_case(name,dict_data.keys())
    if name_corrected != '':
        name = name_corrected
    email = 'Dear {donor[name]}, \n\tThank you for your generous donation of ${donor[amount]:.2f}!\nYour contribution will help new arrivals recieve the highest quality care possible.\nPlease know that your donation makes a world of difference.\n\nSincerly,\n\t\tThe Good Place Team'.format(donor={'name': name,"amount": amount})
    return(email)

def f_execute_thank_you(name,dict_data = GLOBE_dict_donors):
    
    #Print the thank you email.
    

    #Ask user for amount donated
    amount = input('Enter donation amount in dollars:\t$')
    #Allow for bailing midway through
    if amount.lower() == 'return':
        return
    else:
        amount = float(amount)

    #Add donation to database
    dict_data = f_add_donation_2_list(name,amount,dict_data)

    
    #Generate email
    email = f_generate_email(name,amount,dict_data)
    print(email)
    return(email)

def f_thank_you_input(dict_data = GLOBE_dict_donors):
    
    #Add donation for new or existing donor and compose thank you message.
    #Get a current list of donors
    dict_tasks = {
        'list': print('\nCurrent list of donors: \n','\n'.join(dict_data.keys())),
        'return': 0
    }
    response = input('\nEnter donor name:\t')
    dict_tasks.get(response,f_execute_thank_you)(response) #Because of this notation, this will default to global variable use.
    return(dict_data)

def f_send_all_letters(dict_data = GLOBE_dict_donors):
    
    #Generates text files with thank you email templates for each donor to users desktop. Returns list of paths.

    
    #Declare blank list to populate and return
    list_paths = []

    for name in dict_data.keys():
        
        #Generate text file path
        file_full_path = '{path}{subfolder}{file}.txt'.format(path = os.path.normpath(os.path.expanduser("~/Desktop")),subfolder = os.path.normpath('/'),file = name)
        
        #Grab amount of the latest donation
        recent_donation = dict_data.get(name)[-1]
        
        #Generate email message in string
        message = f_generate_email(name,recent_donation,dict_data)
        
        #Create file on desktop and write it with message. Save it afterwards.
        my_file = open(file_full_path,'w+')
        my_file.write(message)
        my_file.close()
        
        #Log Path of where text file has exported to
        list_paths.append(file_full_path)
        if __name__ == "__main__": #Only print to stdIO when ran stand-alone, to avoid GUI errors
            print('Location of {dudes} file: {fpath}'.format(dudes = name,fpath = file_full_path))
            print('\n\n')           ##Extra whitespace
    return(list_paths)

def f_sort_criteria(total_don):
    #Sort by the donor, which is of index one in the zipper report. 
    return total_don[1]
def f_generate_report_data(dict_data = GLOBE_dict_donors):
    
    #Declare empty lists to populate before zipping
    total_don, num_don,avg_don = [],[],[]

    #Populate lists
    for name in dict_data.keys(): #because the arithmetics are simple, no seperate functions needed (and reduce testing, integrity of calculations is easy to see here)
        total_don.append(sum(dict_data.get(name,0)))
        num_don.append(len(dict_data.get(name,0)))
        avg_don.append(total_don[-1]/num_don[-1])
    report = list(zip(dict_data.keys(), total_don, num_don, avg_don))
    report.sort(key=f_sort_criteria, reverse=True)
    return report

def f_print_report(report):
    # Generate formatted report to be printed
    # Input 'report' is expected to be a list of lists with
    # [donor name, total donation, number of donations, average donation]
    formatted_report = ['',
    'Donor Name                    | Total Donation | Num Donations | Avg Donation |',
    '-------------------------------------------------------------------------------']
    formatted_report = '\n'.join(formatted_report + [f'{donor_name:<30} ${total:>14.2f}  {number:14d}  ${average:>12.2f}' for donor_name, total, number, average in report])
    print(formatted_report)
    return(formatted_report)

#Following functions (with exclusion of main) are simple integrator functions. Tests will go all in one go.

def f_create_report(dict_data = GLOBE_dict_donors):
    report = f_generate_report_data(dict_data)
    return(f_print_report(report)) #returns string of formatted report.

def f_exit_program(dict_data = GLOBE_dict_donors):
    print('Exiting program...\n')
    sys.exit()

def f_print_error(dict_data = GLOBE_dict_donors):
    message1 = 'Not a valid option. Please try again!'
    print(message1)
    return(message1)

def main(dict_data = GLOBE_dict_donors):
    #Initiates main user menu

    #Design main menu in string
    s_menu = '\n'.join(['\n*************','Welcome to the FIFA World Donation Center ',
            'Please input the number representing the action you want taken.',
            '1 - Send a Thank You to a single donor.',
            '2 - Create a report.',
            '3 - Send letters to ALL donors',
            '4 - Quit',
            '*********', '','','Input > '])
    #Create dict switch case
    dict_tasks = {
        '1': f_thank_you_input,
        '2': f_create_report,
        '3': f_send_all_letters,
        '4': f_exit_program
        }
    while True:
        response = input(s_menu)
        dict_tasks.get(response,f_print_error)(dict_data)         #yes that extra parenthesis is necessary.......

if __name__ == "__main__":
    # Driver for main function
    main()
