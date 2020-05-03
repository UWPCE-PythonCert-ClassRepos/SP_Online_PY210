#!/usr/bin/env python3


###################################


class MailroomControl():

    def __init__(self, in_charity_name):
        self.charity_name = in_charity_name
        pass

    ######################################

    # Support lib methods

    def process_donor_donation(self, in_all_donors, name, donated_amount):
        donor = in_all_donors.add_donation(name, donated_amount)
        print(f"donor {name} donated {donated_amount}")
        email = donor.send_thankyou_email(self.charity_name, donated_amount)
        return email


    ###################################

    # Mailroom control methods

    def display_donors(self, in_all_donors):
        listed_donors = in_all_donors.display_donors()
        return listed_donors


    def create_donors_report(self, in_all_donors):
        report = in_all_donors.create_report()
        return report


    def receive_donation(self, in_all_donors):
        donor_name = self.ui_menu_specify_donor_name()
        donation_amount = self.ui_menu_specify_donation_amount()
        thankyou_email = self.process_donor_donation(in_all_donors, donor_name, donation_amount)
        return thankyou_email


    def write_letters_to_all_donors(self, in_all_donors):
        all_thankyou_letters = in_all_donors.write_letters()
        return all_thankyou_letters

    ###################################

    # ui Menus

    def ui_menu_main(self):
        msg = ""
        msg += "Please enter option from below:\n"
        msg += " D: Receive donation\n"
        msg += " L: Display list of donors\n"
        msg += " R: Create report\n"
        msg += " W: Write letters to all\n"
        msg += " Q: Quit\n"
        msg += ".....>>"

        entry = input(msg)

        return entry


    def ui_menu_specify_donor_name(self):
        msg = ""
        msg += "Please enter donor name :\n"
        msg += ".....>>"

        entry = input(msg)

        return entry


    def ui_menu_specify_donation_amount(self):
        msg = ""
        msg += "Please enter a donation amount::\n"
        msg += ".....>>"

        donation_amount_entry = int(input(msg))

        return donation_amount_entry

