#!/usr/bin/env python3
import sys

# Hard coded donor records
donor_records = [("Rhianna", [747, 3030303, 1968950]), 
    ("Grumps", [5.99]), ("EatPraySlay", [100000,200000, 300000]), 
    ("Muir", [469503, 50000, 186409]), ("Spacewalker", [4406, 342])]

# Store new donation record, then create e-mail to thank donor
def thank_donor():

    while True:
        donor_name = input("Who would you like to thank? "
            "(Type 'list' to see a list of donors.)\n  Full Name: ")
        entry_exists = False

        # Print list of existing donors to choose from
        if donor_name.lower() == "list":
            entry_exists = True
            for i in donor_records:
                print(i[0])

        # Locate the record for the donor entered, then get and store 
        # the donation amount
        else:
            for i in donor_records:
                if donor_name.lower() == i[0].lower():
                    entry_exists = True
                    donation_amount = float(input(
                        "Please enter the donation amount: "))
                    i[1].append(donation_amount)
        
            # If this is a new donor, collect and store the donor info
            if entry_exists == False:
                donation_amount = float(input(f"Adding {donor_name} to "
                    "the database.\nPlease enter the donation amount: "))
                donor_records.append([donor_name, [donation_amount]])

            # Generate the thank you e-mail
            print(f"To the esteemed {donor_name}:\n\n"
                "Thank you for generous donation of "
                f"${donation_amount:.2f}. You're a champion!")
         
            # Return donor records
            return(donor_records)

# Create a report of all donor records to date
def create_report():
    # Set up column headers
    print(" "+"-"*60+"\n Donor Name"+" "*10+
        "| Total Given | Num Gifts | Average Gift\n "+"-"*60)
    
    # Generate and print donor summaries
    donor_summary = []
    for record in donor_records:
        donor_summary.append([record[0], sum(record[1],0), 
            len(record[1]), sum(record[1],0)/len(record[1])])
    for i in donor_summary:
        print(" {0:<20} ${1:>11.2f}{2:>12}  ${3:>12.2f}".format(*i))

# Display a user menu, then act on the user's selection
def main():
    # Let the user choose what to do, then call the function to make it
    # happen and repeat until the user quits
    while True:
        
        user_action = input("\n".join(("\nWhat would you like to do?", 
            "  Enter 1 to Send a Thank You",
            "  Enter 2 to Create a Report",
            "  Enter q to quit.",
            "  >>>")))

        if user_action == "1":
            thank_donor()

        elif user_action == "2":
            create_report()

        elif user_action[0].lower() == "q":
            print("\nThanks for playing!")
            sys.exit()
        
        else:
            print("Let's behave. Try again using one of the options!")

if __name__ == "__main__":
    main()
