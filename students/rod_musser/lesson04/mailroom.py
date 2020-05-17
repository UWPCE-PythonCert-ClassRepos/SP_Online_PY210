#!/usr/bin/env python3
import sys

donors = {
    'Carmelo Anthony': [1, 50],
    'Damien Lillard': [100.50, 99, 10000],
    'CJ McCollum': [24000, 70, 100, 5, 300],
    'Hassan Whiteside': [10000],
    'Terry Stotts': [500, 500, 100, 100, 100],
}


welcome_prompt = "\n".join(("Welcome to the Local Charity Mail Room System",
                  "Please choose from the following options:",
                  "1 - Send a Thank You",
                  "2 - Create a Report",
                  "3 - Send Letters To All Donors",
                  "4 - Quit",
                  ">>> "))

letter_template = "Dear {first_name} {last_name},\n\n\
Thank you for your generous support of Rod's Early \
Retirement Fund.\n\nYour {num_donations} donation(s) \
totaling ${total_donation:.2f} makes Rod's early retirement \
dreams a reality.  Your generous support will enable Rod \
to perform critical early retirement tasks like \n\n\t- \
Mai Tais on the beach \n\t- First class airline travel \
\n\t- Alpine skiing.  \n\nAgain, thank you {first_name} \
for your generous support. \n\nSincerely, \n\nRod Musser \
\nChairperson\nRod's Early Retirement Fund"


def main():
    while True:
        response = input(welcome_prompt)
        menu_selection = main_menu_dict.get(response)
        if menu_selection is None:
            print("Not a valid option!")
        else:
            menu_selection()


def list_donors():
    newLine = '\n'
    print(f"{newLine.join(donors.keys())}")


def send_thank_you():
        response = input("Please enter a full name: ")
        if response.lower() == "list":
            list_donors()
            send_thank_you()
        else:
            amount = input("Please enter the donation amount: ")
            add_donation(response, float(amount))


def add_donation(donor_name, amt):
    """
    Records a donation and prints a thank you email.
    Expects a list which contains a donor and a list of amounts.
    """
    donors.setdefault(donor_name, []).append(amt)
    letter_data = {}
    first_last = donor_name.split(' ')
    v = donors[donor_name]
    letter_data['first_name'] = first_last[0]
    letter_data['last_name'] = first_last[1]
    letter_data['total_donation'] = sum(v[:])
    letter_data['num_donations'] = len(v)
    print(get_letter_text(letter_data))


def sort_key(donor_summary):
    return donor_summary[1]


def create_report():
    report = []
    for k, v in donors.items():
        total_amount = sum(v[:])
        number_of_gifts = len(v)
        average_gift = round(total_amount / number_of_gifts, 2)
        donor_summary = [k, total_amount, number_of_gifts, average_gift]
        report.append(donor_summary)
    print_report(sorted(report, key=sort_key, reverse=True))


def print_report(report):
    print("Donor Name" + (' ' * 16) + ("| Total Given | Num Gifts | Avergage Gift"))
    print("-" * 68)
    row = "{name:<26s} ${total:=12.2f}  {num:10d} ${avg:14.2f}".format
    for donor in report:
        print(row(name=donor[0], total=donor[1], num=donor[2], avg=donor[3]))


def send_letters():
    letter_directory = input("Which directory shall I write the letters in?: ")
    if not letter_directory.endswith('/'):
        letter_directory = letter_directory + '/'

    all_letter_data = create_letter_data()
    for letter_data in all_letter_data[:]:
        letter_file_name = letter_directory + '{first_name}_{last_name}.txt'.format(**letter_data)
        with open(letter_file_name, 'w') as f:
            f.write(get_letter_text(letter_data))


def get_letter_text(letter_data):
    return letter_template.format(**letter_data)


def create_letter_data():
    all_letter_data = []
    for k, v in donors.items():
        letter_data = {}
        first_last = k.split(' ')
        letter_data['first_name'] = first_last[0]
        letter_data['last_name'] = first_last[1]
        letter_data['total_donation'] = sum(v[:])
        letter_data['num_donations'] = len(v)
        all_letter_data.append(letter_data)
    return all_letter_data


def exit_program():
    print("You made a difference today.  Have a good one!")
    sys.exit()


main_menu_dict = {
    '1': send_thank_you,
    '2': create_report,
    '3': send_letters,
    '4': exit_program
}

if __name__ == "__main__":
    main()
