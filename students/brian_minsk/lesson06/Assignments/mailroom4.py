# Author: Brian Minsk

import pathlib
import tempfile

donor_db = {"Dee Zaster": ({"first_name": "Dee", "last_name": "Zaster",
                            "donations": [10000.00, 1500.00]}),
            "Owen Money": ({"first_name": "Owen", "last_name": "Money",
                            "donations": [7000.00]}),
            "Shanda Lear": ({"first_name": "Shanda", "last_name": "Lear",
                             "donations": [100.00, 900.00, 1500.00]}),
            "Joe King": ({"first_name": "Joe", "last_name": "King",
                          "donations": [500.00, 700.00, 500.00]}),
            "Artie Choke": ({"first_name": "Artie", "last_name": "Choke",
                             "donations": [1600.00, 1800.00]})}

main_prompt = "\n".join(("Please choose an option:",
                         "1 - Send a Thank You",
                         "2 - Create a Report",
                         "3 - Send letters to all donors",
                         "4 - Quit",
                         ">>> "))

thank_you_prompt = "\n".join(("Please type a donor name or type 'list' to "
                              "show all the donor names:", ">>> "))

donation_amount_prompt = "\n".join(("Please type the donation amount:",
                                    ">>> "))


def send_thank_you():
    """ Prompt the user to type a name or type 'list'.
    - If the user types 'list' show a list of the donor names and re-prompt.
    - Check if the donor name the user typed is already in the db.
    - If the user types a name not in the list, add that name to the donor
        db and use it.
    - If the user types a name in the list, use it.
    - Get the donation amount for the donor.

    Compose an email thanking the donor for their generous donation.
    Print the email to the terminal and return to the original prompt.
    """
    donation_amount = None
    donor = None

    while True:
        response = input(thank_you_prompt)
        if response.lower() == "list":
            show_donor_list()
        else:
            donor = process_donor_name_input(response)
            if not donor:
                continue
            else:
                donor = get_donor(response)
            donation_amount = add_donation(donor)
            print(thank_you_message(response, donation_amount))
            break


def process_donor_name_input(donor_name):
    """ If there is a donor with donor_name already in the db return it.
    If not already in the db:
    - check for a valid name.
    - If the name is not valid inform the user and return None.
    - If the name is valid add a donor with donor_name and return the donor.

    Keyword arguments:
    donor_name - string representing a donor name
    """
    donor = get_donor(donor_name)
    if not donor:  # Donor does not exist
        try:
            test_name(donor_name)
        except ValueError:
            print('Name should be of the form "Firstname Lastname"')
            return None
        donor = add_donor(donor_name)

    return donor


def test_name(donor_name):
    """ Test if the name is of the form "Firstname Lastname" i.e. a string
    with one space in the middle. If not, raise a ValueError exception.

    Keyword arguments:
    donor_name - a string
    """
    if donor_name.count(" ") != 1:
        raise ValueError
        return False

    if (donor_name.find(" ") == 0
            or donor_name.find(" ") == len(donor_name) - 1):
        raise ValueError
        return False

    return True


def send_letters():
    """ Create a message for each donor in the donor_db and save each message
    to a file. File will be created in a default temp directory and the file
    name will be the full name of the donor with spaces replaced by
    underscores.
    """
    destination_path = get_file_destination_path()

    for donor_id in donor_db:
        donor_data = donor_db[donor_id]
        donor_name = "{first_name} {last_name}".format(**donor_data)
        # assume the donation amount to use is the last donation
        donation_amount = donor_data["donations"][-1]
        message = thank_you_message(donor_name, donation_amount)

        create_letter_file(message, donor_name, destination_path)

    return destination_path


def create_letter_file(message, donor_name, destination_path):
    """ Create a file with a thank you message for a donor.

    Keyword arguments:
    message - The text to add to the file.
    donor_name - string representing the donor's name
    destination_path - location where the file will be created
    """
    destination_filename = get_destination_filename(destination_path,
                                                    donor_name)
    try:
        with open(destination_filename, "w") as f:
            f.write(message)
    except OSError as err:
        print("File {} error:/n{}".format(destination_filename, err.strerror))

    return destination_filename


def get_destination_filename(destination_path, donor_name):
    """ Return a filename, including the full path. The file will be named with
    the donor's name with an underscore replacing the space between the first
    and last name.

    Keyword arguments:
    destination_path - location where the file will be created
    donor_name - string representing the donor's name
    """
    filename = pathlib.Path("{}.txt".format(donor_name.replace(" ", "_")))
    return destination_path / filename


def get_file_destination_path():
    """ Find a file path, inform the user what it is, and return it. First try
    temporary directories. If no temporary directory exists, return the
    current directory.
    """
    try:
        destination_path = tempfile.gettempdir()
    # this exception will be raised if no appropriate directory is
    # found by gettempdir
    except FileNotFoundError:
        destination_path = pathlib.Path('./')  # use the current directory
    print("Files will be written to {} ".format(destination_path))

    return destination_path


def show_donor_list():
    """ Print donor names to the screen.
    """
    donor_name_list = make_donor_name_list()
    for donor_name in donor_name_list:
        print(donor_name)


def make_donor_name_list():
    """ Return a list of donor names.
    """
    return ["{} {}".format(donor_db[donor_id]["first_name"],
                           donor_db[donor_id]["last_name"]) for donor_id in donor_db]


