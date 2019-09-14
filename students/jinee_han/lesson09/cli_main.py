import donor_models as donor_models
import sys

donor_collection = donor_models.DonorCollection()

# Display options
prompt = "\n".join(("Welcome to the donor list!",
          "Please choose from below options:",
          "1 - Send a Thank you",
          "2 - Create a Report",
          "3 - Exit",
          ">>> "))

def display_list():

    '''
    Display the list of current donors
    :return: prints donor names
    '''

    for d in donor_collection.donors:
        print(d.donor_name)


def send_thank_you_note():

    '''
    Check for the user input and send a thank you once user entered
    :return: nothing
    '''

    input_value = input("Enter a full name. (Type 'list' to see the donor list)")  # Ask the name
    while input_value == 'list':
        display_list()
        input_value = input("Enter a full name. (Type 'list' to see the donor list)")

    # Store the donor name with the first character as an upper case letter
    donor_name = input_value.title()

    donor_not_present = False
    new_donor = None
    if not donor_collection.donor_present(donor_name):
        donor_not_present = True
        new_donor = donor_models.Donor(donor_name)
    else:
        new_donor = next((d for d in donor_collection.donors if d.donor_name == donor_name), None)

    donation_amount = None
    while donation_amount is None:
        try:
            donation_amount = float(input("Please enter the donation amount: "))
            if (donation_amount <= 0):
                print ("Please enter a donation amount larger than zero.")
                donation_amount = None
                pass
        except ValueError:
            print ("Please enter a valid donation amount.")
            pass

    new_donor.add_donation(donation_amount)

    if donor_not_present:
        donor_collection.add_donor(new_donor)

    # send thank you
    print(new_donor.format_thank_you_note(donation_amount))


def create_report():

    '''
    Create the donor report
    :return: Print donor report to console
    '''

    print(donor_collection.create_report())


def exit_program():

    '''
    Exit the program
    :return: nothing
    '''

    print("Thank you for your donations!")
    sys.exit()  # exit the interactive script


def initialize_donors():

    '''
    Initialize the donor collection with the same donors and amounts as Mailroom1
    now using the newly created objects
    :return: void
    '''

    donor_kim = donor_models.Donor("Kim Kardasian")
    donor_kim.add_donation(653772.32, 12.17)
    donor_kendal = donor_models.Donor("Kendal Jenner")
    donor_kendal.add_donation(877.33)
    donor_gigi = donor_models.Donor("Gigi Hadid")
    donor_gigi.add_donation(663.23, 43.87, 1.32)
    donor_justin = donor_models.Donor("Justin Bieber")
    donor_justin.add_donation(1663.23, 4300.87, 10432.0)
    donor_will = donor_models.Donor("Will Smith")
    donor_will.add_donation(43.23, 4000.07, 183423.2)
    donor_collection.add_donor(donor_kim, donor_kendal, donor_gigi, donor_justin, donor_will)


input_dict = {1: send_thank_you_note, 2: create_report, 3: exit_program}

def main():

    '''
    Run the main function to handle user input and displaying options
    :return: void
    '''

    initialize_donors()
    while True:
        try:
            response = int(input(prompt))  # continuously collect user selection
            input_dict.get(response)()
        except TypeError:
            print("Please enter a number between 1 - 3.\n")
        except ValueError:
            print("Please enter a number between 1 - 3.\n")


if __name__ == "__main__":
    main()