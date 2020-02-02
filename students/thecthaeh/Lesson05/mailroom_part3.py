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
    actions = input("Choose one of the following options: \n1. Send a Thank You to a single donor \n2. Create a Report \n3. Send letters to all donors \n4. Quit \n>>> ")

def option1():
    """Send a Thank You letter to a single donor."""
    full_name = input("Enter the donor's full name.\n>> ")
    
    while full_name == 'list':
        for donor in donor_info_dict:
            print(donor)
        full_name = input("\nEnter the donor's full name.\n>> ")
        
    if full_name.lower() == "quit":
        prompt()
        return
    
    donate_amt = input("\nEnter the donation amount.\n>> $")
    while donate_amt != 'quit':
        try:
            add_donation(full_name, float(donate_amt))
            break
        except ValueError:
            donate_amt = input("\nInvalid entry, try again. \nUsing only numbers, enter the donation amount. \n>> $")
    
    if donate_amt.lower() == 'quit':
        prompt()
        return

    prompt()

def add_donation(donor_name, donate_amt):
    """Add a donor and/or a donation."""
    if donor_name in donor_info_dict:
        donor_info_dict[donor_name].append(donate_amt)
    else:
        donor_info_dict.setdefault(donor_name, [donate_amt])
        
    print(f"Thank you, {donor_name}, for your generous donation of ${donate_amt:.2f}.")

def option2():
    """Create a report listing donors, their total donation amount, the number of donations, and their average donation."""
    header = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gifts']
    
    top_row = "{:30} |{:>20} |{:>15} |{:>20}".format(*header[:])
    print(top_row)
    print('-' * len(top_row))
    
    report = [[donor, sum(donor_info_dict[donor]), len(donor_info_dict[donor]), sum(donor_info_dict[donor])/len(donor_info_dict[donor])] for donor in donor_info_dict]
    
    #sort the report in descending order of total donation amount
    sorted_report = sorted(report, key=itemgetter(1), reverse=True)
    
    for donor in sorted_report:
        print("{:30}  ${:>19.2f}  {:>15}  ${:>19.2f}".format(*donor[:]))
    
    prompt()

def option3():
    """Send letters to all donors."""
    letter_dict = {donor_name:sum(donor_info_dict[donor_name]) for donor_name in donor_info_dict}
    print(letter_dict) #test
    
    for name in letter_dict:
        with open(f"./{name}.txt", 'w') as f:
            f.write("Dear {},\n\nYou have donated a total of ${:.2f}. \n\nYour generosty will help us fulfill our plans for the coming year. We will send you updates on our upcoming projects so you can see how your donations are being used.\n\nThank you!\nThe Team\n".format(name, letter_dict[name]))
    prompt()

#This dict holds the different functions for each selection option
select_func_dict = {
    1: option1, 
    2: option2,
    3: option3,
    }

def main(): #use a dict to switch between the user's selections
    prompt()
    while actions != '4':
        if actions == '1':
            select_func_dict.get(1)()
            
        elif actions == '2':
            select_func_dict.get(2)()
            
        elif actions == '3':
            select_func_dict.get(3)()
        
        else:
            prompt()
            
if __name__ == "__main__":
    main()