def is_existing_donor(donor_name):
    """ Iterate through the donor db to see if the donor_name matches a donor.
    If so, return True. If not, return False.

    Keyword arguments:
    donor_name - string to match against the donor names in the donor db.
                 Assume donor_name is in the form "Firstname Lastname"
    """
    name_list = donor_name.split()
    for donor_id in donor_db:
        donor_data = donor_db[donor_id]
        if (donor_data["first_name"].lower() == name_list[0].lower()
                and donor_data["last_name"].lower() == name_list[1].lower()):
            return donor_id
    return False


def add_donation(donor):
    """ Prompt the user for a donation amount and add the donation to the
    matching donor in the donor db. Return the donation amount.

    Keyword arguments:
    donor - item in the donor_db.
    """
    donation_amount = get_donation_amount_from_user()

    donor["donations"].append(donation_amount)

    return float(donation_amount)


def get_donation_amount_from_user():
    """ Prompt user for a donation amount, check to see that it is a number,
    and return the amount. If it is not a number, inform the user and prompt
    again.
    """
    while True:
        donation_amount = input(donation_amount_prompt)
        try:
            float(donation_amount)
        except ValueError:
            print("Donation amount should be a plain number and not formatted "
                  "as currency.")
        else:
            return float(donation_amount)


def add_donor(donor_name):
    """ Add a donor to the donor db with empty donation amounts

    Keyword arguments:
    donor_name - string representing the donor name to add to the donor db.
    """
    names = donor_name.split()
    donor_db[donor_name] = {"first_name": names[0], "last_name": names[1],
                            "donations": []}
    return donor_db[donor_name]


def thank_you_message(donor_name, donation_amount):
    """ Create a thank you letter and return as a string.

    Keyword arguments:
    donor_name = name of the donor
    donation_amount = donation amount as a float
    """
    message_line1 = "\nDear {},\n".format(donor_name)
    # Note: I tried to split the following so the line wouldn't be too long
    # using string continuation like so:
    #   message_rest = "     Thank you very much for your generous donation of "
    #   "${:.2f}.\n     WINNING!\n".format(float(donation_amount))
    # but the output was different. I don't understand.
    message_rest = "     Thank you very much for your generous donation of ${:.2f}.\n     WINNING!\n".format(float(donation_amount))
    return message_line1 + message_rest


def get_donor(donor_name):
    """ Return a donor from the donor_db dict if one exists.

    Keyword arguments:
    donor_name - String with a name, assumed to be of the form
    "first_name last_name"
    """
    donor_id = is_existing_donor(donor_name)
    if donor_id:
        return donor_db[donor_id]
    else:
        return None


def create_report():
    """ Print a list of your donors, sorted by total historical donation amount.
    Include Donor Name, total donated, number of donations, and average
    donation amount as values in each row. The end result should be tabular
    (values in each column should align with those above and below) and look
    something like this:

    Donor Name                | Total Given | Num Gifts | Average Gift
    ------------------------------------------------------------------
    William Gates, III         $  653784.49           2  $   326892.24
    Mark Zuckerberg            $   16396.10           3  $     5465.37
    Jeff Bezos                 $     877.33           1  $      877.33
    Paul Allen                 $     708.42           3  $      236.14
    """
    try:
        report_rows = create_report_rows()
    except AssertionError:
        print("Report creation failed")
        return

    # print header
    print("{:<26}| {:<11}| {:<10}| {:<12}".format("Donor Name", "Total Given",
                                                  "Num Gifts", "Average Gift"))
    # print header line
    print("-" * 65, end="")
    print("")  # get a new line
    # print rows
    print("\n".join(report_rows))
    print("")


def create_report_rows():
    """ Create the rows (as described in create_report()) with the data from
    the donor db, sorted by total donation amount (computed by the sort_key
    function). Return a list with each row as a list item.
    """
    sorted_donor_keys = sorted(donor_db, key=sort_key, reverse=True)
    report_rows = [create_single_report_row(donor_db[donor_key])
                   for donor_key in sorted_donor_keys]
    return report_rows


def create_single_report_row(donor):
    """ Create each body row (as described in create_report()).

    Keyword arguments:
    donor - item from the donor db.
    """
    total_donation = sum(donor["donations"])
    num_donations = len(donor["donations"])
    average_donation = 0.0
    if num_donations > 0:
        average_donation = total_donation / num_donations
    whole_name = "{} {}".format(donor["first_name"].title(),
                                donor["last_name"].title())
    return "{:<26} ${:>11.2f} {:>10d}  ${:>12.2f}".format(whole_name,
                                                          total_donation,
                                                          num_donations,
                                                          average_donation)


def sort_key(donor_key):
    return sum(donor_db[donor_key]["donations"])


def quit_app():
    return "quit"


def main():
    """ Prompt the user to select an option (send a thank you, create a
    report, or quit), which invokes the appropriate function. Except for the
    "quit" response, the others will return to this prompt after finishing.
    """
    switch_main_dict = {"1": send_thank_you, "2": create_report,
                        "3": send_letters, "4": quit_app}

    while True:
        response = input(main_prompt)
        response_result = None
        try:
            response_result = switch_main_dict.get(response)()
        except TypeError:
            print("Please type '1', '2', '3', or '4' to select one of the "
                  "available options.")
        if response_result == "quit":
            break


if __name__ == "__main__":
    main()
