#!/usr/bin/env python
# I will always use donor's full name to be consistant.  I understand this has shortcomings 
# in real practice


class Donor():

    def __init__(self, name, donations=[]):
        """Initialize Donor object."""
        self.name = name

        if type(donations) is list:
            self.donations = donations
        else:
            raise TypeError('Please enter donations as a list.')

    def add_donation(self, donation): # Add a donation for the Donor

        self.donations.append(donation)
    
    def text_thank_you(self):
        """Return thank_you letter for Donor."""

        return f'\nDear {self.name}:\n\nOn behalf of your Local Charity, I would like to thank you for your generous donation. We appreciate your support not only for us but for our cause.\n\nWe wish you all the best,\n\nLocal Charity Persident\n'

        #return email

class DonorCollection():
    """Class to collect data on all donors."""

    def __init__(self, **database):
        """Initialize DonorCollection object"""
        
        self._database = dict(database)

    def add_donor(self, donor, donation): # Add donor information for report
        
        self._database[donor] = Donor(donor, [donation])
        print("Database updated")

        return self._database

    def display_report(self): # Format and print report

        def sort_key(donor): # Define sort key
            return int(sum(donor.donations))

        member_row = '{:<24}{:^5} ${:>14,}{:^5} {:^5}{:^5} ${:>14,.2f}'

        sorted_data = sorted(self._database.values(), key=sort_key, reverse=True)
        
        report_rows = []
        
        # Print each row to format table
        for per in sorted_data:
            report_rows.append(member_row.format(per.name, ' ', 
                int(sum(per.donations)), ' ', 
                round(len(per.donations),2), ' ', 
                round(sum(per.donations) / len(per.donations),2)))

        # Format table with header
        print('Generating report of donors....')
        # Header
        h_1 = (f"-" * 80)
        h_2 = (f" Donor Name"+" " * 19 + "| Total Donated | Num Donations | Average Donation")
        h_3 = (f"-" * 80)
        #print(""+"-" * 80 + "\n Donor Name"+" " * 19 + "| Total Donated | Num Donations | Average Donation\n"+"-" * 80)

        report_rows.insert(0, h_3 )
        report_rows.insert(0, h_2)
        report_rows.insert(0, h_1)

        for row in report_rows:
            print(row)