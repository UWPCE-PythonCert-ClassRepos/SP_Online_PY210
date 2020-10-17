#!/usr/bin/env python3

#+-----------------------------------------+
#| Mailroom Part 3 - Assign #4 of Lesson 5 |
#+-----------------------------------------+

#[x] 1.Exceptions
  # [x] - main input
  # [x] get_name, get_amount 
  # - input errors: change to safe_input
  # - value errors: add try--except blocks
  # [x] - file errors: write_file
#[x] 2.Comprehensions: new_list from dict : changes for loop to comprehension to calculate donation totals


import sys, os.path  


donor_dict = {'Jeff Bridges' : [1309.45, 7492.32], 
              'Alice Summers' : [3178.67, 9823.00], 
              'Henry Cavill' : [9132.92, 7837.50], 
              'Evie Styles' : [4592.25, 2145.90, 7314.87], 
              'Harvey Dent' : [14503.70]
              }


main_prompt = "\n".join(("Welcome to the Mailroom - Part 3.",
          "Please choose one of the following options:",
          "1 - Send a Thank You.",
          "2 - Create a Report",
          "3 - Write Emails to All",
          "4 - Quit Program",
          ">>> "))


current_dir = os.getcwd()


# New helper function for when any text input to prompt may get inadvertantly interrupted 
# or cause the program to inadvertantly crash due to unexpected exit such as via keyboard shortcut (ctrl+D exit)
def safe_input(prompt = ''):
    try:
        result = input(prompt+"\n")
    except (KeyboardInterrupt, EOFError):
        result = None
    return result


def write_file(fname,text):
# Catch File Open Exceptions
    try:                            
        file = open(fname,'w')
    except (OSError, IOError):
        print("File Open Error occured for: ",fname)
        
# Catch File Write Exceptions
    try:                            
        file.write(text)
        file.close()
        print("Written to .txt file:",fname,"...\n")
    except (OSError, IOError):
        print("File Write Error occured for: ",fname)


# Change this to accomodate try--except input checks
def send_thank_you():

    prompt_name = "\n".join(("Please enter the full name of a donor currently in the database.",
                  "Otherwise, enter a new full name to add a new (donor, donations[]) entry in that name.",
                  "(You may type 'list' to see all current donor names in database, or type 'q' to go back.)",
                  ">>> "))  
    while True:
        # donor_name = input(prompt_name) 
        donor_name = safe_input(prompt_name)
        if donor_name.lower() == 'list':
            view_donor_names()
            print()
        elif donor_name.lower() == 'q':
            return    #If user wants to return to main prompt during sending thank you email
        elif donor_name:
            break
        else:
            continue

    new_donation = get_amount()
    add_donation(donor_name, new_donation)
    print(email_templates(donor_name, new_donation, 2))
    # send to second layout fuction option for send-thank-yous
    

# unchanged
def view_donor_names():
    print("The donor dict contains the following donor names:\n")
    for entry in donor_dict:
        print(entry)
        #Since with dict this default refers to the keys i.e. names


def get_amount():
    prompt_amount = "Please enter a $ amount for the associated donation: \n" + ">>> "    
    while True:
        # new_amount = float(input(prompt_amount)) 
        # but for now wait to convert to float in case option to go back 'q' typed in by user 
        
        # encase testing for float conversion of new_amount in try--except block,
        # then if input value cannot be converted to float: ValueError will be raised
        try:
            new_amount = float(safe_input(prompt_amount))
        except ValueError:
            print("Invalid input: Please enter a nonzero positive decimal number (that can be converted to a float).\n")
            continue 
            # throw the loop for another round until something changes.            
        else: 
            if new_amount > 0:
                break    # value finally > 0 and decimal exit the loop and return the amount
            else:
                print("Invalid input: Please enter a nonzero positive decimal number.\n")
                continue # try again
    # return value when finally acceptable positive decimal number input
    return new_amount


# replaces functionality of check_name() function as a whole: 
def add_donation(d_name, n_donation):
# will add donation to existing list if donor exists, and instantiate new donor entry with empty donations list
# which at this point will then prompt for first donation anyways
    donor_dict.setdefault(d_name, []).append(n_donation) 
    print(email_templates(d_name, n_donation, 1))  


# Updated to use a list comprehension 
def create_report():
    # use list comprehension to store contents of dict into a list of tuples structure which can then be sorted and displayed
    
    donor_history = [(donor_name.title(), sum(amounts), len(amounts), sum(amounts)/len(amounts)) for (donor_name, amounts) in donor_dict.items()]
        
    donor_history = sorted(donor_history, key=sort_key, reverse=True) 
    # reverse=True param sorts by highest to lowest total ie. descending ordered totals
    # sorted and changed in place by 2nd item in the new list comprehension ie. the total donation amt
    
    hdrfmt = "| {:<25s}|{:^18s}|{:^15s}|{:^18s}|".format("Donor Name:", "Total Donated:", "# Donations:", "Donation Avg:")
    divider = "-"*len(hdrfmt) 
    rowfmt = "| {d_name:<25s}|${d_total:^17.2f}|{d_count:^15d}|${d_avg:^17.2f}|".format
    # create formatting using .format
    
    print(divider)
    print(hdrfmt) 
    print(divider)
    for d_entry in donor_history:
        print(rowfmt(d_name=d_entry[0], d_total=d_entry[1], d_count=d_entry[2], d_avg=d_entry[3]))
    print(divider, "\n")


# updated for try--except error check blocks on Open and Write files
def write_email_all():
# This process goes through a try--except check for both opening the file and writing to the file,
# using the newly added write_file error check function written/defined at the start of the program.
    div = "===------------------------------------------------------------------------------===\n"
    print("Preparing to send emails to all current donors in the database...\n")
    for fname, amts in donor_dict.items():
        letter = email_templates(fname, sum(amts), 3)
        print(div)
        print(letter)                                           # writing to file
        print(div)
        filename = "_".join(fname.title().split()) + ".txt"
        write_file(filename, letter)
        # produces .txt file in the current working directory (where this script is presently located) 
    print("Files written to Current Working Directory located at: ", current_dir, "\n")
    

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


def main():

    os.chdir(current_dir)
    # To ensure files get written in current working directory
    
    while True:
        # insert try--except block around response input, in case input cannot be converted to an int: (ValueError)
        try:
            response = int(safe_input(main_prompt))  
        except ValueError:
            print("Not a valid integer value. (between 1 - 4 for valid menu selection)")
            continue  # run the input loop till accepted response            
        
        if response in main_menu_dict:
            main_menu_dict.get(response)()
            # fetches relevant value based on key selection which is a call to the associated feature function
        else:
            print("Please enter a valid menu selection (between 1 - 4).\n")
            continue


main_menu_dict = {1 : send_thank_you,
                  2 : create_report,
                  3 : write_email_all,
                  4 : quit_program
                  }


if __name__ == "__main__":
    
    # block to guard against your code running automatically if this module is imported
    main()