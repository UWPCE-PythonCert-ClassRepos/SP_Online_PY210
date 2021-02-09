#!/usr/bin/env python

# ------------------------------------------------------------------------------ #
# Title: Lesson06 - Mailroom Part 4 Assignment
# Description: Assignment from Lesson06 - Mailroom Part 4
# ChangeLog (Who,When,What):
# Mercedes Gonzalez Gonzalez,01-30-2021, Created Mailroom Part 4
# ------------------------------------------------------------------------------ #

# User Presentation Layer


def print_main_menu():
    """
    Display a menu of actions
    :return: nothing
    """
    print("""
    Choose an action:
     
    1 - Send a Thank You to a single donor
    2 - Create a Report.
    3 - Send letters to all donors.
    4 - Quit

    """)


def print_thank_you_menu():
    print("""
    You will be presented with a set of questions to identify which donor should receive 
    the 'Thank you!' email.
    
    1 - Specify which donor should receive a thank you email 
    2 - List existing donors' data 
    3 - Quit (Back to Main Menu)

    """)


def input_choice(msg):
    """
    Gets the menu choice from the user
    :return: string
    """
    choice = str(input(msg)).strip()
    return choice


def print_data_to_user(data):
    print(data)


# Business Logic (Unit-testable)
def generate_email(donor_full_name, total_donation):
    email_to_donor = (
        "Dear {},\nWe would like to thank you for your donation. So far, you "
        "have donated ${:.2f} to our organization and for that, we are grateful."
        "You are helping us continue our work supporting and growing our "
        "community.\nYou truly make a difference! We could not do this work "
        "without your support.\n\n"
    ).format(donor_full_name.title(), total_donation)
    return email_to_donor


def send_thank_you_to_single_donor(donor_records):
    while True:
        print_thank_you_menu()
        choice = input_choice("Which action would you like to perform? ")

        if choice == '1':
            donor_full_name = input_choice("What is the full name of the donor?: ").lower()
            try:
                donation_amount = input_choice(
                    "How much did {} donate to the cause? $ ".format(donor_full_name.title())
                )
                donation_amount = float(donation_amount)
            except ValueError:
                print_data_to_user("\nThe donation amount introduced is not a valid number (i.e: 300.00). Please try again!")
                continue
            if donation_amount > 0:
                for donor in donor_records:
                    if donor_full_name == donor['full_name']:
                        donor['donation_history'].append(donation_amount)
                        total_donation = sum(donor['donation_history'])
                        break
                else:
                    donor_records.append(
                        {
                            'full_name': donor_full_name,
                            'donation_history': [donation_amount]
                        }
                    )
                    total_donation = donation_amount
                print_data_to_user("{}'s donation for $ {:.2f} will be saved in our records".format(
                    donor_full_name.title(),
                    donation_amount)
                )
                email = generate_email(donor_full_name, total_donation)
                print_data_to_user(email)
            else:
                print_data_to_user("A donation needs to be higher than zero dollars in order to be added to the donor's records")
        elif choice == '2':
            print_data_to_user(generate_donor_records(donor_records))
        elif choice == '3':
            break
        else:
            print_data_to_user("Your selection is invalid. Please select a menu option from 1 to 3")


def generate_donor_records(donor_records):
    donor_records_text = ""
    if len(donor_records):
        donor_records_text += "******* The current donors are: *******\n"
        headers = ('Donor Full Name', 'Total Given', 'Num Gifts', 'Average Gift')
        header_str = "{:<20s} | {:>16s} | {:^15s} | {:>16s}\n".format(*headers)
        donor_records_text += header_str
        donor_records_text += "-" * len(header_str)
        for donor in donor_records:
            donor_records_text += "\n{:<20s}   ${:>15.2f}   {:>15d}   ${:>15.2f}".format(
                donor['full_name'].title(),
                sum(donor['donation_history']),
                len(donor['donation_history']),
                sum(donor['donation_history']) / len(donor['donation_history'])
            )
    else:
        donor_records_text += "There are no donors in our current database records. Please add them"
    return donor_records_text


def create_donor_report(donor_records):
    donor_records = sorted(donor_records, key=lambda donor: sum(donor['donation_history']), reverse=True)
    print_data_to_user(generate_donor_records(donor_records))


def read_data_from_file(filename, donor_records):
    donor_records.clear()
    try:
        with open(filename, 'r') as fh:
            for line in fh:
                full_name, donation_history = line.strip().split(';')
                donor = {
                    'full_name': full_name.strip().lower(),
                    'donation_history': [float(amount) for amount in donation_history.strip().split(',')]
                }
                donor_records.append(donor)
    except FileNotFoundError:
        print("File {} does not exist. The donors record history is currently empty!".format(filename))
    return donor_records


def write_data_to_file(filename, donor_records):
    with open(filename, "w+") as fh:
        for donor in donor_records:
            donation_history = [str(amount) for amount in donor['donation_history']]
            donor_str = "{};{}\n".format(donor['full_name'], ','.join(donation_history))
            fh.write(donor_str)


def say_goodbye(filename, donor_records):
    if len(donor_records):
        write_data_to_file(filename, donor_records)
    print_data_to_user("GoodBye!")


def send_letter_to_all_donors(donor_records):
    if len(donor_records):
        for donor in donor_records:
            email = generate_email(donor['full_name'], sum(donor['donation_history']))
            donor_filename = "{}.txt".format(donor['full_name'].replace(' ', '_'))
            with open(donor_filename, "w+") as fh:
                fh.write(email)
        print_data_to_user("A letter has been set to every donor in our records!")
        return True
    else:
        print_data_to_user("There are no donors in our current database records. Please add them")
        return False


def main():
    # Loading donors data if it exists
    filename = 'donors.txt'
    donor_records = []
    donor_records = read_data_from_file(filename, donor_records)

    # Display the menu
    while True:
        print_main_menu()
        choice = input_choice("Which action would you like to perform? ")

        if choice == '1':
            send_thank_you_to_single_donor(donor_records)
        elif choice == '2':
            create_donor_report(donor_records)
        elif choice == '3':
            send_letter_to_all_donors(donor_records)
        elif choice == '4':
            say_goodbye(filename, donor_records)
            break
        else:
            print_data_to_user("Your selection is invalid. Please select a menu option from 1 to 4")


if __name__ == "__main__":
    main()
