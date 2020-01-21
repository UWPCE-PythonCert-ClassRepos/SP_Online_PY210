#!/usr/bin/env python3

"""Automate the process of creating 'Thank You' letters and tracking donors and donations through reports.

"""
from operator import itemgetter

#convert to a dict
donor_info_dict = {}
donor_info_dict['Frank Miller'] = [320.00, 100.00, 570.50]
donor_info_dict['Tess Baker'] = [1000.00, 540.00]
donor_info_dict['Grant Hugh'] = [5000.00]
donor_info_dict['Sarah Piper'] = [40.00]
donor_info_dict['Jim Newton'] = [1350.00, 1500.00, 5.50]

def prompt():
    global actions
    actions = input("Choose one of the following options: \n1. Send a Thank You \n2. Create a Report \n3. Quit \n>>> ")

#function for selection 1
def handle_selection1():
    full_name = input("Enter the donor's full name.\n>> ")
    
    while full_name == 'list':
        for donor in donor_info_dict:
            print(donor)
        full_name = input("\nEnter the donor's full name.\n>> ")
        
    if full_name.lower() == "quit":
        prompt()
        return
    
    donate_amt = input("\nEnter the donation amount.\n>> $")
    if donate_amt.lower() == 'quit':
        prompt()
        return
    add_donation(full_name, float(donate_amt))
    prompt()

#function for adding a donation
def add_donation(donor_name, donate_amt):
    if donor_name in donor_info_dict:
        donor_info_dict[donor_name].append(donate_amt)
    else:
        donor_info_dict.setdefault(donor_name, [donate_amt])
        
    print(f"Thank you, {donor_name}, for your generous donation of ${donate_amt:.2f}.")

#print a thank you letter to the donor
#should use a dict and .format(**dict) method to create letter

#function for selection 2
def handle_selection2():
    header = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gifts']
    
    top_row = "{:30} |{:>20} |{:>15} |{:>20}".format(*header[:])
    print(top_row)
    print('-' * len(top_row))
    
    #initiate the report list
    report = []
    
    #fill the report with donor information
    for donor in donor_info_dict:
        report.append([donor, sum(donor_info_dict[donor]), len(donor_info_dict[donor]), sum(donor_info_dict[donor])/len(donor_info_dict[donor])])
    
    #sort the report
    sorted_report = sorted(report, key = itemgetter(1), reverse = True)
    
    #print the sorted report
    for donor in sorted_report:
        print("{:30}  ${:>19.2f}  {:>15}  ${:>19.2f}".format(*donor[:]))
    
    prompt()

#This dict holds the different functions for each selection option
select_func_dict = {
    1: handle_selection1, 
    2: handle_selection2,
    }

def main(): #use a dict to switch between the user's selections
    prompt()
    while actions != '3':
        if actions == '1':
            select_func_dict.get(1)()
            
        elif actions == '2':
            select_func_dict.get(2)()
            
if __name__ == "__main__":
    main()