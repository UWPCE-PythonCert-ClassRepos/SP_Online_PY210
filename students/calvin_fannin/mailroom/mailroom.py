#!/usr/bin/env python3
import sys

donations = [['John Kestrel', [653772.32, 12.17, 4]],
 ['Jeff Kingbird', [877.33]],
 ['Paul Jacobin', [663.23, 43.87, 1.32]],
 ['Mark Tanager', [1663.23, 4300.87, 10432.0]],
 ['Anna Hummingbird', [4500.0, 800.0, 2350.0]],
 ['Calvin Fannin', [645.0]]]

prompt = "\n".join (("Welcome to Mailroom","Choose an option:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Quit Mailroom",
          " >>> "))


def search_fullname(donor_name):
    #search to see if donor already exits
    for i,name in enumerate(donations):
        if donor_name == (donations[i][0]):
            return True
    return False


def get_name_index(donor_name):
    #find donors name and return the index in the list
    for i,name in enumerate(donations):
        if donor_name == (donations[i][0]):
            return i


def create_email(donor_name, amount):
    #Print thank you message
    print(f"{donor_name.title()}, thank you for your generous donation of ${amount:.2f}.")


def add_donation_new_donor(donor_name, amount):
    #add donor and donation to dontaion list
    donations.append([donor_name, [amount]])


def add_donation(name_index, amount):
    #add to the donation list of lists when donor exists
    donations[name_index][1].append(amount)


def print_donors():
    #[x[0] for x in donations]
    for i,name in enumerate(donations):
        print (donations[i][0])


def sort_key(donation_list):
    #return the value to sort on
    return donation_list[1]


def create_summary():
    summ_values =[]
    for name in donations:
        #aggregate dontations and get averages
        summ_values.append([name[0],sum(name[1][:]),len(name[1]),sum(name[1][:])/len(name[1])])
    return summ_values


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
            create_email(name, response_amount)
        else:
            # add user to list
            #add_donor(name)
            response_amount = float(input ("Enter a dollar amount"))
            # add donation to select user
            add_donation_new_donor(name, response_amount)
            #compose email and print to terninal
            create_email(name, response_amount)


def create_report():
    report_values = create_summary()
    print('{:<20}{:>12}{:>10}{:>20}'.format("Donor Name","| Total Given ","| Num Gifts ","| Average Gift "))
    print("-" * 70)
    #print a list of donations
    for name in (sorted(report_values,key=sort_key,reverse=True)):
        #print('{:<20}${:>12,.2f}{:^20d}${:>12,.2f}'.format(name[0],sum(name[1][:]),len(name[1]),sum(name[1][:])/len(name[1])))
        print('{:<20}${:>12,.2f}{:^20d}${:>12,.2f}'.format(name[0],name[1],name[2],name[3]))


def quit_program():
    sys.exit()


def main():
    main_menu = {1:send_thankyou, 2:create_report, 3:quit_program}
    while True:
        response = int(input(prompt))
        main_menu.get(response, "Invalid option")()

if __name__ == "__main__":
    main()
