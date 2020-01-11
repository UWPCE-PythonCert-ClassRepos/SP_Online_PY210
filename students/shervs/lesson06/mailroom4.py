#!/usr/bin/env python

import sys
import string
import os

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

def get_report(a_donor_dict): #take a donor dictionary and returns sorted list #based on total donation     
    report_rows = list()
    for donor in a_donor_dict:
        report_rows.append((donor,sum(a_donor_dict[donor]),len(a_donor_dict[donor])
        ,sum(a_donor_dict[donor])/len(a_donor_dict[donor])))
    return sorted(report_rows, key=lambda k:k[1], reverse = True)


def print_report(report_list):
    print("\n".join(('Donor Name                | Total Given | Num Gifts | Average Gift',
    '------------------------------------------------------------------')))
    for row in report_list:
        print(f"{row[0]:26s} $ {row[1]:10.2f} {row[2]:11d}  $ {row[3]:11.2f}")


def create_report(a_donor_dict): # prints a list of donors, sorted by total #historical donation amount.
   print_report(get_report(a_donor_dict))


def generate_thank_you_text(name,donation):
    return f"Thank you {name} for your generous donation of ${donation}"
   

def add_donor(new_donor , a_donor_dict): #adds new donor's name to the database
    a_donor_dict.update({new_donor: []})
    return a_donor_dict


def input_donation():
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
    return new_donation
   
   
def add_donation(a_donor, a_donation, a_donor_dict): #takes donation amount from the user for #a given donor, returns donation amount
    {a_donor_dict[donor].append(a_donation) for donor in a_donor_dict if donor == a_donor}
    return a_donor_dict


def generate_donor_list(a_donor_dict): # generates a list of donors from the #donor database
    for donor in a_donor_dict:
        print(donor, end="\n")


def send_thank_you(a_donor_dict): 
    prompt = "\n".join(("Send a thank you note!",
          "Please type donor's full name or type 'list' to view list of donors",
          ">>> "))

    while True:
        response = input(prompt).title()  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "List":
            generate_donor_list(a_donor_dict)
       
        elif response in string.punctuation:
            print("\nDonor's name must include some letters or numbers.\n")

        elif response in a_donor_dict:
            print(generate_thank_you_text(response , add_donation(response,input_donation() , a_donor_dict)))
            break

        else:
            add_donor(response , a_donor_dict)
            print(generate_thank_you_text(response , add_donation(response,input_donation() , a_donor_dict)))
            break


def letter_text(a_donor, some_donations):

    #remove punctuation from donor's name and join
    donor_name = a_donor.translate(str.maketrans('', '', string.punctuation)).split()
    message_dict = { 'first':donor_name[0] , 'last':' '.join(donor_name[1:]) ,'total donation':sum(some_donations) }
    message = '''Dear {first} {last},\n
     Thank you for your donation of ${total donation:.0f} throughout these years.\n
     Cheers,\n
          -The team'''.format(**message_dict)
    file_name = '_'.join(donor_name)+'.txt'
    return (file_name,message)


def write_to_file(a_file_name, a_message): #writes thanks you letter to a file #for each donor
    with open(a_file_name, 'w') as f:
            f.write(a_message)


def Send_letters_to_all(a_donor_dict):
    for donor in a_donor_dict:
        #write letter to the file
        write_to_file(letter_text(donor, a_donor_dict[donor])[0], letter_text(donor, a_donor_dict[donor])[1])
    print("\nThank-you letters were written into the files!\n")      


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