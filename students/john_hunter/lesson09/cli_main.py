#!/usr/bin/env python3
"""
Created on Tue Jan 12 15:01:23 2021

@author: johnh
"""

#Script runner for mailroom_oo

import donor_models
import sys
import pathlib
from operator import itemgetter
import datetime

PATH = pathlib.Path("./")
PATH.is_dir()
PATH.absolute()

#constants
initial_options = {1 : "Names", 2 : "Names and Donations", 3 : "Names, Donations, and Personal Profile"}
#report_attributes = {1: defaults, 2: address, 3: phone, 4: date, 5: status}
options = {1 :'Send a Thank You', 2 : 'Report', 3 : 'Send Thank You to all Donors', 4 : 'Exit'}
donors = ['frank merriweather', 'thomas tran', 'stephanie terrance', 'sam robidas',
          'sandy cohen', 'shioban kemp']
selections = {1 : 'Names', 2 : "Names and Donations", 3 : "Names, Donations, and Personal Profile",\
              4:'Names, Donations, and Phone Number', 5:'Names, Donations, Phone Number, Address',\
              6:'Names, Donations, Phone Number, Address, and Activity Date', \
              7:'Names, Donations, Address', 8:'Names, Donations, Address, and Activity Date',\
              9: 'Names, Donations, and Activity Date'}

now = datetime.datetime.now()

#User can read in whole data, user names only, users 
#with active accounts(donation made in the last year)
def select_initialization():
    print("Loadscreen: You may enter exit at any time")
    print("--------------Mailroom Initialization-------------")
    print("Your have the following donors:")
    print('\n'.join(map(str, donors)).title())

    #from DonorCollection print(list_of_donors)
    print("For each donor you can import the following: ")
    
    for key in initial_options:
        print(str(key)+'. '+ initial_options[key])
    
    entry = input("Enter 1, 2, or 3: ")
    
    if entry == 'exit':
        quit_it()
    if not entry.isnumeric() or int(entry) < 1 or int(entry) > 3:
        print('You must select a number 1, 2, or 3.')
        select_initialization()
    else:
        try:
            int(entry)
        except ValueError:
            select_initialization()
        print('You have selected ' + initial_options[int(entry)])
    
    
    selected = initialization(entry)
    #print(selected + 'Help')
    return selected

