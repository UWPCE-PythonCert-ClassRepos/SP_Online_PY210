#!/usr/bin/env python3

import sys

##### Global Variables

#Initial donor list
#list of donors and a history of amaount.  pop w/ first 5 w/ 1-3 donations each
donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ]

#prompts (alphabetical)
donation_prompt = "Please enter the amount of the donation. \n"

main_prompt = "\n".join(("Please choose from the following options:",
          "1 - Create a report",
          "2 - Send a thank you",
          "3 - Exit \n"
          ))
return_prompt = "Type 'return' to return to main menu. \n"

thank_you_prompt = "Please enter the full name of the donor or type 'list' for list of names. \n"

#email
thank_you_email = "\n".join(("Dear {}",
            "",
            "Thanks you for your generous donation of {}.  Your total donations of {} are greatly appriciated.",
            "",
            "Sincerly,",
            "The Weyland-Yutani Corporation"
          ))

#####Functions (alphabetical)
def create_a_report():
    #import db
    global donor_db
    #keep doing all this until further notice
    while True:
        #the title row of the report
        header_string = "{0: <28}|{1: ^13}|{2: ^11}|{3: ^15}"
        #boarder thing
        spacing_string = "---------------------------------------------------------------------"
        #format string for all the donors
        donator_string = "{0: <28} ${1: >11.2f}   {2: >9}  ${3: >12.2f}"
        
        #Print all the things!
        print(header_string.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
        print(spacing_string)
        for donor in sorted(donor_db, key = sort_key, reverse=True): #sorts based on function suming up donations
            print(donator_string.format(donor[0], round(sum(donor[1]),2), round(len(donor[1]),2), round(mean(donor[1]),2)))
        response = input(return_prompt)
        #return to main menu
        if response == "return":
             break

def exit_program():
    #It's all there, black and white, clear as crystal! 
    #You stole fizzy lifting drinks! 
    #You bumped into the ceiling which now has to be washed and sterilized, so you get nothing! 
    #You lose!
    print("Good day!")
    sys.exit()
    
def send_thank_you():
    #import db
    global donor_db
    #keep doing this until further notice
    while True:
        #ask for name or to print list of names
        response = input(thank_you_prompt)
        #print out names
        if response == 'list':
            for donor in donor_db:
                print(donor[0])
            continue
        #User has name chosen, need to check it they exist in the db
        else:  
            #loop through names
            for donor in donor_db:
                #if found then break the loop and use the previous donations
                if response == donor[0]:
                    entry = donor
                    break
                #if not found create new entry with no donations
                entry = (response, [])
        #ask for the donation amount
        response = input(donation_prompt)
        #set as a numeric value
        response = float(response)
        #append donation into the donation list
        entry[1].append(response)
        #append if the list just has one entry (is new)
        if len(entry[1]) == 1:
            donor_db.append(entry)
        #print out the thank you email
        print(thank_you_email.format(entry[0], response, sum(entry[1])))
        break

def sort_key(db):
    #suming up donations for sortation
    return sum(db[1])
    
##### Main 
def main():
    #keep doing this until further notice
    while True:
        #print out main menu for user choice
        response = input(main_prompt)
        #print out report and return to main prompt
        if response == "1":
            create_a_report()
            continue
        #inserts new donators and print thank you letter
        elif response == "2":
            send_thank_you()
            continue
        #exit
        elif response == "3":
            exit_program()


if __name__ == '__main__':
    main()





