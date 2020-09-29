"""
Programming In Python - Lesson 9 Assignment 1: Object Oriented Mail Room
Code Poet: Anthony McKeever
Start Date: 09/10/2019
End Date: 09/15/2019
"""

import argparse
import os.path as path

from support import Helpers
from support import FileHelpers

from support import MenuItem
from support import MenuDriven

from donor_models import Donor
from donor_models import Donor_Collection


parser = argparse.ArgumentParser(description="Studio Starchelle's Donor Appreciation System")
parser.add_argument("--donors", metavar="path", help="The donor list to import", type=str,
                    default=FileHelpers.default_resource_file_path("donor_list.csv"))
parser.add_argument("--email", metavar="path", help="The email template to import", type=str,
                    default=FileHelpers.default_resource_file_path("email_template.txt"))


donor_list = None


def main(args):
    """
    The main method of the applicaiton.
    
    :args:  The arguments parsed from argparse
    """
    print("\nStudio Starchelle Donor Appreciation System")

    main_menu = [
        MenuItem("Send a Thank You", "Get email template to thank a donor.", send_thanks),
        MenuItem("Create a Report", "View all donors and their cumulative donations",
                 create_report),
        MenuItem("Send Letters to All", "Generate a letter for every donor.", send_to_all)
    ]
    main_menu = MenuDriven("Main Menu:", main_menu, "What do you want to do?")


    try:
        while True:
            main_menu.run_menu()
    except SystemExit:
        donor_list.save_to_file(args.donors)
        raise


def send_thanks():
    """
    Accept a donation and thank the donor.
    """
    thanks = [MenuItem("List Donors", "Print a list of available donors.",
              print_donors, tabs=3)]
    thanks = MenuDriven("Lets Send Thanks!", thanks,
                        "Who would you like to thank? (Enter '1' to list donors)",
                        show_main=True, invalid=donor_list.handle_donation)
    thanks.run_menu()


def print_donors():
    """
    Prints a list of donor names.
    """
    print(donor_list.get_names)


def create_report():
    """
    Print a report of donors, their total donations, count of donations and average donation.
    """
    headers = ["Name:", "Total Given:", "Number of Gifts:", "Average Gift:"]
    summary = sorted(donor_list, reverse=True)
    summary = [d.to_summary for d in summary]

    print("\n".join(Helpers.get_table(headers, summary)) + "\n")


def send_to_all():
    """
    Export thank you notes for all donors.
    """
    print("\n\nLets thank everybody!")
    print(str("\nThis will prepare a letter to send to everyone has donated to "
              "Studio Starchelle in the past."))
    print(str("All letters will be saved as text (.txt) files in the default directory a "
              "different directory is specified."))

    save_dir = FileHelpers.get_user_output_path()

    if save_dir is None:
        print("\nCancelling send to all.  Returning to main menu...\n")
        return
    
    for donor in donor_list:
        file_path = path.join(save_dir, f"{donor.name}.txt")
        FileHelpers.write_file(file_path, donor.get_email(donor_list.email_template))
    
    print(f"Donor letters successfully saved to: {save_dir}")


if __name__ == "__main__":
    args = parser.parse_args()
    donor_list = Donor_Collection.from_file(args.donors, args.email)

    main(args)
