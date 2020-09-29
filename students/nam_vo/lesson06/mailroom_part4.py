import sys  # imports go at the top of the file
import os
from collections import defaultdict

# Initialize dictionary of donors with their names and the amounts they have donated
donor_dict = defaultdict(
    list,
    {
        "William Gates, III": [653772.32, 12.17],
        "Jeff Bezos": [877.33],
        "Paul Allen": [663.23, 43.87, 1.32],
        "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
        "Bill Nordstrom": [2013.25, 23456.78],
    },
)

def send_single():
    """Compose an email thanking the donor for their generous donation."""

    # Ask for donor's full name
    name = input("Enter donor's full name (or 'list' to list all donor' names): ")
    # Continue asking for donor's full name
    while name == "list":
        # Get list of donor names
        names = get_names(donor_dict)
        # Display list of donor names
        print(names)
        # Ask for donor's full name
        name = input("Enter donor's full name (or 'list' to list all donor' names): ")
    # Continue asking for a valid donated amount
    while True:
        # Prompt for a donation amount
        response = input("Enter donation amount: $")
        # Convert user's prompt in string to float
        try:
            amount = float(response)
        except ValueError:
            print("Not a valid amount!")
        else:
            # The input amount is valid, stop asking for donated amount
            break
    # Add/update donor with the amount they have donated
    update_donor(donor_dict, name, amount)
    # Generate thank you text to send to the donor
    prompt = generate_text(name, amount)
    print(prompt)
  
def create_report():
    """
    Return a final report consists of a list of donors, sorted by total historical donation amount.

    Sample:
Donor Name                | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------
William Gates, III         $  653784.49           2  $   326892.24
Mark Zuckerberg            $   16396.10           3  $     5465.37
Jeff Bezos                 $     877.33           1  $      877.33
Paul Allen                 $     708.42           3  $      236.14

    """

    # Initialize report
    report = ""
    # Sort the donor's dictionary by total historical donation amount
    sorted_donor_list = sorted(donor_dict.items(), key=sort_key, reverse=True)
    # Print header
    fheader = "{:<26}|{:^13}|{:^11}|{:>13}"
    print(fheader.format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print('-' * 66)
    # Get body format
    fbody = "{:<27}${:>11.2f}{:>12}  ${:>12.2f}"
    # Loop thru each donor in the dictionary
    for donor in sorted_donor_list:
        # Get total donated amount, number of gifts, and average gift amount
        total_given = sum(donor[1])
        num_gifts = len(donor[1])
        ave_gift = total_given / num_gifts
        # Get current row report and add it to the final report
        row = fbody.format(donor[0], total_given, num_gifts, ave_gift)
        report += row + "\n"   
    # Display final report
    print(report)

    return report

def send_all():
    """Generate a thank you letter for each donor in the list and write each letter to current working directory as text file"""

    # Loop thru each donor's name in the dictionary
    for (name, donations) in donor_dict.items():
        # Get the latest amount of donation
        amount = donations[len(donations) - 1]
        # Assign file name
        file_name = name.replace(' ', '_').replace(',', '') + ".txt"
        # Open file for writing
        with open(file_name, 'w') as outFile:
            # Get letter's content
            data = get_letter_text(name, amount)
            # Write content to file
            outFile.write(data)
            # Print success message
            print(f'File "{file_name}" has been created in current working directory!')

def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script

def get_user_select(user_select):
    """
    Return a string contains user's selections

    :user_select: dictionary of all user's selections
    """
    prompt = "\nChoose an action:\n\n"
    for (key, val) in user_select.items():
        prompt += f"{key} - {val}\n"
    prompt += ">>> "

    return prompt

def get_names(donor_dict):
    """
    Return a list of all donor names separated by newline character.

    :donor_dict: dictionary of donor's full name and list of amounts they have donated
    """

    return "\n".join(list(donor_dict))

def update_donor(donor_dict, name, amount):
    """
    Add/update donor in the dictionary with the amount they have donated

    :donor_dict: dictionary of donor's full name and list of amounts they have donated
    :name: new donor to be added/updated in the donor dictionary
    :amount: donated amount
    """

    donor_dict[name].append(amount)

    return f"{name}: {donor_dict[name]}"

def generate_text(name, amount):
    """
    Return thank you text to send to the donor

    :name: name of the donor
    :amount: donated amount
    """
    
    return "\nDear {:s},\n\n        Thank you for your very kind donation of ${:.2f}.\n\n        It will be put to very good use.\n\n                       Sincerely,\n                          -The Team\n".format(name, amount)

def sort_key(item):
    """
    Return total donated amount for selected donor, which will be used as key for the sorted() function.

    :item: pair of donor's name and list of amounts they have donated
    
    """
    return sum(item[1])

def get_letter_text(name, amount):
    """
    Return letter's content

    :name: name of the donor
    :amount: donated amount
    """
    
    return "\nDear {:s},\n\n        Thank you for your very kind donation of ${:.2f}.\n\n        It will be put to very good use.\n\n                       Sincerely,\n                          -The Team\n".format(name, amount)

# Initialize dictionary of user's selections and corepsonding actions
user_select = {
    1: "Send a Thank You to a single donor",
    2: "Create a Report",
    3: "Send letters to all donors",
    4: "Quit",
}
user_action = {
    1: send_single,
    2: create_report,
    3: send_all,
    4: exit_program,
}

def main():
    while True:
        # Get user's selections
        prompt = get_user_select(user_select)
        # Continuous get user selection
        try:
            response = int(input(prompt))
        except ValueError:
            print("Please enter a number!")
            continue
        # now redirect to feature functions based on the user selection
        try:
            user_action.get(response)()
        except TypeError:
            print("Not a valid option!")

if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()
