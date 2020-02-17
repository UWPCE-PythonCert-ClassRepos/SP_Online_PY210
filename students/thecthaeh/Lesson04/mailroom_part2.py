#!/usr/bin/env python3

"""Automate the process of creating 'Thank You' letters and tracking donors and donations through reports.

"""
import sys
from operator import itemgetter

#convert to a dict
donor_info_dict = {}
donor_info_dict['Frank Miller'] = [320.00, 100.00, 570.50]
donor_info_dict['Tess Baker'] = [1000.00, 540.00]
donor_info_dict['Grant Hugh'] = [5000.00]
donor_info_dict['Sarah Piper'] = [40.00]
donor_info_dict['Jim Newton'] = [1350.00, 1500.00, 5.50]

#function for selection 1
def single_thank_you():
    full_name = input("Enter the donor's full name.\n>> ")
    
    while full_name == 'list':
        for donor in donor_info_dict:
            print(donor)
        full_name = input("\nEnter the donor's full name.\n>> ")
        
    if full_name.lower() == "quit":
        return
    
    donate_amt = input("\nEnter the donation amount.\n>> $")
    if donate_amt.lower() == 'quit':
        return
    add_donation(full_name, float(donate_amt))

#function for adding a donation
def add_donation(donor_name, donate_amt):
    if donor_name in donor_info_dict:
        donor_info_dict[donor_name].append(donate_amt)
    else:
        donor_info_dict.setdefault(donor_name, [donate_amt])
        
    print(f"Thank you, {donor_name}, for your generous donation of ${donate_amt:.2f}.")

#function for selection 2
def create_report():
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
    sorted_report = sorted(report, key=itemgetter(1), reverse=True)
    
    #print the sorted report
    for donor in sorted_report:
        print("{:30}  ${:>19.2f}  {:>15}  ${:>19.2f}".format(*donor[:]))

#function for selection 3
def thank_all():
    for name, donation in donor_info_dict.items():
        with open(f"./{name}.txt", 'w') as f:
            f.write("Dear {},\n\nYou have donated a total of ${:.2f}. \n\nYour generosty will help us fulfill our plans for the coming year. We will send you updates on our upcoming projects so you can see how your donations are being used.\n\nThank you!\nThe Team\n".format(name, sum(donation)))

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