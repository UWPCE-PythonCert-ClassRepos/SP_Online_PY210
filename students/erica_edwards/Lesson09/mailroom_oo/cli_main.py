
import sys
from donor_models import Donor
from donor_models import DonorCollection

donors = DonorCollection.from_dict(
           {'Sandy Pie': [75],
            'Judy Smith': [75, 100, 1000],
            'Mike Jones': [75, 1000],
            'Joe Smith': [75, 100, 2000],
            'Kelly Blue': [75, 150, 275]})


def menu():
    """Display user menu and process selections."""
    while True:
        print()
        print('''Menu:
                    1. Enter a Donation.

                    2. Generate Thank You messages.

                    3. View Donation Report.

                    4. Quit.''')
        print()
        try:
            response = int(input("Please enter a number to make your selection. "))-1
            switch_func_dict = {
                0: ask_donor_name,
                1: generate_letters,
                2: create_report,
                3: quit_now}
            switch_func_dict[response]()
        except (KeyError, ValueError):
            print("Please enter a menu option from 1-4.")


def quit_now():
    """Quit the application."""
    print('bye')
    sys.exit(0)


def ask_donor_name():
    """Enter a Donation, Step 1. Ask for donor name and validate or create new donor."""
    while True:
        donor_name = input("Enter the full name of the donor. ('list', or 'q' to quit) ")
        if donor_name.upper() == 'Q':
            return
        # If user types list print donors
        elif donor_name.upper() == "LIST":
            print(donors.list_donors())
            continue
        else:  # user didn't type list
            result = donors.donor_exists(donor_name)
            if result is False:
                answer = input("The donor name is not in the list of donors. "
                               "Do you want to add the donor? Yes or No ")
                if answer.upper() == "YES":
                    donor = Donor(donor_name)
                    ask_donation_value(donor)
                    return
                else:
                    continue
            else:
                ask_donation_value(donors.donors[donor_name])
                return


def ask_donation_value(donor):
    """Enter a Donation, Step 2. Ask donation value, validate, and append to donor's list."""
    while True:
        try:
            donation_amount = input("Enter the donation amount (or q to quit) ")
            if donation_amount.upper() == 'Q':
                return
            elif float(donation_amount) > 0:
                donor.donation_add(float(donation_amount))
                donors.add(donor)
                print(donor.single_donation_letter())
                return
            else:
                print("The number you enter must be greater than 0.")
                continue
        except ValueError:
            print('Invalid input. You must enter a number.')


def generate_letters():
    """Generate a letter for each donor in the collection."""
    donors.generate_letters()
    print('Generated letters.\n')


def create_report():
    """Display a report showing donations."""
    print(donors.create_report())


if __name__ == "__main__":
    menu()
