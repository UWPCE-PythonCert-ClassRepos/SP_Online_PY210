donation_data_header = ["Name", "Total Given", "Num Gifts", "Average Gift"]
donation_data = [
    ["Usama Black", 22002, 3],
    ["Kezia Hassan", 3023.23, 3],
    ["Lyla Moody", 580, 1],
    ["King Arthur", 400, 1],
    ["Pamela Guerra", 32, 2],
    ["Malachy Krause", 4242, 1],
]


def sort_donation_data():
    """Sort the donation_data data-structure by Total-Given"""
    global donation_data
    sorted_data = []
    for donor_record in donation_data[:]:
        if not sorted_data:
            sorted_data.insert(0, donor_record)
        else:
            for index_sorted, sorted_record in enumerate(sorted_data[:]):
                if donor_record[1] >= sorted_record[1]:
                    sorted_data.insert(index_sorted, donor_record)
                    break
            else:
                sorted_data.append(donor_record)
    donation_data = sorted_data


def report():
    """Print a report of the donation history."""
    # Format report lines
    sort_donation_data()
    title = donation_data_header[:]
    report_header = f"|{title[0]:^16}|  {title[1]:^12}|{title[2]:^13}|  {title[3]:^13}|"
    report_break_list = []
    for char in report_header[:]:
        break_char = "+" if char == "|" else "-"
        report_break_list.append(break_char)
    report_break = "".join(report_break_list)
    report_length = len(report_break)
    report_end = "-" * report_length
    report_title = "|{{:^{:d}}}|".format(report_length - 2).format("Donor Report")

    # Print report Title and Header
    print(report_end)
    print(report_title)
    print(report_break)
    print(report_header)

    # Print Donor Records
    for donor in donation_data:
        print(report_break)
        donor_average = float(donor[1] / donor[2])
        donor_string = f"|{donor[0]:^16}| ${donor[1]:>12.2f}|{donor[2]:^13d}| ${donor_average:>13.2f}|"
        print(donor_string)
    print(report_end)


def donor_existance(donor_name):
    """Returns a donor's record if it exists, else None"""
    return_record = None  # TODO Remove this
    for donor_record in donation_data:
        if donor_name.lower() == donor_record[0].lower():
            return_record = donor_record
            break
    else:
        return_record = [donor_name, 0, 0]
        donation_data.append(return_record)  # Create donor if not found
    return return_record


def new_donation(donor_name, amount):
    """Adds a new donation to the donation record"""
    donor_record = donor_existance(donor_name)
    donor_record[1] += amount
    donor_record[2] += 1
    compose_email(donor_record, amount)


def donor_list():
    """Return a string of comma seperated donor names"""
    all_names = []
    for donor_record in donation_data:
        all_names.append(donor_record[0])
    format_string = " {}," * (len(all_names))
    return format_string.format(*all_names)[:-1]  # Slice removes extra comma at end


def compose_email(donor_record, amount):
    """Print a thank-you email using the donor's historical information"""
    time_s = "times" if donor_record[2] > 1 else "time"
    email = f"Thank you {donor_record[0]} for your donation of ${amount:.2f}! You have donated {donor_record[2]} {time_s} for a total of ${donor_record[1]:.2f}."
    print(email)


def thank_you():
    """Add new donation to the record and compose a thank you email for it"""
    donor_name = None
    while not donor_name:
        donor_name = input("Who just made a donation? Full Name please. ->: ")
        if donor_name == "list":
            print("All Donors:" + donor_list())
            donor_name = None
    donor_amount = float(input("How much was the donation? ->: "))
    new_donation(donor_name, donor_amount)


if __name__ == "__main__":
    print("\nBack to the grind in the mailroom.", end="\n\n")
    are_you_mocking_me = int(input('Are you mocking me?? "0": no, "1": yes->: '))

    if are_you_mocking_me:
        """Mocks input() to allow for automated list of user-inputs to be run"""

        def response_generator(seq):
            for item in seq:
                yield item

        def input(prompt):  # Mocks input function
            print(prompt, end="")
            response = mocked_resp_gen.__next__()
            print(response)
            return response

        mocked_responses = [
            "spam",
            "create a report",
            "send a thank you",
            "Bob Barker",
            "1",
            "send a thank you",
            "list",
            "King ArThur",
            "400.2",
            "create a report",
            "quit",
        ]
        mocked_resp_gen = response_generator(mocked_responses)

    quit_flag = False
    while not quit_flag:
        command = input(
            "\nChoose: Say “Send a Thank You”, “Create a Report” or “Quit” ->: "
        )
        command = command.lower()
        if command == "send a thank you":
            thank_you()
        elif command == "create a report":
            report()
        elif command == "quit":
            quit_flag = True
        else:
            print(f"Unrecognized Command: {command}")
    print("Fin")
