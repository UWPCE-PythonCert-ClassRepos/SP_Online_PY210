#!/usr/bin/env python3

'''

'''

# create initial donor list
donors = [
    ("William Gates, III", [653772.32, 12.17]),
    ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
    ("Jeff Bezos", [877.33]),
    ("Paul Allen", [663.23, 43.87, 1.32])
    ]

def main():
    '''
    Prompt the user for input.  Current choices are to send a thank you or to
    create a report to display all the current donors and respective donation
    totals and averages.  The user can also quit.
    '''
    
    print("Welcome to the mailroom program")
    prompt = "\n".join((
        "Please choose a function from the below options:",
        "1 - Send a Thank You",
        "2 - Create a Report",
        "3 - Quit",
        ">> "
        ))

    while True:
        choice = input(prompt)
        if choice == "1":
            thank_you()
        elif choice == "2":
            create_report()
        elif choice == "3":
            print("Closing mailroom... Goodbye")
            break
        else:
            print(str(choice) + " is an invalid selection, "
            "please make a valid selection \n")



def thank_you():
    '''
    prompts the user for a full name.  If the user types "list", then print
    a list of donor names and re-prompt.  If a name is typed that is not
    in the list, add the name to the list.  If a name is typed that is
    already in the list, then use it.  Once a name is selected, a
    donation amount is specified.  Donation amount input by users is then
    added to the donation history of the name.  Email is then automatically
    drafted using string formatting thanking the donor for the donation.
    Return to main prompt after.
    '''

    while True:
        ty_input = input('Type "list" to display a list of donor names. '
        'Otherwise enter a name you would like to add a donation for:\n>>')

        if ty_input == "list":
            print_names()
        else:
            donation_amount = input("Please enter donation amount:\n>>")
            add_donation(ty_input, donation_amount)
            print_email(ty_input, donation_amount)
            break

def print_names():
    print("\nCurrent Donors: ")
    for donor in donors:
        print(donor[0])
    print()

def print_email(donor_name, donation_amount):
    '''
    Takes a donor's name and donation amount as parameters, and then creates
    an email template thanking them for their donation
    '''

    print(f"\nDear {donor_name},\n\n"
    f"It is with incredible gratitude that we accept your wonderfully generous "
    f"donation of ${float(donation_amount):,.2f}.  Your contribution will truly "
    "make a difference in the path forward towards funding our common goal."
    "\n\nEver Greatefully Yours,\n\n"
    "X" + ("_"* 20) + "\n")

def add_donation(donor_name, donation_amount):
    pass

def create_report():
    '''
    Prints a list of donors, sorted by total historical donation
    amount.  Includes donor name, total donated, number of donations,
    and average donation amount.  
    '''

if __name__ == "__main__":
    '''
    run main prompt
    '''

    main()