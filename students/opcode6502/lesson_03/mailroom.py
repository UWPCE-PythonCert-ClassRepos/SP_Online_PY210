# mailroom.py
# opcode6502: SP_Online_PY210

import sys

donors_db = [
    ("Donor 01", [100.00]),
    ("Donor 02", [200.00, 250.00]),
    ("Donor 03", [300.00, 350.00, 375.00]),
    ("Donor 04", [20.99, 3.01, 1576.89]),
]


def add_donation(donor_name, donation_amount):
    donors_db.append([donor_name, donation_amount])


def create_donor(donor_name):
    donors_db.append([donor_name, [0, 0, 0]])


def create_report():

    # Print the header rows.
    print('{:25} | {:1} | {:1} | {:1}'.format(
        "Donor Name",
        "Total Given",
        "Num Gifts",
        "Average Gift"))
    print('-'*66)

    # Sort the donor list.
    donors_db_sorted = sorted(donors_db, key=sort_donation_amount, reverse=True)

    # Print the donor list.
    for donor in donors_db_sorted:
        donor_name = donor[0]
        donor_total = sum(donor[1])
        number_of_gifts = len(donor[1])
        average_gift = float(donor_total) / float(number_of_gifts)
        average_gift = donor_total / number_of_gifts
        print('{:26} ${:>11.2f} {:>11}  ${:>12.2f}'.format(
              donor_name,
              donor_total,
              number_of_gifts,
              average_gift))


def exit_script():
    sys.exit()


def list_donor_names():

    # Sort the donor list.
    donors_db_sorted = sorted(donors_db, key=sort_donor_name)

    # Print the donor list.
    for donor in donors_db_sorted:
        donor_name = donor[0]
        print('{:26}'.format(donor_name))


def send_thank_you():
    while True:
        user_response = input(
                    '[ ----- ]: ------------------------------------------------------- \n'
                    '[ DONOR ]: Select an option:\n'
                    '[ ----- ]: ------------------------------------------------------- \n'
                    '[     1 ]: Type: \'list\'\n'
                    '[       ]:        Display a list of donors.\n'
                    '[     2 ]: Type: \'Existing Donor\'s Name\'\n'
                    '[       ]:        Add a new donation for a donor.\n'
                    '[     3 ]: Type: \'New Donor\'s Name\'\n'
                    '[       ]:        Create a new donor.\n'
                    '[     4 ]: Type: \'main\'\n'
                    '[       ]:        Return to the Main Menu.\n'
                    '[ INPUT ]: ')
        if user_response.lower() == 'list':
            list_donor_names()
            continue
        elif user_response.lower() == 'main':
            break
        for donor in donors_db:
            if user_response.upper() == donor[0].upper():

                # Get the donation amount.
                donation_amount = input("[ INPUT ]: Amount to add for {}: ".format(user_response))

                # Cast donation_amount to a list[] object and add the amount.
                donation_amount_list = []
                donation_amount_list.append(float(donation_amount))

                # Add the donation.
                add_donation(user_response, donation_amount_list)

                # Print the mail
                print(f"\n"
                "Dear {},\n\n"
                "Thank you for your donation of ${}.\n\n"
                "  Regards,\n"
                "  - the Thank You bot\n".format(donor[0],(float(donation_amount))))

                break
        else:
            create_donor(user_response)


def sort_donor_name(donor_name):
    return donor_name[0]


def sort_donation_amount(donation_amount):
    return sum(donation_amount[1])


def main():
    while True:
        user_response = input(
                    '[ ----- ]: ------------------------------------------------------- \n'
                    '[  MAIN ]: Select an option:\n'
                    '[ ----- ]: ------------------------------------------------------- \n'
                    '[     1 ]: Send a Thank You\n'
                    '[     2 ]: Create a Report\n'
                    '[     3 ]: Quit\n'
                    '[ INPUT ]: ')
        if user_response == '1':
            send_thank_you()
        elif user_response == '2':
            create_report()
        elif user_response == '3':
            exit_script()
        else:
            print("[ ERROR ]: Select item: 1, 2, or 3.")


if __name__=='__main__':
    main()