def initialization(initial):
    
    if initial == '1':
        #collection = []
        collection = donor_models.DonorCollection()
        for name in donors:
            collect = donor_models.Donor(name)
            collection.add_donor(collect)
            collection.donors_listed(collect)
        initial = 1
        selection = selections[initial]    
        return [collection, selection, initial]
    
    elif initial is '2': 
        collection = donor_models.DonorCollection()
        donor_thom = donor_models.Donor("Thomas Tran".lower())
        donor_thom.donations = [5, 17, 23]
        collection.add_donor(donor_thom)
        collection.donors_listed(donor_thom)
        
        donor_frank = donor_models.Donor("Frank Merriweather".lower())
        donor_frank.donations = [10, 15, 100]
        collection.add_donor(donor_frank)
        collection.donors_listed(donor_frank)
        
        donor_stephanie = donor_models.Donor("Stephanie Terrance".lower())
        donor_stephanie.donations = [31, 48, 108]
        collection.add_donor(donor_stephanie)
        collection.donors_listed(donor_stephanie)
        
        donor_shioban = donor_models.Donor("Shioban Kemp".lower())
        donor_shioban.donations = [2, 23000, 19]
        collection.add_donor(donor_shioban)
        collection.donors_listed(donor_shioban)
        
        donor_sandy = donor_models.Donor("Sandy Cohen".lower())
        donor_sandy.donations = [29, 41, 70]
        collection.add_donor(donor_sandy)
        collection.donors_listed(donor_sandy)
        
        donor_sam = donor_models.Donor("Sam Robidas".lower())
        donor_sam.donations = [4, 90, 101]
        collection.add_donor(donor_sam)
        collection.donors_listed(donor_sam)
        initial = 2
        selection = selections[initial]
        #print(initial)
        return [collection, selection, initial]
    if initial is '3':
        collection = donor_models.DonorCollection()
        donor_thom = donor_models.Donor("Thomas Tran".lower())
        donor_thom.donations = [5, 17, 23]
        collection.add_donor(donor_thom)
        collection.donors_listed(donor_thom)
        donor_thom.address = "36-81 Astor Place"
        donor_thom.phone_number = "718-218-3020"
        donor_thom.activity_date = datetime.datetime.strptime("2020-03-28", '%Y-%m-%d')
        
        donor_frank = donor_models.Donor("Frank Merriweather".lower())
        donor_frank.donations = [10, 15, 100]
        collection.add_donor(donor_frank)
        collection.donors_listed(donor_frank)
        donor_frank.address = "341 8th Avenue"
        donor_frank.phone_number = "212-432-3121"
        donor_frank.activity_date = datetime.datetime.strptime("2020-05-15", '%Y-%m-%d')
        
        donor_stephanie = donor_models.Donor("Stephanie Terrance".lower())
        donor_stephanie.donations = [31, 48, 108]
        collection.add_donor(donor_stephanie)
        collection.donors_listed(donor_stephanie)
        donor_stephanie.address = "419 Greenpoint Street"
        donor_stephanie.phone_number = "646-256-7463"
        donor_stephanie.activity_date = datetime.datetime.strptime("2020-06-01", '%Y-%m-%d')
        
        donor_shioban = donor_models.Donor("Shioban Kemp".lower())
        donor_shioban.donations = [2, 23000, 19]
        collection.add_donor(donor_shioban)
        collection.donors_listed(donor_shioban)
        donor_shioban.address = "3456 Tartan Way"
        donor_shioban.phone_number = "718-982-2648"
        donor_shioban.activity_date = datetime.datetime.strptime("2019-03-15", '%Y-%m-%d')
    
        donor_sandy = donor_models.Donor("Sandy Cohen".lower())
        donor_sandy.donations = [29, 41, 70]
        collection.add_donor(donor_sandy)
        collection.donors_listed(donor_sandy)
        donor_sandy.address = "9827 Grease Court"
        donor_sandy.phone_number = "817-495-3678"
        donor_sandy.activity_date = datetime.datetime.strptime("2021-01-04", '%Y-%m-%d')
        
        donor_sam = donor_models.Donor("Sam Robidas".lower())
        donor_sam.donations = [4, 90, 101]
        collection.add_donor(donor_sam)
        collection.donors_listed(donor_sam)
        donor_sam.address = "34 21st Street"
        donor_sam.phone_number = "387-466-2354"
        donor_sam.activity_date = datetime.datetime.strptime("2018-09-28", '%Y-%m-%d')
        initial = 3
        selection = selections[initial]
        return [collection, selection, initial]
        
def menu_prompt(included_fields, initial):
    #options = {1 :send_ty, 2 : run_report, 3 : save_emails, 4 : quit_it}
    print("Welcome to the mailroom. The Donors have been loaded with {} \
           \nThese are your options".format(included_fields))
    for key in options:
        print(str(key)+'. '+ options[key])
    
    entry = input("Enter 1, 2, or 3: ")
    
    if entry == 'exit':
        quit_it()
    if not entry.isnumeric() or int(entry) < 1 or int(entry) > 4:
        print('You must select a number 1, 2, 3, or 4.')
        menu_prompt(included_fields, initial)
    else:
        print('You have selected ' + options[int(entry)])

    return [entry, initial]

def send_ty(donor_collection, initial):
    """Returns the text of the email with the donor name, description of the
    donations
    Prompts to enter a 'Full Name' or list, if the name is not part of the
    list, then add that name to the list of donors and use the name
    Prompt for a donation amount, type as a number and enter into the dictionary
    Generate the Email thanking the donor, print it to terminal
    return to the prompt
    """
    #Provide for the possible need to format a list of the Donor names, length
    #sorted in donor list format function
    #provide for the need to sort by donation total as well
    donors = donor_collection.donors
    
    while True:
        input_named = str(input('Enter full name of donor or \'list\' to request list of donors: '))
        
        if input_named == 'list':
            print('List of Current Donors')
            for donor in donor_collection:
                print('{:{align}{width}}'.format(donor.name.title(), align='<', width=10))
            continue
        if input_named == 'exit':
            quit_it()
        input_name = input_named.lower()


        if input_name in donor_collection.donors_names:
            list_or_not = 'y' #local variable which tracks whether the user 
            # provided name is on the list of donors or not
            for entry in donors:
                if entry.name == input_name:
                    this_donor = entry
                    #print(this_donor.name)
            break

        else:
            this_donor = choice_add_donor(donor_collection, input_name)
            list_or_not = 'n'
            more_donations = 'n'
            break

    while True:
        mas_donations = 'Would you like to add more donations for ' + input_named + '? y/n: '
        if list_or_not == 'y':
            more_donations = input(mas_donations)
        if more_donations == 'y':
            #donors[input_name] = donors[input_name] + add_donations(input_name, list_or_not)
             #this needs to be called from the input choice function
            choice_add_donation(this_donor, list_or_not)
        elif more_donations == 'n':
            break
        else:
            pass
    
    print(this_donor.construct_email())

