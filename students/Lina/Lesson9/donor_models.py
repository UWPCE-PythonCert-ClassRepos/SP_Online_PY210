#!/usr/bin/env python3
#------------------------------------------------------
# Lesson 9 - Assignment 8: Mailroom - Object Oriented
#
#            donor_models.py
#               class Donor
#               class DonorCollection
#------------------------------------------------------

from datetime import date
from operator import itemgetter

# Donor class contains information of a single donor
class Donor:
    def __init__(self, donor_name, donor_details=None):
        self.full_name = donor_name
        if donor_details == None:
            details = self.lookup_donor(donor_name)
            if details:
                self.details = details
            else:
                self.details = {"gift_amounts" : [0]}
        else:
            self.details = donor_details

    @classmethod
    def lookup_donor(cls, name):
        return DonorCollection().lookup_donor(name)

    @property
    def first_name(self):
        return self.full_name.split()[0]

    @property
    def last_name(self):
        return self.full_name.split()[1]

    @property
    def total_gift_amount(self):
        return round(sum(self.details["gift_amounts"]), 2)

    @property
    def total_gift_count(self):
        return len([amount for amount in self.details["gift_amounts"] if amount > 0])

    @property
    def avg_gift_amount(self):
        if self.total_gift_count > 0:
            avg = round(self.total_gift_amount / self.total_gift_count, 2)
        else:
            avg = 0
        return avg

    def thank_you_letter(self, first_name, gift_amount):
        #Compose a letter to thank the donor for the donation that they just made.
        #returns letter in a string
        letter_layout, sender_template = self.letter_template(first_name, gift_amount)

        letter = "\n".join(("Dear {donor_first_name},",
                 "{new_paragraph_indent}Thank you for your generous gift of ${donation_amount:.2f} to support the work of ChangeALife. Your",
                 "donation will remain in your local community and be used by ChangeALife to provide programs",
                 "and services to those in need.",
                 "{new_paragraph_indent}On behalf of those whose lives will be impacted, please accept our sincere gratitude. May ",
                 "you know the deep satisfaction of having made a difference in the lives of others.",
                 "\n\n",
                 "Below is a summary of your gift.",
                 "",
                 "Amount: ${donation_amount:.2f}",
                 "Date: {date:%m-%d-%Y}",
                 sender_template)).format(**letter_layout)
        return letter

    def letter_template(self, first_name, gift_amount):
        #Creates a common format for some letters.
        #Returns letter layout and sender template in a string
        letter_layout = {"donor_first_name" : first_name,
                         "donation_amount" : gift_amount,
                         "sender_name" : "Tiffany Kurnett",
                         "sender_title" : "President & CEO",
                         "sender_alignment" : ' '*25,
                         "new_paragraph_indent" : '\n   ',
                         "date" : date.today()
                        }
        sender_template = "\n".join(("\n\n\n\n{sender_alignment}Sincerely,",
                          "{sender_alignment}{sender_name}",
                          "{sender_alignment}{sender_title}",
                          "\n\n\n"))
        return letter_layout, sender_template

# DonorCollection class contains information about all donors
class DonorCollection:
    #This dictionary database contains the donor names and a history of their donation amounts.
    def __init__(self):
        self.donor_db = self.get_donors_history()

    def donor_list(self):
        #Returns a list with all donors sorted by name.
        return sorted(self.donor_db.keys())

    def lookup_donor(self, name):
        #If donor is found, returns a dictionary with donor details
        #If donor is not found, returns None
        return self.donor_db.get(name)

    def add_donation(self, name, amount):
        #Adds a donation from a donor. If the donor does not exist, it will add to donor_db{} first.
        self.donor_db.setdefault(name, {"gift_amounts":[]})
        self.donor_db[name]["gift_amounts"].append(amount)

    def donors_summary(self):
        #Returns a list with summary of each donor in a tuple, sorted by total donated from
        #highest to lowest.
        # [(name, total donated, donation count, average amount)]
        summary = []
        for name, detail in self.donor_db.items():
            d = Donor(name, detail)
            summary.append((name, d.total_gift_amount, d.total_gift_count, d.avg_gift_amount))
        summary = sorted(summary, key=itemgetter(1), reverse=True)
        return summary

    def donors_summary_report(self):
        #Creates a summary report to list all donors, their total donation test_avg_gift_amount_2
        #amount, number of donations and average amount. It will show in the order of total
        #Returns report in a string
        header = "{:<25s} | {:11s} | {:9s} | {:12s}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
        lines = (header, f"{'-'*len(header):s}")
        summary = self.donors_summary()
        row = "{name:<25s}  ${total_donated:11.2f}  {gift_count:10d}  ${avg_amount:12.2f}".format
        for col in summary:
            line = row(name=col[0], total_donated=col[1], gift_count=col[2], avg_amount=col[3]),
            lines += tuple(line)
        return "\n".join(lines)

    def letters_to_all_donors(self):
        #Compose a letter to all donors with their total contribution included.
        #Returns all letters in a list of tuples [(letter, fullname), (letter, fullname), ...]
        letters = []
        for name, detail in self.donor_db.items():
            d = Donor(name, detail)
            letter_layout, sender_template = d.letter_template(d.first_name, d.total_gift_amount)
            letter = "\n".join(("Dear {donor_first_name},",
                     "{new_paragraph_indent}Whether you are a new donor or have suppported ChangeALife for many years, your compassionate",
                     "generosity gives us the vital resource to provide programs and services to those in need. I hope",
                     "you will continue to support our work at ChangeALife. Your support means the world to the families",
                     "and people we serve.",
                     "{new_paragraph_indent}On behalf of those whose lives will be impacted and from all of us at ChangeALife, THANK YOU!",
                     "\n\n"
                     "Below is a summary of your gift.",
                     "",
                     "Amount: ${donation_amount:.2f}",
                     sender_template)).format(**letter_layout), name,
            letters.append(tuple(letter))
        return letters

    def get_donors_history(self):
        #Returns donor history in a dictionary
        donor_data = {"Jennifer Lee" : {"gift_amounts" : [1350.0, 120.17]},
                      "Linda Anderson" : {"gift_amounts": [877.33]},
                      "Melissa Carey" : {"gift_amounts" : [663.23, 43.87, 1.32]},
                      "Dmitriy Mikutin" : {"gift_amounts" : [1663.23, 4300.87, 10432.0]},
                      "John Palmer" : {"gift_amounts" : [3312.00, 5500.00]},
                      "Henry Ma" : {"gift_amounts" : [250.75, 120.00, 55.50, 100.50]}
                     }
        return donor_data
