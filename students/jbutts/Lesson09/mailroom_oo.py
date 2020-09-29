#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tempfile


'''
revised mailroom app using dict switch and dict as a data structure (we used a list 
in the first version.

Added ability to create letters as text files, in a temp directory, in batch.

Added sorting abilities here. I originally missed this in the first mailroom assignment.

'''


class Donors(object):

    def __init__(self, content=None, **kwargs):
        self.content = [content] if content else []
        self.attributes = kwargs
        self.donor_db = {}
        self.populate_data()

    def populate_data(self):
        '''
        Populate dictionary with initial data
        '''


        self.add_contribution("Daenerys Targaryen", [100.00, 1000])
        self.add_contribution("Arya Stark", [65.00, 45.92, 1004, 2008, 7777])
        self.add_contribution("Melisandre", [19.00, 100000, 100000, 100000])
        self.add_contribution("Cersei Lannister", [10.00])
        self.add_contribution("Daenerys Targaryen", [400, 500, 700, 5555])
        self.add_contribution("Bran Stark", [666])
        self.add_contribution("Bran Stark", 777) # We even handle for floats instead

    def get_donors_details(self):
        #  Return a sorted, formatted list of donors names with their contributions, descending
        donors = []
        ordered_donors = sorted(self.donor_db, key=lambda k: sum(self.donor_db[k]), reverse=True)
        for donor in ordered_donors:
            #  Iterate through the dict to match the sorted list.
            for key, value in self.donor_db.items():
                if key == donor:
                    # alphabetical by keys. Write out rows: "Donor", "Total", "Gifts", "Average"
                    row = key, sum(value), len(value), sum(value)/len(value)
                    donors.append("{:<25s}${:<19.2f}{:<10d}${:<13.2f}\n".format(*row))
        return donors

    def show_donors(self):
        '''
        Write a report to screen of donors and information about how they've donated

        Return values in descending order from the sum of their historical contributions
        '''

        # Write header row
        row = "Donor", "Total", "Gifts", "Average"
        print("{:<25s}{:<20s}{:<10s}{:<13s}".format(*row))
        # Write corresponding ===='s
        print(''.join(("=" * 24 + " ",  # donor
                       "=" * 19 + " ",  # total
                       "=" * 9 + " ",   # gifts
                       "=" * 12)))      # average

        print(''.join(self.get_donors_details()))

    def list_donors(self):
            '''
            Write a numbered list for the purpose of selecting a donor

            Use a list comprehension to print the numbered list
            '''
            # List current donors in the dictionary as '#. First Last'
            donor_list = "{:<4} {:<7}\n".format("No.", "Name")
            donor_list += "{} {}\n".format("=" * 4, "=" * 7)

            for i, donor in enumerate(sorted(self.donor_db)):
                donor_list += "{:<4} {:<7}\n".format(i + 1, donor)

            return donor_list

    def add_contribution(self, name, amount):
        '''
        After record_contribution() prompts user for input, add records to dictionary as needed.

        Do extra handling to account for floats and lists for the amounts
        '''

        if self.donor_db.get(name):
            if isinstance(self.donor_db[name], list):
                if isinstance(amount, list):
                    self.donor_db[name].extend(amount)  # when amount is a list
                else:
                    self.donor_db[name].extend([amount])  # in case we get passed a float for amount
        else:
            # otherwise, add a single contribution with a new user
            if isinstance(amount, list):
                self.donor_db[name] = amount
            else:
                self.donor_db[name] = [amount]
        return self.donor_db

    def send_letter_to_all(self):
        #  Write text files containing letter contents for all donors in the database


        for key, value in self.donor_db.items():
            tempfilepath = tempfile.gettempdir() + "/" + str(key.replace(' ', "_")) + ".txt"
            try:
                with open(tempfilepath, "w") as outputfile:
                    outputfile.writelines(Donor.format_email(self, key, value[len(value)-1], sum(self.donor_db[key])))
            except IOError:
                print("IOError: Could not create file:" + tempfilepath)


class Donor(object):

    def __init__(self, content=None, **kwargs):
        self.content = [content] if content else []
        self.attributes = kwargs

    def format_email(self, name, amount, total_contribution):
        '''
        Create a thank you email for a donor.
        '''

        mail_str = ''.join((
            "Dear {},\n\n",
            "Thank you for your recent contribution of ${:.2f}.\n\n",
            "We appreciate your generosity in support of our mission.\n\n",
            "Thank you for your lifetime contributions of ${:.2f}.\n\n"
            "Warmest Regards,\n\n",
            "Charity Staff\n")).format(name, amount, total_contribution)

        return mail_str











