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

#function for selection 1
def option1():
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

#print a thank you letter to each donor
#should use a dict and .format(**dict) method to create letter

#function for selection 2
def option2():
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

#function for selection 3
def option3():
    letter_dict = {}
    for donor_name in donor_info_dict:
        letter_dict.setdefault(donor_name, sum(donor_info_dict[donor_name]))
    print(letter_dict) #test
    
    for name in letter_dict:
        with open(f"./{name}.txt", 'w') as f:
            f.write("Dear {},\n\nYou have donated a total of ${:.2f}. \n\nYour generosty will help us fulfill our plans for the coming year. We will send you updates on our upcoming projects so you can see how your donations are being used.\n\nThank you!\nThe Team\n".format(name, letter_dict[name]))
            #f.write(("{}, your donation values were: {}" + ((", {}") * (len(donor_info_dict[name])-1)) + "\n").format(name, *donor_info_dict[name][:]))
    
    
    prompt()

#This dict holds the different functions for each selection option
select_func_dict = {
    1: option1, 
    2: option2,
    3: option3,
    #4: option4,
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
            
if __name__ == "__main__":
    main()