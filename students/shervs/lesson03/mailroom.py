#!/usr/bin/env python

import sys  

donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ("Donald Trump", [0])
            ]

prompt = "\n".join(("Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Quit",
          ">>> "))

def sort_key(donation_list):   #sortkey to sort for total donation amount
    return sum(donation_list[1])

def create_report(a_donor_db): # prints a list of donors, sorted by total #historical donation amount. 
    print("\n".join(('Donor Name                | Total Given | Num Gifts | Average Gift',
    '------------------------------------------------------------------')))
    for donor in sorted(a_donor_db, key = sort_key , reverse = True):
        print('{:26s}'.format(donor[0]),'$','{:10.2f}'.format(sum(donor[1])),
        '{:11d}'.format(len(donor[1])), ' $',
        '{:11.2f}'.format(sum(donor[1])/len(donor[1])))

def donor_exist(a_name, a_donor_db): # returns true if a donar's name exists in #the database , Flase if not
    for donor in a_donor_db:
        if donor[0] == a_name:
            return True
    return False

def add_donor(new_donor , a_donor_db): #adds new donor's name to the database
    a_donor_db.append((new_donor , []))
    
def add_donation(a_donor, a_donor_db): #takes donation amount from the user for #a given donor, returns donation amount
    new_donation = input("input donation amount?")
    for donor in a_donor_db:
        if donor[0] == a_donor:
            donor[1].append(int(new_donation))
    return new_donation

def print_donor_list(a_donor_db): # prints the name of all the donors
    for donor in a_donor_db:
        print(donor[0], end="\n")

def send_thank_you(a_donor_db): 

    prompt = "\n".join(("Send a thank you note!", 
          "Please type donor's full name or type 'list' to view list of donors",
          ">>> "))

    while True:
        response = input(prompt).title()  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "List":
            print_donor_list(a_donor_db)

        elif not donor_exist(response, a_donor_db):
            add_donor(response , a_donor_db)
            
            print(f"Thank you {response} for your generous donation of ${add_donation(response, a_donor_db)}")
            break

        else:
            print(f"Thank you {response} for your generous donation of ${add_donation(response, a_donor_db)}")
            break
           
def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script

def main():
    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "1":
            send_thank_you(donor_db)
        elif response == "2":
            create_report(donor_db)
        elif response == "3":
            exit_program()
        else:
            print("Not a valid option!")

if __name__ == "__main__":
    main()