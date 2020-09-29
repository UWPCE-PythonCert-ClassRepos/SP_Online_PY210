#! bin/user/env python3
import sys
"""Program Part1:
It should have a data structure that holds a list of your donors and a history of the amounts they have donated.
This structure should be populated at first with at least five donors, with between 1 and 3 donations each.
You can store that data structure in the global namespace.
The script should prompt the user (you) to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”."""
# Donor name, donation amount, donation history
donor_list = [["John Doe", 2000, 2],
              ["Jane Doe", 3000, 3],
              ["George Washington", 1, 1],
              ["Andrew Jackson", 20, 2],
              ["Benjamin Franklin", 100, 3]]

# Main options menu for user to pick from
def main():
    while True:
        options()  # Display each option to the user
        choice = input("What would you like to do? ")
        if choice == "1":
            thank_you()
        elif choice == "2":
            report(donor_list)
        elif choice == "3":
            print("Done")
            sys.exit()  # Exit the script
        else:
            print("Please choose again.", "\n")

# Menu of options for the user in the script
def options():
    print("You have 3 options to choose from: ", "\n"
        "1) Send Thank you", "\n"
        "2) Create Report", "\n"
        "3) Exit"), "\n"

# Ask for a donor name and donation amount, send an email to that donor once completed
def thank_you():
    name = input("Enter a first and last name: ").title()
    if name.lower() == "list":
        print(donor_list)
        thank_you()
    gift = float(input("Enter a donation amount: "))
    for donor in donor_list:
        if name in donor:
            donor[1] += gift  # Total balance of donations
            donor[2] += 1  # Keeping track of donation history
            break  # If donor is in the list, break out
    else:
        if name not in donor:
            donor_list.append([name, gift, 1])
    # Thank you email to the donor
    print(f"Thank you {name} for your generous donation of ${gift:.2f}, your kindness is very appreciated.", "\n")

# Show a list of current donor's in the list and sorted by total number of donations
def report(seq):
    donor_list.sort(reverse=True, key=sort_list)
    fields = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    report_list = []
    print(f"{fields[0]:<20} | {fields[1]:<11} | {fields[2]:<3} | {fields[3]}")
    print("{}".format('-' * 61))
    for item in seq:
        report_list.append((item[0], item[1], item[2], item[1]/item[2]))
    for donor in report_list:
        print(f"{donor[0]:<20} $ {donor[1]:>11.2f} {donor[2]:>11} $ {donor[3]:>11.2f}")

# Sort the list by the 2nd position in a sequence
def sort_list(seq):
    return seq[2]

if __name__ == "__main__":
    print("Mailroom script has been started. ")
    main()