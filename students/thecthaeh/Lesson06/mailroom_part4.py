#!/usr/bin/env python3

"""Automate the process of creating 'Thank You' letters and tracking donors and donations through reports.

"""
import sys
from operator import itemgetter

donors = {}
donors['Frank Miller'] = [320.00, 100.00, 570.50]
donors['Tess Baker'] = [1000.00, 540.00]
donors['Grant Hugh'] = [5000.00]
donors['Sarah Piper'] = [40.00]
donors['Jim Newton'] = [1350.00, 1500.00, 5.50]

def add_donation(donor_name, donation):
    """Add a donation amount to a new or existing donor."""
    if donor_name in donors:
        donors[donor_name].append(donation)
    else:
        add_donor(donor_name)
        add_donation(donor_name, donation)

def add_donor(donor_name):
    if donor_name not in donors:
        donors.setdefault(donor_name, [])

def list_donors():
    list = []
    for donor in donors: list.append(donor)
    return "\n".join(list)

def thank_you(donor_name):
    if donor_name in donors:
        letter = f"Thank you, {donor_name}, for your generous donation of ${donors[donor_name][-1]:,.2f}."
        return letter
    else:
        return "This donor does not exist."

def single_thank_you():
    """Send a Thank You letter to a single donor.
    
    Update the donors dict with a new donor and/or donation amount and
    display a thank you letter to that donor for their latest donation.
    """
    input_donor = input("Enter the donor's full name.\n>> ")
    
    while input_donor.lower() == 'list':
        print(list_donors())
        input_donor = input("\nEnter the donor's full name.\n>> ")
        
    if input_donor.lower() == "quit":
        return
    
    input_donation = input("\nEnter the donation amount.\n>> $")
    while input_donation != 'quit':
        try:
            add_donation(input_donor, float(input_donation))
            break
        except ValueError:
            input_donation = input("\nInvalid entry, try again. \nUsing only numbers, enter the donation amount. \n>> $")
    
    if input_donation.lower() == 'quit':
        return

    print(thank_you(input_donor))

def report(a_dict):
    """Take in a dict and create a report."""
    header = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gifts']
    
    top_row = "{:30} |{:>20} |{:>15} |{:>20}".format(*header[:])
    
    report_info = [[x, sum(a_dict[x]), len(a_dict[x]), sum(a_dict[x])/len(a_dict[x])] for x in a_dict]
    
    #sort the report by total donation amount (descending order)
    sorted_report = sorted(report_info, key=itemgetter(1), reverse=True)
    
    report_content = [top_row, sorted_report]
    
    return report_content

def create_report():
    """Create a report of all the donors.
    
    Include each donor, their total donation amount, the number of donations, and their average donation.
    Sort the report by largest total donation.
    """
    full_report = report(donors)
    
    print(full_report[0])
    print('-' * len(full_report[0]))
    for donor in full_report[1]:
        print("{:30}  ${:>19,.2f}  {:>15}  ${:>19,.2f}".format(*donor[:]))

def text_files(a_dict):
    """Create a text file for each donor."""
    text = "Dear {name},\n\nYour total donations to date equal ${total:,.2f}.\n\nWe are grateful for your continued patronage and we can't wait to show you what your generosity will help us achieve.\n\nThank you!\nThe Team\n"
    
    for key in a_dict:
        letter_dict = {'name': key, 'total': sum(a_dict[key])}
        with open(f"./{key}.txt", 'w') as f:
            f.write(text.format(**letter_dict))
    
def thank_all():
    """Send letters to all donors.""" 
    text_files(donors)

def quit_program():
    sys.exit()

def main(): #use a dict to switch between the user's selections
    menu = {
            '1': single_thank_you, 
            '2': create_report,
            '3': thank_all,
            '4': quit_program,
            'quit': quit_program
        }
    while True:
        prompt = input("Choose one of the following options: \n1. Send a Thank You to a single donor \n2. Create a Report \n3. Send letters to all donors \n4. Quit \n>>> ")
        menu[prompt]()
            
if __name__ == "__main__":
    main()