def run_report(donor_collection, initial):
    """
    Collects remaining formatting and prints an ordered list of the donors by donation total
    """
    """
    selections = {1 : 'Names', 2 : "Names and Donations", 3 : "Names, Donations, and Personal Profile",\
              4:'Names, Donations, and Phone Number', 5:'Names, Donations, Phone Number, Address',\
              6:'Names, Donations, Phone Number, Address, and Activity Date', \
              7:'Names, Donations, Address', 8:'Names, Donations, Address, and Activity Date',\
              9: 'Names, Donations, and Activity Date'}"""
    selections_order = {1 : 2, 2: 5, 3: 7, 4: 5, 5: 5 , 6: 7 ,7: 5 ,8: 7 , 9: 7}
    print_ordered = donor_collection
    print_order = donor_collection.donors
    #print(len(initial))
    
    if isinstance(initial, int):#<class 'int'>:
        #continue_with_defaults = 'y'
    
        print('Reports can include different attribute sets')
        
        #initial = str(initial)
        #print(type(initial))
        #print(selections[initial])
        
        while True:
            continue_with_defaults = input('Would you like to use the default attributes(n) or extend(y)?')
            continue_with_defaults.lower()
            try:
                (continue_with_defaults == 'y' or continue_with_defaults == 'n' or\
                 continue_with_defaults == 'exit') == True
                break
            except:
                print('enter a valid value')
                continue
        if continue_with_defaults == 'exit':
            quit_it()
        elif continue_with_defaults == 'y':
            extended = choice_extend(donor_collection, initial)
            donor_collection = extended[0]
            print_ordered = donor_collection
            initial = extended[1]
        else:
            the_list = view_attributes(donor_collection, initial=[])#gets the updated list of attributes
            donor_collection = the_list[0]
            print_ordered = donor_collection
            print_order = donor_collection.donors
            initial = the_list[1]
            the_list = the_list[2]
    else:
        the_list = view_attributes(donor_collection, initial=[])#gets the updated list of attributes
        donor_collection = the_list[0]
        print_ordered = donor_collection
        print_order = donor_collection.donors
        initial = the_list[1]
        the_list = the_list[2]
    print(the_list)
    #sett = ['First Name', 'Last Name', 'Donations', 'Phone Number', 'Activity Date', 'Address']
    sorting_attributes = ['1. Alphabetically by First Name','2. Alphabetically by Last Name',\
                          '3. By Donation Total','4. By number of Donations'\
                          ,'5. By Average Donation','6. By Date of Last Donation'\
                          ,'7. Status']
    max_len_of_address = 0
    if the_list == ['First Name', 'Last Name']:
        choice = selections_order[1]
        attr = 1
    if the_list == ['First Name', 'Last Name', 'Donations']:
        choice = selections_order[2]
        attr = 2
    if the_list == ['First Name', 'Last Name', 'Donations', 'Phone Number', 'Activity Date', 'Address']:
        choice = selections_order[3]
        attr = 3
        for item in print_order:  #get max length of any donor's name
            if len(item.address) > max_len_of_address:
                max_len_of_address = len(item.address)
    if the_list == ['First Name', 'Last Name', 'Donations', 'Phone Number']:
        choice = selections_order[4]
        attr = 4
    if the_list == ['First Name', 'Last Name', 'Donations', 'Phone Number', 'Address']:
        choice = selections_order[5]
        attr = 5
        for item in print_order:  #get max length of any donor's name
            if len(item.adress) > max_len_of_address:
                max_len_of_address = len(item.address)
    if the_list == ['First Name', 'Last Name', 'Donations', 'Phone Number', 'Activity Date', 'Address']:
        choice = selections_order[6]
        attr = 6
        for item in print_order:  #get max length of any donor's name
            if len(item.address) > max_len_of_address:
                max_len_of_address = len(item.address)
    if the_list == ['First Name', 'Last Name', 'Donations', 'Address']:
        choice = selections_order[7]
        attr = 7
        for item in print_order:  #get max length of any donor's name
            if len(item.address) > max_len_of_address:
                max_len_of_address = len(item.address)
    if the_list == ['First Name', 'Last Name', 'Donations', 'Activity Date', 'Address']:
        choice = selections_order[8]
        attr = 8
        for item in print_order:  #get max length of any donor's name
            if len(item.address) > max_len_of_address:
                max_len_of_address = len(item.address)
    if the_list == ['First Name', 'Last Name', 'Donations', 'Activity Date']:
        choice = selections_order[9]
        attr = 9
    
    max_len_of_name = 0
    for item in print_order:  #get max length of any donor's name
        if len(item.name) > max_len_of_name:
            max_len_of_name = len(item.name)
    
    #print(sorting_attributes[1])
    #print(sorting_attributes[1] in sorting_attributes[:choice])
    while True:
        print('The report can be sorted:')
        
        for item in sorting_attributes[:choice]:
            print(item)
        
        ordering = input('Please Enter the Number: ')
        if ordering.lower() == 'exit':
            quit_it()
        try:
            #print(sorting_attributes[ordering])
            #print('k')
            #print(sorting_attributes[:choice])
            (sorting_attributes[ordering] in sorting_attributes[:choice]) == True
            break
        except:
            print('You must enter a number.')
            #run_report(donor_collection, initial)
        try:
            ordering.isnumeric() == True
            break
        except:
            print('You must enter a number.')
            run_report(donor_collection, initial)
    
    print_for_total = []
    print(initial)
    if initial == 3:
        for donor in print_order:
            donor.get_status()
    
    if ordering == '1':
        print_ordered = sorted(print_order, key= lambda x:(x.name))
    elif ordering == '2':
        for donor in print_order:
            print_for_total.append([donor, donor.last()])
        print_for_total = sorted(print_for_total, key = itemgetter(1))
        print_ordered = [item[0] for item in print_for_total]
    elif ordering == '3':
        for donor in print_order:
            print_for_total.append([donor, donor.get_total()])
        print_for_total = sorted(print_for_total, key = itemgetter(1), reverse = True)
        print_ordered = [item[0] for item in print_for_total]
    elif ordering == '4':
        for donor in print_order:
            print_for_total.append([donor, donor.number_of_donations()])
        print_for_total = sorted(print_for_total, key = itemgetter(1), reverse = True)
        print_ordered = [item[0] for item in print_for_total]
    elif ordering == '5':
        for donor in print_order:
            print_for_total.append([donor, donor.average()])
        print_for_total = sorted(print_for_total, key = itemgetter(1), reverse = True)
        print_ordered = [item[0] for item in print_for_total]
    elif ordering == '6':
        print_ordered = sorted(print_order, key= lambda x:(x.activity_date), reverse = True)
    elif ordering == '7':
        print_ordered = sorted(print_order, key= lambda x:(x.status), reverse = True)
    
    extra_len = len(the_list)-3
    head1 = '{:{align}{width}}'.format('Donor Name', align='^', width=max_len_of_name) \
          +  ' | Total Donations | Number of Donations | Avg Donation' 
    head2 = ' '.join([item + ' | ' for item in the_list[3:]])
    
    print(head1 + head2)
    print('-'*max_len_of_name + '-------------------------------------------------------'+'\
          ---------'*extra_len+'-'*max_len_of_address)

    for donor in print_ordered:
        if attr == 1 or attr == 2:
            total = donor.get_total()
            number = donor.number_of_donations()
            average = donor.average()
            person = donor.name.title()
            print('{:{align}{width}}'.format(person, align='<', width=max_len_of_name) + \
            ' ' + '{:{align}{width}.0f}'.format(total, align='^', width=17) + \
            ' ' + '{:{align}{width}}'.format(number, align='^', width=21) + \
            ' ' + '{:{align}{width}.2f}'.format(average, align='^', width=15))
        if attr == 3 or attr == 6:
            total = donor.get_total()
            number = donor.number_of_donations()
            average = donor.average()
            person = donor.name.title()
            phone = donor.phone_number
            act = donor.activity_date
            addy = donor.address
            status = donor.get_status()
            print('{:{align}{width}}'.format(person, align='<', width=max_len_of_name) + \
            ' ' + '{:{align}{width}.0f}'.format(total, align='^', width=17) + \
            ' ' + '{:{align}{width}}'.format(number, align='^', width=21) + \
            ' ' + '{:{align}{width}.2f}'.format(average, align='^', width=15)+\
            ' ' + '{:{align}{width}}'.format(phone, align='^', width=14)+\
            ' ' + '{:{align}{width}}'.format(act, align='^', width=12)+\
            ' ' + '{:{align}{width}}'.format(addy, align='^', width=max_len_of_address)+\
            ' ' + '{:{align}{width}}'.format(status, align='^', width=12))
        if attr == 4:
            total = donor.get_total()
            number = donor.number_of_donations()
            average = donor.average()
            person = donor.name.title()
            phone = donor.phone_number
            #act = donor.activity_date()
            #addy = donor.address()
            #status = donor.status()
            print('{:{align}{width}}'.format(person, align='<', width=max_len_of_name) + \
            ' ' + '{:{align}{width}.0f}'.format(total, align='^', width=17) + \
            ' ' + '{:{align}{width}}'.format(number, align='^', width=21) + \
            ' ' + '{:{align}{width}.2f}'.format(average, align='^', width=15)+\
            ' ' + '{:{align}{width}}'.format(phone, align='^', width=14))
        if attr == 5:
            total = donor.get_total()
            number = donor.number_of_donations()
            average = donor.average()
            person = donor.name.title()
            phone = donor.phone_number
            #act = donor.activity_date()
            addy = donor.address
            #status = donor.status()
            print('{:{align}{width}}'.format(person, align='<', width=max_len_of_name) + \
            ' ' + '{:{align}{width}.0f}'.format(total, align='^', width=17) + \
            ' ' + '{:{align}{width}}'.format(number, align='^', width=21) + \
            ' ' + '{:{align}{width}.2f}'.format(average, align='^', width=15)+\
            ' ' + '{:{align}{width}}'.format(phone, align='^', width=14)+\
            ' ' + '{:{align}{width}}'.format(addy, align='^', width=max_len_of_address))
        if attr == 7:
            total = donor.get_total()
            number = donor.number_of_donations()
            average = donor.average()
            person = donor.name.title()
            #phone = donor.phone_number()
            #act = donor.activity_date()
            addy = donor.address
            #status = donor.status()
            print('{:{align}{width}}'.format(person, align='<', width=max_len_of_name) + \
            ' ' + '{:{align}{width}.0f}'.format(total, align='^', width=17) + \
            ' ' + '{:{align}{width}}'.format(number, align='^', width=21) + \
            ' ' + '{:{align}{width}.2f}'.format(average, align='^', width=15)+\
            ' ' + '{:{align}{width}}'.format(addy, align='^', width=max_len_of_address))
        if attr == 8:
            total = donor.get_total()
            number = donor.number_of_donations()
            average = donor.average()
            person = donor.name.title()
            #phone = donor.phone_number()
            act = donor.activity_date
            addy = donor.address
            status = donor.get_status()
            print('{:{align}{width}}'.format(person, align='<', width=max_len_of_name) + \
            ' ' + '{:{align}{width}.0f}'.format(total, align='^', width=17) + \
            ' ' + '{:{align}{width}}'.format(number, align='^', width=21) + \
            ' ' + '{:{align}{width}.2f}'.format(average, align='^', width=15)+\
            ' ' + '{:{align}{width}}'.format(act, align='^', width=12)+\
            ' ' + '{:{align}{width}}'.format(addy, align='^', width=max_len_of_address)+\
            ' ' + '{:{align}{width}}'.format(status, align='^', width=12))
        if attr == 9:
            total = donor.get_total()
            number = donor.number_of_donations()
            average = donor.average()
            person = donor.name.title()
            #phone = donor.phone_number()
            act = donor.activity_date
            #addy = donor.address()
            status = donor.get_status()
            print('{:{align}{width}}'.format(person, align='<', width=max_len_of_name) + \
            ' ' + '{:{align}{width}.0f}'.format(total, align='^', width=17) + \
            ' ' + '{:{align}{width}}'.format(number, align='^', width=21) + \
            ' ' + '{:{align}{width}.2f}'.format(average, align='^', width=15)+\
            ' ' + '{:{align}{width}}'.format(act, align='^', width=12)+\
            ' ' + '{:{align}{width}}'.format(status, align='^', width=12))
