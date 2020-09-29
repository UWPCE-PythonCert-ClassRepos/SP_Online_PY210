#Chris Dela Pena
#UW PCE PY210
#Assignment 3 - Mailroom Part 1
#2020/6/14

"""
Deliverable:
It should have a data structure that holds a list of your donors and a
history of the amounts they have donated. This structure should be populated
at first with at least five donors, with between 1 and 3 donations each.
You can store that data structure in the global namespace.
The script should prompt the user (you) to choose from a menu of 3
actions: “Send a Thank You”, “Create a Report” or “quit”.

If the user (you) selects “Send a Thank You” option, prompt for a Full Name.
If the user types list show them a list of the donor names and re-prompt.
If the user types a name not in the list, add that name to the data structure
and use it.
If the user types a name in the list, use it.
Once a name has been selected, prompt for a donation amount.
Convert the amount into a number; it is OK at this point for the program to
crash if someone types a bogus amount.
Add that amount to the donation history of the selected user.
Finally, use string formatting to compose an email thanking the donor for
their generous donation. Print the email to the terminal and return to the
original prompt.

If the user (you) selected “Create a Report,” print a list of your donors,
sorted by total historical donation amount.
Include Donor Name, total donated, number of donations, and average donation
amount as values in each row. You do not need to print out all of each donor’s
donations, just the summary info.
Using string formatting, format the output rows as nicely as possible. The
end result should be tabular (values in each column should align with those
above and below).
After printing this report, return to the original prompt.
At any point, the user should be able to quit their current task and return
to the original prompt.
From the original prompt, the user should be able to quit the script cleanly.
"""

import sys


donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]
            )]

prompt = "\n".join(("Mail Room Program version 1.0",
            "Please choose from below options:",
            "1 - Send a Thank you",
            "2 - Create a Report",
            "3 - Quit",
            ">>> "))

prompt_name = "\n".join(("Please enter the full name of the donor",
                "or type 'list' to see a full list of donor names",
                "or type 'q' to quit."
                ">>> "))

prompt_amount = "\n".join(("What was the donation amount?",
                ">>> "))

def thank_you():
    donor_name = input(prompt_name)
    if donor_name.upper() == 'Q':
        return
    elif donor_name.upper() == "LIST":
        for donor in donor_db:
            print('-'*60)
            print(donor[0])
            print('-'*60)
    else:
        #if donor is found in db
        for i in donor_db:
            if donor_name == i[0]: #Use i[0] to handle tuple
                donation_amount = input(prompt_amount)
                donation_amount = float(donation_amount) #String to float
                i[1].append(donation_amount) ##i[1] to add into tuple
                print('-'*60)
                print(f"Dear {donor_name}, thank you for your generous donation of ${donation_amount}."
                " Regards, the Club Owners")
                print('-'*60)
                return
        else:
            print('-'*60)
            print(f"Adding new donor {donor_name}")
            donation_amount = input(prompt_amount)
            donation_amount = float(donation_amount) #String to float
            print('-'*60)
            new_donor = (donor_name, [donation_amount])
            donor_db.append(new_donor)
            return

def donor_report():
    print('-'*60)
    print('-'*60)
    header = ["Donor", "Total Donated", "Times Donated", "Average Donation"]
    print(f"{header[0]:<20}{header[1]:<15}{header[2]:<15}{header[3]:<7}")
    print('-'*60)
    #Create sorted list
    donors_sorted = sorted(donor_db, key=sort_key,reverse=True)

    for i in donors_sorted:
        print(f"{i[0]:<20}{sum(i[1]):<15.2f}{len(i[1]):<15}{sum(i[1])/len(i[1]):<7.2f}")
    print('-'*60)

def sort_key(donor_db):
    return sum(donor_db[1])

def quit():
    print("Goodbye and have a great day!")
    sys.exit()

def main():
    while True:
        response = input(prompt)
        if response == "1":
            thank_you()
        elif response == "2":
            donor_report()
        else:
            quit()

if __name__ == "__main__":
    main()
