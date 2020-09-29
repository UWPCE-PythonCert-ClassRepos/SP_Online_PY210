#!/usr/bin/env python3
from operator import itemgetter

class Donor(object):
    def __init__(self, donor_name, new_donation=None):
        self.name = donor_name
        if new_donation is None:
            self.donation = []
        else:
            self.donation = list(new_donation)

    def new_donation(self, new_amount):
        update_donation = self.donation.append(new_amount)
        return update_donation

    @property
    def donation_total(self):
        return sum(self.donation)

    @property
    def donation_count(self):
        return len(self.donation)

    @property
    def donation_avg(self):
        return round(float(sum(self.donation) / self.donation_count), 2)

    def thank_you_letter(self, donor_name, gift):
        # Thank you email to donor for their gift
        email = f"Thank you {donor_name} for your generous donation of ${gift:.2f}, your kindness is very appreciated." + "\n"
        return email

class DonorCollection:
    def __init__(self):
        # List of existing donors
        self.donor_list = [Donor("Method Man", [1000, 2000]),
                           Donor("The Rza", [500, 100, 50, 80, 12]),
                           Donor("Ghost Face", [10, 20, 5]),
                           Donor("John Doe", [1]),
                           Donor("Jane Doe", [2, 1000, 3000, 8800])]

    # Check if provided name of donor is in the list
    def check_donor(self, donor_name):
        for donor in self.donor_list:
            if donor.name == donor_name:
                return donor_name
            else:
                return f"{donor_name} not found"

    # Add a donor and their donation if they are not in the list
    def add_donor(self, donor_name, new_donation):
        temp_donor = Donor(donor_name, [new_donation])
        self.donor_list.append(temp_donor)
        return temp_donor

    # If donor is in the list, append the donation amount
    def add_donation(self, donor_name, new_donation):
        for donor in self.donor_list:
            if donor.name == donor_name.title():
                donor.new_donation(new_donation)
        return self.donor_list

    # Generate the current list of donors that is also sorted.
    def list_donors(self):
        all_donors = []
        for donor in self.donor_list:
            all_donors.append([donor.name, donor.donation_total, donor.donation_avg])

        sorted_donors = sorted(all_donors, reverse=False)
        return sorted_donors

    def create_report(self):
        # report headers
        fields = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
        # format headers to have a uniform look
        header = f"{fields[0]:<20} | {fields[1]:<11} | {fields[2]:<3} | {fields[3]}"
        # seperates fields from donors list based on the length of the headers
        line_break = "{}".format('-' * len(header))

        # temp list used in order to sort by donor name
        report_list = []
        for donor in self.donor_list:
            temp_list = f"{donor.name:<20} $ {donor.donation_total:>11.2f} {donor.donation_count:>11} $ {donor.donation_avg:11.2f}"
            report_list.append(temp_list)
        # Sort the list by name
        sorted_donors = sorted(report_list, key=itemgetter(0), reverse=False)
        sorted_donors.insert(0, header)  # Add the header row to the list
        sorted_donors.insert(1, line_break)  # Add the line break after header row
        return sorted_donors

    # create a text file for all donors in the list and output in the same directory where the script is ran
    def all_letters(self):
        for donor in self.donor_list:
            with open(f"thank_you_{donor.name.lower()}.txt", 'w') as fh:
                fh.write(f"Dear {donor.name.title()},\nThank you for your very generous donation of ${donor.donation_total:.2f}. "
                         f"Your help will go a long way in supporting our foundation."
                f"\n\nThank you,\nYour Non-Profit Team\n\n")
