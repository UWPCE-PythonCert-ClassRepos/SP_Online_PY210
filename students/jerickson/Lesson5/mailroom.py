"""Automate the mailroom workflow."""

# pylint: disable=line-too-long

donation_data_header = ["Name", "Total Given", "Num Gifts", "Average Gift"]
donation_data = {
    "Usama Black": {"total given": 22002, "num gifts": 3},
    "Kezia Hassan": {"total given": 3023.23, "num gifts": 3},
    "Lyla Moody": {"total given": 580, "num gifts": 1},
    "King Arthur": {"total given": 400, "num gifts": 1},
    "Twin Arthur": {"total given": 400, "num gifts": 2},
    "Pamela Guerra": {"total given": 32, "num gifts": 2},
    "Malachy Krause": {"total given": 4242, "num gifts": 1},
}


def sort_donation_data():
    """Return list of sorted donors by Total-Given"""

    donation_data_sortable = [
        [record["total given"], name] for name, record in donation_data.items()
    ]
    sorted_donors = [name for _, name in sorted(donation_data_sortable, reverse=True)]

    return sorted_donors


def report():
    """Print a report of the donation history."""
    # Format report lines
    sorted_donors = sort_donation_data()
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
    for name in sorted_donors:
        print(report_break)
        total_given = donation_data[name]["total given"]
        num_gifts = donation_data[name]["num gifts"]
        donor_average = float(total_given / num_gifts)
        donor_string = f"|{name:^16}| ${total_given:>12.2f}|{num_gifts:^13d}| ${donor_average:>13.2f}|"
        print(donor_string)
    print(report_end)


def new_donation(donor_name, amount):
    """Adds a new donation to the donation record"""
    donor_record = donation_data.setdefault(
        donor_name, {"total given": 0, "num gifts": 0}
    )
    donor_record["total given"] += amount
    donor_record["num gifts"] += 1
    compose_new_donation_email(donor_name, donor_record, amount)


def donor_list():
    """Return a string of comma seperated donor names"""
    all_names = sort_donation_data()
    format_string = " {}," * (len(all_names))
    return format_string.format(*all_names)[:-1]  # Slice removes extra comma at end


def compose_new_donation_email(donor_name, donor_record, amount):
    """Print a new-donation thank-you email using the donor's historical information"""
    time_s = "times" if donor_record["num gifts"] > 1 else "time"
    email = f"Thank you {donor_name} for your donation of ${amount:.2f}! You have donated {donor_record['num gifts']} {time_s} for a total of ${donor_record['total given']:.2f}."
    print(email)


def compose_all_donors_emails():
    """Write to disk a thank-you email using the donor's historical information"""
    file_id = 0
    for donor_name, donor_record in donation_data.items():
        time_s = (
            f"{donor_record['num gifts']:d} donations"
            if donor_record["num gifts"] > 1
            else "donation"
        )  # Grammer correction of donation vs # donations
        email = f"Thank you {donor_name},\n\nYour {time_s} totaling ${donor_record['total given']:.2f} will help us.\n\n{'':>40}Best Regards,\n{'':>40}Jacob Erickson"
        file_name = f"Donor{file_id:03d}_{donor_name}_gitnore.txt"
        with open(file_name, "w") as file:
            file.write(email)
        file_id += 1


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


def quit_interface():
    """Return the string "quit" to exit a menu-level"""
    return "quit"


def menu_selection(prompt, dispatch_dict):
    """
    Creates a CLI for users to interact with.

    Manages the flow of the CLI using the parameters. The
    dispatch dictionary controls the function that will be
    called as the result of the user's input. Unrecognized
    commands print an error message to the user and prompts
    them to try again.

    A function that returns 'quit' string will cause the
    loop to break.

    Parameters
    ----------
    prompt : str
        The prompt the user will see in the terminal
    dispatch_dict : dict
        The dictionary where values are callable functions

    Returns
    -------
    None
    """
    while True:
        command = input(prompt).lower()
        try:
            if (
                dispatch_dict[command]() == "quit"
            ):  # Runs command and gets checks if quit is returned
                break
        except KeyError:
            print(f"Unrecognized Command: {command}")


def main():
    """Main function to run user-interace of the mailroom program."""
    command_dispatch = {
        "send a thank you": thank_you,
        "create a report": report,
        "send letters to everyone": compose_all_donors_emails,
        "quit": quit_interface,
    }
    prompt = "Choose: “Send a Thank You”, “Create a Report” “Send Letters to Everyone” or “Quit” ->: "
    menu_selection(prompt, command_dispatch)


if __name__ == "__main__":
    print("\nBack to the grind in the mailroom.", end="\n\n")

    are_you_mocking_me = int(input('Are you mocking me?? "0": no, "1": yes->: '))

    if (
        are_you_mocking_me
    ):  # Mocks input() to allow for automated list of user-inputs to be run

        def response_generator(seq):
            # TODO comprehension
            for item in seq:
                yield item

        def input(prompt):  # pylint: disable=redefined-builtin
            """Mocks input function for automated receipe running"""
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
            "King Arthur",
            "400.2",
            "create a report",
            "send letters to everyone",
            "quit",
        ]
        mocked_resp_gen = response_generator(mocked_responses)

    main()
    print("Fin")
