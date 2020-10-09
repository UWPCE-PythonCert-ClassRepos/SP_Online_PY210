#!/usr/bin/env python3

#+--------------------------+
#| Mailroom pt.2 - Lesson 4 |
#+--------------------------+


import sys  
#to cleanly exit out of the program should the user select to.

import os.path
#to get current working directory to write and place the email_all() files into


#updated data structure to a dict using 'donor names' as the keys and the respective list of donations as values
donor_dict = {'Jeff Bridges' : [1309.45, 7492.32], 
              'Alice Summers' : [3178.67, 9823.00], 
              'Henry Cavill' : [9132.92, 7837.50], 
              'Evie Styles' : [4592.25, 2145.90, 7314.87], 
              'Harvey Dent' : [14503.70]
              }


main_prompt = "\n".join(("Welcome to the Mailbox part 2.",
          "Please choose one of the following options:",
          "1 - Send a Thank You.",
          "2 - Create a Report",
          "3 - Write Emails to All",
          "4 - Quit Program",
          ">>> "))


current_dir = os.getcwd()
#initialized in global namespace so that can confirm where files written in email_all() function


def send_thank_you():

    prompt_name = "\n".join(("Please enter the full name of a donor currently in the database.",
                "Otherwise, enter a new full name to add a new (donor, donations[]) entry in that name.",
                "(You may type 'list' to see all current donor names in database, or type 'q' to go back.)",
                ">>> "))  
    while True:
        donor_name = input(prompt_name) 
        if donor_name.lower() == 'list':
            view_donor_names()
            print()
        elif donor_name.lower() == 'q':
            return    #If user wants to return to main prompt during sending thank you email
        else:
            break
    check_name(donor_name)
    new_donation = get_amount()
    add_donation(donor_name, new_donation)
    print(email_templates(donor_name, new_donation, 2))
    #new using dicts for email layout instead of the print_email(donor_name, new_donation) function from before
    

#Updated for dicts:
def view_donor_names():
    print("The donor dict contains the following donor names:\n")
    for entry in donor_dict:
        print(entry)
        #Since with dict this default refers to the keys i.e. names


def check_name(name_input):
    #check if name_input is a key in the dict:
    if name_input.title() in donor_dict:
        return  #do nothing and proceed with steps following this function call
    else:
        donor_dict[name_input.title()] = []
        #if not in donor_dict then initialize empty donation list as the 'value' associated with the added name 'key' 


def get_amount():
    prompt_amount = "Please enter a $ amount for the associated donation: \n" + ">>> "
    new_amount = float(input(prompt_amount))
    while True:
        if new_amount <= 0:
            print("Donation must be nonzero positive dollar amount, please enter an appropriate value.\n")
            new_amount = float(input(prompt_amount))  
        else:
            break
    return new_amount


#Updated for dict:
def add_donation(d_name, n_donation):
    #adding donation happens after its been checked whether input name is in db and an empty list itialized if not
    #Hence name is either already in the dict or its been created as a new entry with empty list of donations.

    donor_dict[d_name.title()].append(n_donation)  
    #adds donation to existing list 'value' associated to the name 'key' 
            
    print(email_templates(d_name, n_donation, 1))
    #added using template dict and new function as confirmation that new donation was added to donor's donation list


