#!/usr/bin/env python3
'''
Use dicts where appropriate.
Part 1 of this assignment used these basic data types: numbers, strings, 
ists and tuples.

However, using dictionaries, covered in Lesson 4, will let you re-write 
your program a bit more simply and efficiently.

Update your mailroom program to:

Use dicts where appropriate.
See if you can use a dict to switch between the user’s selections.
See if you can use a dict to switch between the users selections. 
see Using a Dictionary to switch for what this means.
Convert your main donor data structure to be a dict.
Try to use a dict and the .format() method to produce the letter 
as one big template, rather than building up a big string that 
produces the letter in parts.
'''

import sys

donor_dict = {"William Gates, III": [653772.32, 12.17],
        "Jeff Bezos":  [877.33],
        "Paul Allen": [663.23, 43.87, 1.32],
        "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
        "Alexandra Butler": [777.77, 44.44]}

prompt = "\n".join(("Welcome to the mail room!",
          "Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Send letters to all donors",
          "4 - Quit",
          ">>> "))

prompt_name = "\n".join(("Type the donors full name or,",
              "type 'list' to display a list of the donors names.",
              ">>> "))

prompt_amount = "\n".join(("Whats the donation amount?",
                ">>> "))

exit_report = "\n".join(("Press 1 to exit to the initial prompt.",
                         "\n"))

report_header = "\n".join(("Donor Name           | Total Given | Num Gifts | Average Gift",
                            "{:-^61}")).format('')

def dis_info():
    for item in donor_dict:
        spaces = ((20 - len(item[0]))*" ")
        
        sum_donations = sum(item[1:])
        sum_donations = round(sum_donations,2)
        num_gifts = len(item[1:])
        avg_gift = (str(round(sum_donations/num_gifts,2)))
        spaces_two = ((15 - len(str(sum_donations)))*' ')
        spaces_three = (42*" ")
        
        print(item[0], spaces, ('$'), sum_donations, spaces_two, num_gifts, spaces_three, ('$'), avg_gift)

def get_index(donor_name):
    # Return the index number based on user input
    for item in (donor_dict):
        if item[0] == donor_name:
            index = donor_dict.index(item)
            
            return index
        
    return None

def add_donor(donor_name):
    # Add donor name to the data structure.
    for item in donor_dict:
        if item[0] not in donor_dict:
            donor_dict[donor_name] = []
            print (donor_dict)
            break

def view_list():
    # Display the donor list.
    print("\n".join(donor_dict))
    
def display_dict():
    for i in donor_dict.keys():
        print(i)
            
def send_thank_you():
    # Request the user to input donor name, and donation information.
    response = str(input(prompt_name))
    while response.lower() == 'list':
        display_dict()
        response = str(input(prompt_name))
       
    else:
        response_amount = float(input(prompt_amount))
        if response in donor_dict.keys():
            donor_dict[response].append(response_amount)
            
        else:
            donor_dict[response] = [response_amount]   
            
    print(f"Hi {response},\n\nThank you for the generous donation of {response_amount}.\n\nSincerely,\nClifford Butler")
    
def create_report():
    # Generate and display a report of the donors in donor_dict
    while True:
        print(report_header)
        dis_info()
        
        response_quit = input(exit_report)
        # Return back to the initial prompt
        if response_quit == "1":
            print("fake exit")
            break
        else:
            print("Not a valid option!")
            break
        
def letter_to_all():
    for donor_name in donor_dict:
        with open(f"{donor_name}.txt","w+") as donor_letter:
            donor_letter.write(f"Hi {donor_name},\n\nThank you for the generous donation of ${sum(donor_dict[donor_name]):.2f}.\n\nSincerely,\nClifford Butler")
    print("\nThank you letters sent!\n")
            
def exit_program():
    # exit the interactive script
    print("Bye!")
    sys.exit()  

def main():
    # continuously collect user selection
    while True:
        response = input(prompt)  
        # redirect to feature functions based on the user selection
        if response == "1":
            send_thank_you()
        elif response == "2":
            create_report()
        elif response == "3":
            letter_to_all()
        elif response == "4":
            exit_program()
        else:
            print("Not a valid option!")

if __name__ == "__main__" :
    # run main function
    main()
   