def choice_add_donor(donors, input_name):
    """
    function receives the value of the new donor's name, and requests that
    donation values values be added for that donor and calls the add donations function
    input variable name is the new donor to be added
    return none
    """
    print("The donor you entered was not on the list")
    while True:
        choice = input("Would you like to add a new donor?(y/exit)")
        if choice.lower() == 'exit':
            quit_it()
        elif choice.lower() == 'y':
            break
        else:
            print('You entered an invalid value')
            continue
    
    list_or_not = 'n'
    this_donor = donor_models.Donor(input_name)
    donors.add_donor(this_donor)
    print('You will need to add donations for ' + input_name.title() + ' by entering the values as requested: ')
    list_or_not = 'n'
    return choice_add_donation(this_donor, list_or_not)
    
    
def choice_add_donation(this_donor, list_or_not):
    """
    adds donations to the selected donor. The donor may be from the initial donors list
    or it could be added by the use
    input variable determines whether the selected donor is on the list already or not
    returns the donations by donor
    """
    if list_or_not == 'y':
        print("Add donations to this donor?")
    update_or_not = input("would you like to update the account activity date to today's date?(y/n)")
    try:
        (update_or_not.lower() == 'y' or update_or_not.lower() == 'n' or update_or_not == 'exit') == True
        if update_or_not == 'y':
            this_donor.update_date()
        elif update_or_not == 'exit':
            quit_it()
        else:
            pass
    except:
        choice_add_donation(this_donor, list_or_not)
    
    while True:
        donation = int(input('Enter a donation amount, enter \'0\' for no donation: '))
        if donation == 0:
            break
        elif list_or_not == 'n':
            this_donor.donations.append(donation)
            continue
        else:
            this_donor.donations.append(donation)
    return this_donor

