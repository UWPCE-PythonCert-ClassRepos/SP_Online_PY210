#!/usr/bin/env python

import sys
import string

donor_dict = {"William Gates, III": [1.50, 653772.32, 12.17],
             "Jeff Bezos": [877.33],
             "Paul Allen": [663.23, 43.87, 1.32],
             "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
             }

prompt = "\n".join(("Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Send letters to everyone",
          "4 - Quit",
          ">>> "))

def create_report(a_donor_dict): # prints a list of donors, sorted by total #historical donation amount.
    print("\n".join(('Donor Name                | Total Given | Num Gifts | Average Gift',
    '------------------------------------------------------------------')))
    for donor in sorted(a_donor_dict, key=lambda k: sum(a_donor_dict[k]), reverse =True):
        print('{:26s}'.format(donor),'$',
        '{:10.2f}'.format(sum(a_donor_dict[donor])),
        '{:11d}'.format(len(a_donor_dict[donor])), ' $',
        '{:11.2f}'.format(sum(a_donor_dict[donor])/len(a_donor_dict[donor])))


def add_donor(new_donor , a_donor_dict): #adds new donor's name to the database
    a_donor_dict.update({new_donor: []})

   
def add_donation(a_donor, a_donor_dict): #takes donation amount from the user for #a given donor, returns donation amount
    while True:  
        try:
            new_donation = float(input("Input donation amount>"))
        except ValueError:
            print('Input must be a number, try again.')
        else:
            if new_donation >= 0.01:
                break
            else:
                print('Donations less than 1 cent are not accepted')
    {donor_dict[donor].append(new_donation) for donor in a_donor_dict if donor == a_donor}
    return new_donation


def send_thank_you(a_donor_dict):
    prompt = "\n".join(("Send a thank you note!",
          "Please type donor's full name or type 'list' to view list of donors",
          ">>> "))

    while True:
        response = input(prompt).title()  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "List":
            for donor in a_donor_dict:
                print(donor, end="\n") 
        
        elif response in string.punctuation:
            print("\nDonor's name must include some letters or numbers.\n")


        elif not response in a_donor_dict:
            add_donor(response , a_donor_dict)
           
            print(f"Thank you {response} for your generous donation of ${add_donation(response, a_donor_dict)}")
            break

        else:
            print(f"Thank you {response} for your generous donation of ${add_donation(response, a_donor_dict)}")
            break


def Send_letters_to_all(a_donor_dict):
    for donor in a_donor_dict:
        #remove punctuation from donor's name and join
        donor_name = donor.translate(str.maketrans('', '', string.punctuation)).split()
        message_dict = { 'first':donor_name[0] , 'last':' '.join(donor_name[1:]) ,'total donation':sum(a_donor_dict[donor]) }

        #write letter to the file
        with open('_'.join(donor_name)+'.txt', 'w') as f:
            f.write('''Dear {first} {last},\n
     Thank you for your donation of ${total donation:.0f} throughout these years.\n
     Cheers,\n
            -The team'''.format(**message_dict))
    print("\nThank you letters were written into the files!\n")      


def exit_program(a_donor_dict):
    print("Bye!")
    sys.exit()  # exit the interactive script


def not_valid(a_donor_dict):
    print('\nNot a valid option!\n')


def main():
    switch_func_dict = {
                       '1': send_thank_you,
                       '2': create_report,
                       '3': Send_letters_to_all,
                       '4': exit_program
                       }
    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        switch_func_dict.get(response,not_valid)(donor_dict)


if __name__ == "__main__":
    main()