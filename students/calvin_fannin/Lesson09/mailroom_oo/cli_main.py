#!/usr/bin/env python3
import sys
import os
import tempfile
import time
import donor_models as dm
import random

prompt = "\n".join (("Welcome to Mailroom","Choose an option:",
          "1 - Send a Thank You Letter to Single Donor",
          "2 - Create a Report",
          "3 - Send Letters to All Donors",
          "4 - Quit Mailroom",
          " >>> "))


email_template = "\n".join (("Hi {name}",
         "",
         "Thank you for your generous donations of {amount}.",
         "",
         "Respectfully,",
         "{email_sign}"))


def sort_key(donation_list):
    #return the value to sort on
    return donation_list[1]


#Sample data
names = [("Calvin","Fleming"), ("Mary", "Andrews"), ("Bucket", "Head")]
donorslist = [dm.Donor(*name,random.random() * 1000) for name in names]
dc = dm.DonorCollection(donorslist)
#    return dc


def print_donors():
    for donor in dc.list_donors():
        print(donor.fullname)


def send_thankyou():
    name = input("Enter Donors Full name <First> <Last>")
    while name.lower() == "list":
        print_donors()
        name = input("Enter Donors Full name <First> <Last>")
    else:
        if dc.search_fullname(name):
            while True:
                try:
                    response_amount = float(input ("Enter a dollar amount"))
                    #add donation to select user
                    dc.add_donation(name,response_amount)
                    #compose the email and print to terminal
                    print(create_email(name, response_amount))
                except ValueError:
                    print("Not a valid donation amount")
        else:
            createuser = input("The Person was not found create Donor? Y(es) or N(o)")
            if createuser.lower() == "y":
                while True:
                    try:
                        # add user to list
                        #add_donor(name)
                        response_amount = float(input ("Enter a dollar amount"))
                        # add donation to select user
                        nameparts = name.split()
                        newdonor = dm.Donor(nameparts[0],nameparts[1], response_amount)
                        dc.add_donor(newdonor)
                        #compose email and print to terninal
                        print(create_email(name, response_amount))
                    except ValueError:
                        print("Not a valid donation amount")


def create_report():
    report_values = dc.create_summary()
    print('{:<20}{:>12}{:>10}{:>20}'.format("Donor Name","| Total Given ","| Num Gifts ","| Average Gift "))
    print("-" * 70)
    #print a list of donations
    for name in (sorted(report_values,key=sort_key,reverse=True)):
        print('{:<20}${:>12,.2f}{:^20d}${:>12,.2f}'.format(name[0],name[1],name[2],name[3]))


def create_email(donor_name, amount):
    #Print thank you message
    email_signature = 'Hydro Flask'
    email_fields = {'email_sign':email_signature,'name':donor_name,'amount':amount}
    return email_template.format(**email_fields)
    #print(f"{donor_name.title()}, thank you for your generous donation of ${amount:.2f}.")


def write_letters_all_donors():
    #write emails to file in temp directory.
    temp_dir = tempfile.gettempdir()
    file_locations = []
    for donor in dc.donors:
        dest = os.path.join(temp_dir, donor.fullname.replace(" ", "_") + time.strftime("%Y%m%d-%H%M%S") + ".txt")
        file_locations.append(dest)
        with open(dest, 'w') as outfile:
            outfile.write(create_email(donor.fullname, donor.totaldonation))
            #print("File has been written to : " + dest)
    return file_locations


def quit_program():
    sys.exit()


def invalid_option():
    print ("Invalid Option Please Try again!")


def main():
    #dictionary to be used for switching of main menu
    main_menu = {1:send_thankyou, 2:create_report, 3:write_letters_all_donors, 4:quit_program}
    while True:
        try:
            response = int(input(prompt))
        except ValueError:
            print('Please enter a  int number')
        else:
            main_menu.get(response,invalid_option)()


if __name__ == "__main__":
    main()