#allow the user to select to read in data in two styles, one for sending/viewing 
#emails(names, and totals) or a full report of all data on the donor

def edit_donor(extended):
    donor_collection = extended[0]
    initial = extended[1]
    print(initial)
    
    print("You have selected to add attributes to the donors. Please Enter values in the given formats")
    donor_print = donor_collection.donors
    
    for donor in donor_print:
        for item in initial:
            if item == 'Activity Date':
                donor.activity_date = input('Enter Activity Date in the  given format: ')
            if item == 'Address':
                donor.address = input('Enter Address in given format:')
            if item == 'Last Name':
                donor.last = input('Enter the last name of the donor: ')
            if item == 'Donations':
                add_donations(donor)
            if item == 'Phone Number':
                donor.phone_number = input('Enter the donor phone number in the given format: ')
    initial = [1, initial]
    print(initial)
    print('what')
    run_report(donor_collection, initial)
    #many = len(attributes_options_call[initial])
    #for donor in print_order:
    #    for item in attributes_options_call[initial]:
    #        print(donor.attributes_options_call[initial][item]())
    #print(type(donor_print))
# offer 4 choices of type, mailing address, active account(Status:Yes/No) 
# calculated from one year from last donation, 
# date of last donation, and phone number
def choice_extend(donor_collection, initial):
    attribute_name = ['First Name', 'Last Name', 'Donations', 'Phone Number', 'Activity Date', 'Address']
    if initial == 1:
        first_initial = 1
    if initial == 2:
        first_initial = 2
    if initial == 3:
        first_initial = 3
    
    attributes = view_attributes(donor_collection, initial)
    
    donor_collection = attributes[0]
    initial = attributes[1]
    attributes = attributes[2]
    available = list()
    
    for item in attribute_name:
        if item not in attributes:
            available.append(item)
    if available == []:
        extended = [donor_collection, initial]
        return extended
    
    while True:
        print("You have selected add user data field:")
        i = 0
        for item in available:
            i = i + 1
            print(str(i) + '. ' + item)
        
    
        try:
            
            select_attributes = list(map(int, input('Select any of the available attrbiutes by number, seperated by a space: ').split()))
            break
            if select_attributes[0].lower() == 'exit':
                quit_it()
            elif len(select_attributes) > len(available):
                select_attributes = list()
                print('You have selected too many')
                
                continue
            elif any([((int(item) < 0 or item > len(available))) for item in select_attributes]):
                print('Out of range entry, please try again.')
                select_attributes = list()
                break
                continue
            break
        except:
            break
            print('Unknown Error, try again')
            continue
    
    print(available)
    print('j')
    print(select_attributes)
    initial = []
    for item in select_attributes:
        initial.append(available[item-1])
        
    
    extended = [donor_collection, initial]
    return edit_donor(extended)

