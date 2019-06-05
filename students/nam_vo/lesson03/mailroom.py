import sys  # imports go at the top of the file

# Initialize list of donors with their names and the amounts they have donated
donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ("Bill Nordstrom", [2013.25, 23456.78]),
            ]

prompt = "\n".join(("Welcome to the mail room!",
          "Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - quit",
          ">>> "))

def send_thankyou():
    """Compose an email thanking the donor for their generous donation."""
    # Ask for donor's full name
    name = input("Enter donor's full name (or 'list' to list all donor' names): ")
    # Continue asking for donor's full name
    while name == "list":
        # Display list of donor names
        print_donor(donor_db)
        # Ask for donor's full name
        name = input("Enter donor's full name (or 'list' to list all donor' names): ")
    # Get index of existing/new donor in the list
    index = add_donor(name, donor_db)
    # Prompt for a donation amount
    response = input("Enter donation amount: $")
    # Convert user's prompt in string to float
    amount = float(response)
    # Add new amount to the donation history of the selected donor
    donor_db[index][1].append(amount)
    # Compose thank you email to the donor
    prompt = "\n\n".join((
        f"\nDear {name},",
        "Thank you for your generous donation in the amount of ${:.2f}! Have a great day!\n".format(amount),
    ))
    print(prompt)
    
def create_report():
    """
    Print a list of donors, sorted by total historical donation amount.

    Sample:
    Donor Name                | Total Given | Num Gifts | Average Gift
    ------------------------------------------------------------------
    William Gates, III         $  653784.49           2  $   326892.24
    Mark Zuckerberg            $   16396.10           3  $     5465.37
    Jeff Bezos                 $     877.33           1  $      877.33
    Paul Allen                 $     708.42           3  $      236.14

    """
    # Sort the donor's list by total historical donation amount
    sorted_donor_db = sorted(donor_db, key=sort_key, reverse=True)
    # Print header
    fheader = "{:<26}|{:^13}|{:^11}|{:>13}"
    print(fheader.format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print('-' * 66)
    # Get body format
    fbody = "{:<27}${:>11.2f}{:>12}  ${:>12.2f}"
    # Loop thru each donor in the list
    for donor in sorted_donor_db:
        # Get total donated amount, number of gifts, and average gift amount
        total_given = sum(donor[1])
        num_gifts = len(donor[1])
        ave_gift = total_given / num_gifts
        # Print report
        print(fbody.format(donor[0], total_given, num_gifts, ave_gift))

def sort_key(donor):
    """
    Return total donated amount for selected donor, which will be used as key for the sorted() function.

    :donor: a tuple contains two items: name and list of donated amounts
    
    """
    return sum(donor[1])

def add_donor(name, donor_list):
    """
    Return index of the selected donor. If it's new, add it to the donor list.

    :name: full name of the new donor
    :donor_list: list of all donors

    """
    # Get index of existing donor
    for (index, donor) in enumerate(donor_list):
        if name == donor[0]:
            break
    # If it's a new donor, add it to the list and return it's index
    else:
        donor_list.append((name, []))
        index = len(donor_list) - 1

    return index

def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script

def print_donor(donor_list):
    """
    Print all donor names.

    :donor_list: list of tuples with the first entry in each tuple is a donor's full name

    """
    for donor in donor_list:
        print(donor[0])

def main():
    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "1":
            send_thankyou()
        elif response == "2":
            create_report()
        elif response == "3":
            exit_program()
        else:
            print("Not a valid option!")


if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()
