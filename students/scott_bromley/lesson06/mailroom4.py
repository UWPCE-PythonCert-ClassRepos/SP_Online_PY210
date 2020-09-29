#!/usr/bin/env python3
import datetime
import statistics
import tempfile

# prompt user to select from mailroom menu: send a thank you, create a report, or quit
# send a thank you: allows user to select a name, adds donor if not in donor list, otherwise ask for donation
# and thanks donor
# create a report summarizes the donors and their donations in a table
# quit ends the program

# donors exists in global namespace
donors = {
      "Jerry Seinfeld": [
          324.33
      ],
      "John Stewart": [
          5000000.00
      ],
      "Larry David": [
          1800.18,
          36036.36
      ],
      "Gene Wilder": [
          7272.72,
          1818.18,
          545454.54
      ],
      "Jerry Lewis": [
          0.00
      ],
      "Gilda Radner": [
          324.32
      ],
      "Rodney Dangerfield": [
          363363.63,
          18181.81,
          545454.54,
          727.72,
          9090.90,
          108.18,
          126.12,
          7272.72,
          54.54,
          18.00,
          0.18
      ]
}
now = datetime.datetime.now()


def main():
    main_prompt = ("\nPlease enter an option from the following menu\n"
                   "1 - Send a Thank You to a single donor\n"
                   "2 - Create a Report\n"
                   "3 - Send letters to all donors\n"
                   "4 - Quit\n>> ")
    dispatch = {"1": send_thank_you, "2": create_report, "3": send_thank_you_all_donors, "4": quit_mailroom}
    menu_selection(main_prompt, **dispatch)


def menu_selection(prompt, **dispatch_dict):
    """
    prompts user for input and calls function object in dispatch_dict
    :param prompt: user input prompt
    :param dispatch_dict: dict of dispatch functions
    :return:
    """
    while True:
        try:
            response = get_user_input(f"{prompt}")
        except (TypeError, ValueError) as menu_err:
            print(f"Invalid option {response}\n")
            raise menu_err
        except (KeyboardInterrupt, EOFError):
            return None
        if dispatch_dict[response]() == 4:
            break


def quit_mailroom():
    """
    quit the mailroom
    :return: 4 (quit option)
    """
    return 4


def send_thank_you():
    """
    prompt user for a donor name; if name exists, prompts for donation, otherwise add name to donors
    'list' displays a list of donors
    print thank you to donor
    :return: None
    """
    donor_name = get_user_input("Please enter the name of a donor: ")
    if donor_name == 'list':
        print(f"List of donors: {', '.join(list_donors(**donors))}")
    else:
        while True:
            try:
                donation = float(get_user_input("Please enter the donation amount: ").strip('$'))
                if bool(donation) is True:
                    break
                else:
                    print(f"Invalid donation, please enter a valid donation.\n")
            except ValueError as donation_err:
                raise donation_err
                continue
        donor_info = (donor_name, donation)
        update_donor(donor_info)
        print(f"{format_thank_you(donor_info)}")


def list_donors(**donors):
    """
    :param donors: dict of key:donor and value:list of donations
    :return: list of donors
    """
    if not donors:
        raise TypeError("donors cannot be empty")
    else:
        try:
            return list(donors.keys())
        except KeyError as key_error:
            print(f"{key_error}")


def update_donor(donor_info=None):
    """
    add donor if donor does not exist, otherwise update donor's list of donations
    :param donor_info: tuple of donor name and donation amount
    :return:
    """
    if not donor_info[0]:
        raise TypeError("donor_name cannot be empty")
    else:
        if donor_info[0] in donors:
            try:
                donors.setdefault(donor_info[0], []).append(donor_info[1])
            except IndexError as donor_info_error:
                print(f"{donor_info_error}")
        else:
            donors.setdefault(donor_info[0], []).append(donor_info[1])
            print(f"Sorry, the name you entered is not in our donor list.  Adding donor to list...")


def send_thank_you_all_donors():
    """
    generate a thank you letter for all donors, write each letter to disk as .txt in tempdir
    :return: None
    """
    try:
        with tempfile.TemporaryDirectory(suffix='mailroom2', prefix='tys_all_donors', dir='.') as tempdir:
            for donor in donors:
                donor_info = (donor, format(donors.get(donor)[-1], '.2f'))
                with open(f"{(donor_info[0]).replace(' ','_')}_{str(now.date()).replace('-','_')}.txt", 'w') as f:
                    f.write(format_thank_you(donor_info))
    except (IOError,  PermissionError, NotADirectoryError, FileExistsError, FileNotFoundError) as report_err:
        print(f"{report_err}")
        raise report_err


def format_thank_you(donor_info=None):
    """
    create thank you letter
    :param donor_info: tuple of donor name and donation amount
    :return:
    """
    if not donor_info[0]:
        raise ValueError("donor name and donation cannot be empty")
    elif not donor_info[1]:
        raise ValueError("donation amount cannot be empty")
    else:
        thank_you = (
            f"\n\n{now.date()}\n\n"
            f""
            f"Dear {donor_info[0]},\n\n"
            f""
            f"On behalf of all of us at the ADL office we'd like to recognize and thank you for your generous\n"
            f"donation of ${donor_info[1]}.  "
            f"These funds will be used to further our mission in fighting hate\n"
            f"through leadership programs and education.  \n\n"
            f"We look forward to seeing you at this year's banquet.\n"
            f"\n"
            f"Sincerely, "
            f"\n"
            f"ADL")
    return str(thank_you)


def display_report(donor_summary=None):
    """
    prints formatted donor report
    :param donor_summary:
    :return:
    """
    print(f"Donor Name{'':<20} | Total Given{'':>0} | Num Gifts{'':>0} | Average Gift{'':>0}")
    print(f"-" * 72)
    for name, total, num_gift, avg_gift in donor_summary:
        print(f"{name:<32}${total:>11.2f}{num_gift:>12}  ${avg_gift:>13.2f}")


def get_report(donors=None):
    """
    data logic function for reports
    :param donors:
    :return: donor summary list
    """
    donor_summary = []
    if not donors:
        raise ValueError("donors list cannot be empty")
    else:
        for donor in donors:
            try:
                donor_summary.append([donor, sum(donors.get(donor)), len(donors.get(donor)),
                                     statistics.mean(donors.get(donor))])
            except (KeyError, IndexError) as donor_summary_err:
                raise donor_summary_err
    donor_summary.sort(key=lambda x: float(x[1]), reverse=True)
    return donor_summary


def create_report():
    """
    dispatch function for creating and displaying donor report
    :return:
    """
    display_report(get_report(donors))


def get_user_input(prompt):
    """
    :param prompt: prompt for user to respond to
    :return: response to question/prompt
    """
    return input(prompt).strip()


if __name__ == "__main__":
    print("Running", __file__)
    main()
else:
    print("Running as imported module", __file__)