def view_attributes(donor_collection, initial):
    collection = donor_collection.donors    
    the_list = list()
    attribute_name = ['First Name', 'Last Name', 'Donations', 'Phone Number', 'Activity Date', 'Address']
    i = 0
    max_len = len(collection)
    first_is_empty = [0] * max_len
    last_is_empty = [0] * max_len
    donations_is_empty = [0] * max_len
    phone_is_empty = [0] * max_len
    date_is_empty = [0] * max_len
    address_is_empty = [0] * max_len
    all_attributes = [first_is_empty, last_is_empty, donations_is_empty, phone_is_empty, date_is_empty, address_is_empty]
    
    for donor in collection:
        if donor.first == None:
            print(donor.name.title() + ' has no ' + attribute_name[0])
            first_is_empty[i] = 1
        if donor.last == None:
            print(donor.name.title() + ' has no ' + attribute_name[1])
            last_is_empty[i] = 1
        if donor.donations == []:
            print(donor.name.title() + ' has no ' + attribute_name[2])
            donations_is_empty[i] = 1
        if donor.phone_number == '':
            print(donor.name.title() + ' has no ' + attribute_name[3])
            phone_is_empty[i] = 1
        try:
            donor.activity_date.date != None 
        except AttributeError:
            print(donor.name.title() + ' has no ' + attribute_name[4])
            date_is_empty[i] = 1
        if donor.address == "":
            print(donor.name.title() + ' has no ' + attribute_name[5])
            address_is_empty[i] = 1
        i = i + 1
    i = 0
    print(sum(date_is_empty))
    for item in all_attributes:    
        still_empty = sum(item)
        #print(still_empty)
        if still_empty == 0:
            the_list.append(attribute_name[i])
        i= i + 1  
        #is_empty = [0, 0, 0, 0, 0]
    if isinstance(initial, list):
        return [donor_collection, initial, the_list]
        #list_of_attributes.append(attributes)
    print('The current set of attributes selected is:')
    print(selections[initial])
    
    print('These are the attributes that are present for all donors')    
    print(*the_list, sep = '\n')
            
    return [donor_collection, initial, the_list]
#saves emails, mailing address, return address, and gift receipt
def save_emails(donor_collection, initial):
    for key in donors:
        total = sum(donors[key])
        with open(f"{key}.txt", "w") as location:
            location.write(email_text(key, total))
#saves reports for either tax purposes or for permanent in house record keeping
def save_report():
    """
    Allows a snap shot of the current report
    """
    
    with open(f"{key}.txt", "w") as location:
        location.write(report_text(stuff))

def quit_it():
    """
    offers the user a quick exit from the script
    """
    sys.exit(0)

def main():
    
    options_call = {'1' : send_ty, '2' : run_report, '3' : save_emails, '4' : quit_it}
    while True:
        included_fields = select_initialization()
        #print(included_fields)
        while True:
            donor_list = included_fields[0]
            initial = included_fields[2]
            donor_collection = donor_list
            option = menu_prompt(included_fields[1], initial)
            if option[0] == '4':
                quit_it()
            options_call[option[0]](donor_collection, initial)
        
    if __name__ == '__main__':
        True
main()