#Updated for dicts: specifically building up the donor history tuples list by collecting the data from donor_dict
def create_report():
    donor_history = []
    for donor_name, amounts in donor_dict.items():  
        donor_history.append((donor_name.title(), sum(amounts), len(amounts), sum(amounts)/len(amounts)))
        #Collect and store into list of tuples structure appropriate for sorting
        
    donor_history = sorted(donor_history, key=sort_key, reverse=True) #reverse=True param sorts by highest to lowest total
    #Set the donor_history to it after having the sorted function applied 
    #sort by 2nd item in tuples i.e. by the total donation amt 
    
    hdrfmt = "| {:<25s}|{:^18s}|{:^15s}|{:^18s}|".format("Donor Name:", "Total Donated:", "# Donations:", "Donation Avg:")
    divider = "-"*len(hdrfmt) 
    rowfmt = "| {d_name:<25s}|${d_total:^17.2f}|{d_count:^15d}|${d_avg:^17.2f}|".format
    #uses format as a function to create formatting for each entry
    
    print(divider)
    print(hdrfmt) 
    print(divider)
    for d_entry in donor_history:
        print(rowfmt(d_name=d_entry[0], d_total=d_entry[1], d_count=d_entry[2], d_avg=d_entry[3]))
    print(divider, "\n")


#new added function and the added 4th option to the main menu selection
def write_email_all():
    for d_Name, d_Amounts in donor_dict.items():
        filename = "_".join(d_Name.title().split()) + ".txt"
        with open(filename, 'w') as email_file:
            email_file.write(email_templates(d_Name, sum(d_Amounts), 3))
            #produce a letter with their historical total of donations to each donor as .txt file 
            #in current directory that this program is running in
        print("Creating .txt file: ", filename, "...\n")
    print("Files written to the Current Directory: ", current_dir, "\n")
    

#new added function 
def email_templates(dname, damt, template_num):
    #function returns the appropriate template based on template_num where the layout_dict is passed to .format()
    
    layout_dict = {"donor_name" : dname.title(),
                   "donation_amount" : damt,
                   "new_pgph_indent" : '\t',
                   "line_break" : '\n\n',
                   "greeting" : "Have a positively wonderful day!",
                   "signature_indent" : ' '*25,
                   "sender_indent" : ' '*20,
                   "sender_name" : "Your Friendly Neighborhood CEOs"
                  }


    added_donation_template = "\n".join(("\n\tNew Donation Amount of: ${donation_amount:.2f} has been recorded in the donor database,",
                              "under the associated Donor Name: {donor_name}. Thanks for contributing!{line_break}")).format(**layout_dict)
    
    email_individual_template = "\n".join(("Dear {donor_name},{line_break}",
                                "{new_pgph_indent}Thank you for the generous donation of: ${donation_amount:.2f}!{line_break}",
                                "You will forever hold a place in our hearts! {greeting}{line_break}",
                                "{sender_indent}Sincerely,{line_break}",
                                "{signature_indent} - {sender_name}{line_break}")).format(**layout_dict) 
    
    email_all_template = "\n".join(("Dear {donor_name},{line_break}",
                         "{new_pgph_indent}Thank you for your repeated historical donations totalling: ${donation_amount:.2f}!{line_break}",
                         "Your long time generosity recognized you as a pillar of our community!{line_break}",
                         "{greeting}{line_break}",
                         "{sender_indent}Sincerely,{line_break}",
                         "{signature_indent} - {sender_name}{line_break}")).format(**layout_dict) 
    
    
    templates = {1 : added_donation_template,
                 2 : email_individual_template,
                 3 : email_all_template
                }
    
    return templates[template_num]


def sort_key(hist_tup):
    return hist_tup[1]   #sorted by total (historical) donation amount


def quit_program():
    print("Thank you, this program will now terminate.")
    sys.exit()


#Updated for dicts: redirect to functions based on selection using new dict structure, and call function from dict
def main():
    
    os.chdir(current_dir)
    #To ensure files get written in current working directory
    
    while True:
        response = int(input(main_prompt))  
        if response in main_menu_dict:
            main_menu_dict.get(response)()
            #fetches relevant value based on key selection which is a call to the associated feature function
        else:
            print(response, " is not a valid selection. Please enter a valid menu option value (1 - 4).\n")


main_menu_dict = {1 : send_thank_you,
                  2 : create_report,
                  3 : write_email_all,
                  4 : quit_program
                  }


if __name__ == "__main__":
    
    # block to guard against your code running automatically if this module is imported
    main()
    
    