#!/usr/bin/env python3
import sys
import os
import tempfile
import time

# donations = [['John Kestrel', [653772.32, 12.17, 4]],
#  ['Jeff Kingbird', [877.33]],
#  ['Paul Jacobin', [663.23, 43.87, 1.32]],
#  ['Mark Tanager', [1663.23, 4300.87, 10432.0]],
#  ['Anna Hummingbird', [4500.0, 800.0, 2350.0]],
#  ['Calvin Fannin', [645.0]]]

donations = {1:{'name':'John Kestrel','amount':[653772.32, 12.17, 4]},
2:{'name':'Jeff Kingbird','amount':[877.33]},
3:{'name':'Paul Jacobin','amount':[663.23, 43.87, 1.32]},
4:{'name':'Mark Tanager','amount':[1663.23, 4300.87, 10432.0]},
5:{'name':'Anna Hummingbird','amount':[4500.0, 800.0, 2350.0]},
6:{'name':'Calvin Fannin', 'amount':[645.0]}}

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

def search_fullname(donor_name):
    #search to see if donor already exits
    for i in donations:
        if donations[i]['name'] == donor_name:
            return True
    return False


def get_name_index(donor_name):
    #find donors name and return the index in the list
    for i in donations:
        if donations[i]['name'] == donor_name:
            return i


def create_email(donor_name, amount):
    #Print thank you message
    email_signature = 'Hydro Flask'
    email_fields = {'email_sign':email_signature,'name':donor_name,'amount':amount}
    return email_template.format(**email_fields)
    #print(f"{donor_name.title()}, thank you for your generous donation of ${amount:.2f}.")


def get_next_key():
    return len(donations) + 1


def add_donation_new_donor(donor_name, amount):
    #add donor and donation to dontaion list
    key_id = get_next_key()
    donations[key_id] = {}
    donations[key_id]['name'] = donor_name
    donations[key_id]['amount'] = []
    donations[key_id]['amount'].append(amount)


def add_donation(name_index, amount):
    #add to the donation list of lists when donor exists
    donations[name_index]['amount'].append(amount)


def print_donors():
    #[x[0] for x in donations]
    # for i,name in enumerate(donations):
    #     print (donations[i][0])
    for i in donations:
        print(donations[i]['name'])


def sort_key(donation_list):
    #return the value to sort on
    return donation_list[1]


def create_summary():
    summary_values =[]
    for donor_id in donations:
        #aggregate dontations and get averages
        donor_name = donations[donor_id]['name']
        total = sum(donations[donor_id]['amount'])
        donate_count = len(donations[donor_id]['amount'])
        donate_avg = total / donate_count
        summary_values.append([donor_name, total, donate_count, donate_avg])
    return summary_values


def send_thankyou():
    name = input("Enter Donors Full name <First> <Last>")
    while name == "list":
        print_donors()
        name = input("Enter Donors Full name <First> <Last>")
    else:
        if search_fullname(name):
            response_amount = float(input ("Enter a dollar amount"))
            #add donation to select user
            add_donation(get_name_index(name),response_amount)
            #compose the email and print to terminal
            print(create_email(name, response_amount))
        else:
            # add user to list
            #add_donor(name)
            response_amount = float(input ("Enter a dollar amount"))
            # add donation to select user
            add_donation_new_donor(name, response_amount)
            #compose email and print to terninal
            print(create_email(name, response_amount))


def write_letters_all_donors():
    #write emails to file in temp directory.
    temp_dir = tempfile.gettempdir()
    file_locations = []
    for donor_id in donations:
        dest = os.path.join(temp_dir, donations[donor_id]['name'].replace(" ", "_") + time.strftime("%Y%m%d-%H%M%S") + ".txt")
        file_locations.append(dest)
        with open(dest, 'w') as outfile:
            outfile.write(create_email(donations[donor_id]['name'], sum(donations[donor_id]['amount'])))
            #print("File has been written to : " + dest)
    return file_locations


def create_report():
    report_values = create_summary()
    print('{:<20}{:>12}{:>10}{:>20}'.format("Donor Name","| Total Given ","| Num Gifts ","| Average Gift "))
    print("-" * 70)
    #print a list of donations
    for name in (sorted(report_values,key=sort_key,reverse=True)):
        print('{:<20}${:>12,.2f}{:^20d}${:>12,.2f}'.format(name[0],name[1],name[2],name[3]))


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
