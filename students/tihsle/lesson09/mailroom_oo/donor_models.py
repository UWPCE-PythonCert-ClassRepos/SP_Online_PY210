#!/usr/bin/env python3
#Donor and DonorCollection classes
import statistics

class Donor(object):
    """
    Class responsible for donor data encapsulation
    """
    def __init__(self, name, donation):
        self.name = name
        if type(donation) is list:
            self.gifts = donation
        else:
            self.gifts = [donation]

    def total_gifts(self):
        return sum(self.gifts)

    def num_gifts(self):
        return len(self.gifts)

    def avg_gift(self):
        return statistics.mean(self.gifts)

    def add_gift(self, donation):
        self.gifts.append(donation)

    def send_thank_you(self):
        thank_you_text = "\n".join(("Dear {},\n".format(self.name),
          "\nThank you for donating!  Your generous donation will be used to fulfill our mission.\n",
          "We look forward to updating you on how your funds are used throughout the year.\n",
          "\nBest Regards,\n",
          "\nCharity1\n"))
        return thank_you_text.format(self.name)

class DonorCollection(object):
    """
    Class responsible for donor collection data encapsulation
    """
    #starting dictionary
    donors_dict = {"William Gates, III": [65000.00,10.00],
        "Mark Zuckerberg": [1442.25, 4000.00, 5000.00],
        "Jeff Bezos": [877.33],
        "Paul Allen": [400.00, 200.0000, 10.00],
        "Joe Smithe": [1000.00, 2000.00]
        }

    def __init__(self, donors = donors_dict):
        donor_list = []

        #build the donor_list
        for key, value in donors.items():
            donor_list.append(Donor(key, value))

        self.donor_list = donor_list

    def sort_key():
        return donor.total_gifts()

    def get_report_line(self, p):
        report_line = "{:20} ${:>18.2f} {:>21} ${:>18.2f}".format(p[0],p[1],p[2],p[3])
        return report_line

    def report(self):
        head_form = "{:^20}|" * 4
        grid_form = "-" * 21 * 4

        #build report content line by line
        report_content = "\n"
        report_content += head_form.format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
        report_content += "\n"
        report_content += grid_form
        report_content += "\n"

        patrons_list = [(patron.name, patron.total_gifts(), patron.num_gifts(), patron.avg_gift()) for patron in self.donor_list]
        sorted_patrons_list = sorted(patrons_list, key=lambda p: p[1], reverse = True)
        for patron in sorted_patrons_list:
            report_content += self.get_report_line(patron)
            report_content += "\n"
        return report_content

    def list_donors(self):
        patrons_text = ''
        for patron in self.donor_list:
            patrons_text += '{}\n'.format(patron.name)
        return patrons_text

    def new_donor_check(self, donor):
        """Check if donor is new"""
        for patron in self.donor_list:
            if patron.name == donor.name:
                return False
        return True

    def add_donation(self, donor):
        """Add donation"""
        for patron in self.donor_list:
            if patron.name == donor.name:
                patron.gifts.append(donor.gifts[0])
                break

    def add_donor(self, name, donation):
        """Add a new donor or a new donation"""
        new_gift = Donor(name, donation)
        if self.new_donor_check(new_gift):
            self.donor_list.append(new_gift)
        else:
            self.add_donation(new_gift)
