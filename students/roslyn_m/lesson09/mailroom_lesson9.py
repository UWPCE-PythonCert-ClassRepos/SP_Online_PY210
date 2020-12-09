#!/usr/bin/env python3
# Title: Mailroom Part 5 (Lesson 9)
# Dev: Roslyn Melookaran
# Date: 11/26/20
# Change Log: (Who, When, What)
# R. Melookaran, 11/26/20, created script)
# --------------------------------------------------------------
# ------------------- Data Classes --------------------- #


class Donor():

    def __init__(self,first, last, donations):
        self.first = first
        self.last = last
        self.donations = donations

    @property
    def average(self):
        """ Calculates average donation amount
                        :return: average donation
                        """
        return sum(self.donations)/len(self.donations)

    @property
    def qty(self):
        """ Adds amount of donations.
                        :return: qty of donations
                        """
        return len(self.donations)

    @property
    def total(self):
        """ totals all donations
                        :return: sum donations
                        """
        return sum(self.donations)

    def __str__(self):
        """ user friendly string describing object
                        :return: (string)
                        """
        return "Name: {self.first} {self.last}, Donations: {self.donations}".format(self=self)

# -------------------- IO Classes ---------------------- #


class IO():

    @staticmethod
    def options_menu():
        """ Show menu of options to user.
                :return: nothing
                """
        print(
            "\nMenu of actions:" + '\n \t1) Send a Thank You \n \t2) Create a report \n \t3) Create Thank You files for all donors \n \t4) Quit\n')

    @staticmethod
    def option_input():
        """ Gather input from user on what action they want.
                    :return: user_selection (string)
                    """
        while True:
            user_selection = input('Please select option 1-3: ')
            try:
                user_selection = int(user_selection)
                break
            except ValueError:
                print("You must enter a number from 1-4")
        return user_selection

    @staticmethod
    def person_input():
        """ Gather input from user on donor name.
                :return: user_input (string)
                """
        user_input = input(
            'Please type the FULL NAME of the donor who you would like to write a thank you note to. If you would like to see a complete donor report, type "report": ')
        user_input = user_input.title()
        return user_input

    @staticmethod
    def donation_input():
        """ Gather input from user on donation amount.
            :return: donation_amt (float)
            """
        try:
            donation_amt = float(input("Please enter the donation amount: "))
        except ValueError:
            print("Your input was not valid!")
            donation_amt = float(input("Please enter the donation amount: "))
        if donation_amt < 0:
            donation_amt = float(input("Please enter a donation amount greater than 0: "))
        return donation_amt

    @staticmethod
    def print_to_user(string):
        """ print data to user
            return: nothing
                """
        print(string)


# ---------------- Processing Classes ------------------ #

class Processing():

    @staticmethod
    def create_report(donor_all):
        """ Create a report of donors to show user.
                    :param: donor_all (list of donor objects)
                    :return: nothing
                    """
        sorted_donors = sorted(
            ([donor.total, donor.first + " " + donor.last, donor.qty, donor.average] for donor in donor_all),
            reverse=True)
        title = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
        string = f'{title[0]:20}|{title[1]:^12}|{title[2]:^10}|{title[3]:^14}|'
        IO.print_to_user(string)
        string2 = "-" * 60
        IO.print_to_user(string2)
        for person in sorted_donors:
            string3 = f'{person[1]:20}  ${person[0]:^12}{person[2]:9}      ${person[3]:^12}'
            IO.print_to_user(string3)
        string4 = "\n"
        IO.print_to_user(string4)
        return sorted_donors

    @staticmethod
    def thank_you_note(donor_all):
        """ User will be prompted for a Full Name.
                -If the user type list show them a list of the donor names and re-prompt.
                -If the user types a name not in the list, it will be added to data structure and used
                -If the user types a name in the list, it is used.
            -Once a name has been selected, user will be prompted for a donation amount to be added to donation history
            -Thank you note will be generated
                      :param: donor_all (list of objects)
                      :return: donor_all (list of objects)
                      """
        donation_new = []
        user_input = IO.person_input()
        existing = False

        while user_input == "Report":
            Processing.create_report(donor_all)
            user_input = IO.person_input()
        donation_amt = IO.donation_input()
        first, last = user_input.split()
        donation_new = [first, last, donation_amt]

        for donor in donor_all:
            if donation_new[0] == donor.first and donation_new[1] == donor.last:
                donor.donations.append(donation_new[2])
                existing = True
        if existing != True:
            donor_new = Donor(first, last, [donation_amt])
            donor_all.append(donor_new)

        string1 = "The following thank you note will be emailed to the donor: "
        IO.print_to_user(string1)
        string2 = '"Dear {}, \n Thank you so much for your gracious donation of ${:.2f}. We are so thankful for your strong support!! \nCheers,\nRoslyn Melookaran"'.format(
                first, donation_amt)
        IO.print_to_user(string2)
        return donor_all

    @staticmethod
    def send_all_thank_you(donor_all):
        """ Function will print a .txt file thank you note for each donor in list
                :param: donor_all (list of objects)
                :return: donor_all
                """
        for donor in donor_all:
            string = "Dear %s, \n\n \t Thank you so much for your support! You have donated a total of $%s, which is so very appreciated. We hope to have your continued support through these times. \n\nThanks, \nRoslyn" % (
                donor.first, donor.total)
            filename = donor.first + "_" + donor.last + ".txt"
            with open(filename, 'w') as f:
                f.write(string)
        string1 = "Thank you note files have been created and saved in current folder!"
        IO.print_to_user(string1)
        return donor_all


# ------------- MAIN -------------------#
donor1 = Donor('William', 'Gates', [100.00, 100.00, 100.00])
donor2 = Donor('Mark', 'Zuckerberg', [20.00, 20.00])
donor3 = Donor('Jeff', 'Bezos', [50.00, 50.00, 50.00, 50.00, 50.00])
donor4 = Donor('Paul', 'Allen', [200.00])
donor_list = [donor1, donor2, donor3, donor4]
user_input = ""

dict = {
    1: Processing.thank_you_note,
    2: Processing.create_report,
    3: Processing.send_all_thank_you
    }

if __name__ == '__main__':
    IO.options_menu()
    user_input = IO.option_input()
    while user_input != 4:
        dict.get(user_input)(donor_list)
        IO.options_menu()
        user_input = IO.option_input()
    exit_input = input('Thanks for using the program. Hit enter to exit.')

