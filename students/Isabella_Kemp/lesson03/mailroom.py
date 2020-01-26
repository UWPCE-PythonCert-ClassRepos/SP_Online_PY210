# Isabella Kemp
# Assignment 1: Mailroom part 1
# Jan/25/2020

import sys

# list of donors and the amounts they have donated
donors = [("John", [150080.00, 41.28]),
          ("Irene", [1600.00, 24.47]),
          ("Rob", [19000.00, 200.47]),
          ("Kathy", [819.00, 34.5]),
          ("Laureen", [830.00, 47.00, 982.13]),
          ("Miles", [24.50, 87.00, 193.00])]


main_prompt = ("Welcome to the Mailroom! Please choose an option from the menu: " 
                    "\n1. Send a Thank you " 
                    "\n2. Create a Report " 
                    "\n3. Quit" 
                    "\n\n ----> ")


#        print(record[0]) #name
#        print(record[1]) #donations

# common function to get input from user, call with a prompt string
# returns response object that may need to be recast
def get_user_input(prompt_string):
    response = input(prompt_string)
    return response


# User can enter 'list' to get list of existing donors
# User can enter 'listall' to get list of donors and their donations
# User can enter existing donor name, new donation, donation is added to list
# User can enter a new donor, new donation, user and donation is added to list
# We finish with a thank you
def thank_you():
    while True:
        name = get_user_input("Enter a donor name to send a thank you letter, "
                              "'list' or 'listall' for list of donors, '3' will exit: ")
        if name == "list":
            for record in donors:
                print(record[0])  # name
        elif name == "listall":
            for record in donors:
                print(record)  # entire record, name with donations
        elif name == '3':  # allows them to quit and go back to menu
            print("Finished processing thanks to donors...\n\n")
            return
        else:
            # User entered a name, so process that
            record = get_donor(name)
            #print(record) # for debug comment out
            if (record != None):
                # donor is in our list,
                # get donation amount, add donation to list, send thank you
                print("user is in our list")  # for debug
                donation = get_donation()
                #print(donation)  # for debug
                record[1].append(donation)
                #print(record)  # for debug
                email(name, donation)

            else:
                # new donor is not in our list
                # add the donor to our list
                # get donation amount, add donation to list, send thank you
                print("!!! NEW DONOR !!!")
                donation = get_donation()
                #print(donation)  # for debug
                new_record = (name, [donation])
                #print(new_record)  # for debug
                donors.append(new_record)
                email(name, donation)
#end thank_you


# checks to see if provided name is in our donor list
# returns donor record if found, else None
def get_donor(donor_name):
    for record in donors:
        if (record[0] == donor_name):
            return record  # record[0] is name, record[1] is tuple with variable length of donations
    return None

# get donation amount
def get_donation():
    money = get_user_input("Please enter a donation amount: $ ")
    amount = float(money)
    #donors.append(amount)
    return amount


# send thank you to donor
def email(name, amount):
    print("Thank you {}, for your generous donation of ${:.2f} !".format(name,amount))
    return


# creates a report of donor name, total donated, number of donations, and average
# donation amount in each row

def report():
    print("\n{:<19}| {:<13} | {:<13} | {:>13}".format('Donor Name', 'Total Donated',
                                                'Number of Donations',
                                                'Avg. Donation Amount'))
    print("-"*80)
    # Takes donors and sorts it representing each item in the list
    sort_donor = sorted(donors, key = sort_key,reverse = True)
    # For loop going through donors and calculating sum, number of donations, and average donations
    # Then formatting them correctly into the table. Returns to main menu at the end.
    for donor in sort_donor:
        total = sum(donor[1])
        num_donations = len(donor[1])
        average = total/num_donations
        print('{:<20} ${:>11,.2f}{:>13}            ${:>11,.2f}'.format(donor[0], total, num_donations, average))
    return #return to main menu

#define sort key
def sort_key(donor):
    return sum(donor[1])


def exit_menu():
    print("Thank you, Goodbye...")
    sys.exit() # terminates the program


def main():
    while True:
        # call a definition  get user response number
        response = get_user_input(main_prompt)
        if response == "1":
            thank_you()
        elif response == "2":
            report()
        elif response == "3":
            exit_menu()
        else:
            print("Main menu input is invalid, enter 1 2 3 only please")

if __name__ == "__main__":
    main()



