#!/usr/bin/env python3

"""Automate the process of creating 'Thank You' letters and tracking donors and donations through reports.

"""
from operator import itemgetter

donor_info = [('Frank Miller', [320.00, 100.00, 570.50]), ('Tess Baker', [1000.00, 540.00]), 
('Grant Hugh', [5000.00]), ('Sarah Piper', [40.00]), ('Jim Newton', [1350.00, 1500.00, 5.50])]

def prompt():
    global actions
    actions = input("Choose one of the following options: \n1. Send a Thank You \n2. Create a Report \n3. Quit \n>>> ")

#function for selection 1
def handle_selection1():
    full_name = input("Enter the donor's full name.\n>> ")
    
    while full_name == 'list':
        for donor in donor_info:
            print(donor[0])
        full_name = input("\nEnter the donor's full name.\n>> ")
        
    if full_name.lower() == "quit":
        prompt()
        return
    
    donate_amt = input("Enter the donation amount.\n>> $")
    if donate_amt.lower() == 'quit':
        prompt()
        return
    add_donation(full_name, float(donate_amt))
    prompt()

#function for adding a donation
def add_donation(donor_name, donate_amt):
    donor_found = False
    for donor in donor_info:
        if donor[0] == donor_name:
            donor[1].append(donate_amt)
            donor_found = True
    if donor_found is False:
        donor_info.append((donor_name, [donate_amt]))
    print(f"Thank you, {donor_name}, for your generous donation of ${donate_amt:.2f}.")

#function for selection 2
def handle_selection2():
    header = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gifts']
    
    top_row = "{:30} |{:>20} |{:>15} |{:>20}".format(*header[:])
    print(top_row)
    print('-' * len(top_row))
    
    #initiate the report list
    report = []
    
    #fill the report with donor information
    for donor in donor_info:
        report.append([donor[0], sum(donor[1]), len(donor[1]), sum(donor[1])/len(donor[1])])
    
    #sort the report
    sortedReport = sorted(report, key=itemgetter(1), reverse=True)
    
    #print the sorted report
    for donor in sortedReport:
        print("{:30}  ${:>19.2f}  {:>15}  ${:>19.2f}".format(*donor[:]))
    
    prompt()

def main():
    prompt()
    while actions != '3':
        if actions == '1':
            handle_selection1()
            
        elif actions == '2':
            handle_selection2()
            
if __name__ == "__main__":
    main()