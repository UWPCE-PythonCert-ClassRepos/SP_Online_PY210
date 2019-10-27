#!/usr/bin/env python3
#lesson5
#https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/mailroom-part3.html

import sys
import os.path
from statistics import mean\

##### Global Variables

#Dictionaries
donor_db = {
            "William Gates, III": [653772.32, 12.17],
            "Jeff Bezos": [877.33],
            "Paul Allen": [663.23, 43.87, 1.32],
            "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
            }

report_dict = {"Header": "{0: <28}|{1: ^13}|{2: ^11}|{3: ^15}",
               "Filler": "-" * 68,
               "Rows":"{0: <28} ${1: >11.2f}   {2: >9}  ${3: >12.2f}",
               }

#prompts (alphabetical)
donation_prompt = "Please enter the amount of the donation. \n"

thank_you_prompt = "Please enter the full name of the donor or type 'list' for list of names. \n"

write_location_prompt = "Please enter the directory name to save to, or type 'no' for temp directory. \n"

main_prompt = "\n".join(("Please choose from the following options:",
          "1 - Create a report",
          "2 - Send thank you letter to one donor",
          "3 - Send thank you letter to all donors",
          "4 - Exit \n"
          ))

#Email
thank_you_email = "\n".join(("Dear {donor},",
            "",
            "Thanks you for your generous donation of {donation:.2f}.  Your total donations of {total:.2f} are greatly appriciated.",
            "",
            "Sincerly,",
            "The Weyland-Yutani Corporation"
          ))

#####Functions(alphabetical)
def create_a_report():
    #Print the report
    print("\n")
    print(report_dict["Header"].format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print(report_dict["Filler"])
    for key, value in sorted (donor_db.items(), key = sort_key, reverse=True):
        print(report_dict["Rows"].format(key, round(sum(value),2), round(len(value),2), round(mean(value),2)))

def exit_program():
    #It's all there, black and white, clear as crystal! 
    #You stole fizzy lifting drinks! 
    #You bumped into the ceiling which now has to be washed and sterilized, so you get nothing! 
    #You lose!
    print("Good day!")
    sys.exit()
    
def send_thank_you_one():
    #import db
    #global donor_db
    #keep doing this until further notice
    while True:
        #ask for name or to print list of names
        donor_name = input(thank_you_prompt)
        #print out names
        if donor_name == 'list':
            for name in donor_db.items():
                print(name)
            #skip loop to reprompt
            continue
        
        #ask for the donation amount
        donor_amount = input(donation_prompt)
        #set as a numeric value
        donor_amount = float(donor_amount)
        
        if donor_name in donor_db.keys():
            donor_db[donor_name].append(donor_amount)
        else:
            donor_db[donor_name] = [donor_amount]
                
        #print out the thank you email
        thanks_dict = {"donor": donor_name, "donation": donor_amount, "total": sum(donor_db[donor_name])}
        print(thank_you_email.format(**thanks_dict))
        break

def send_thank_you_all():
    #Send out last donation and total donations
    while True:
        try:
            response = str(input(write_location_prompt))
        except ValueError:
            print('please enter a valid string')
            continue
        else:
            if response == 'no' or os.path.isfile(response):
                break
        
    for key, value in donor_db.items():
        if response == 'no':
            file_name = key + '.txt'
        else:
            file_name = response + key + '.txt'
        
        with open(file_name, 'w') as thank_you:
            thanks_dict = {"donor": key, "donation": value[-1], "total": sum(value)}
            thank_you.write(thank_you_email.format(**thanks_dict))
    
def sort_key(db):
    #sum up donations for sortation
    return sum(db[1])

##Switchs
main_menu = {
        1 : create_a_report,
        2 : send_thank_you_one,
        3 : send_thank_you_all,
        4 : exit_program
        }

##### Main 
def main():
    #keep doing this until further notice
    while True:
        #print out main menu for user choice
        try:
            response = int(input(main_prompt))
        except ValueError:
            print("please input valid number")
            pass
        main_menu.get(response)()

if __name__ == '__main__':
    main()
