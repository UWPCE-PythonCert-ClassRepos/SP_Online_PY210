#!/usr/bin/env python3
#Donor and donor collections classes
import statistics

class Donor(object):
    """
    Any functionality with only one donor
    """
    def __init__(self, name, donation):
        self.name = name
        if type(donation) is list:
            self.donations = donation
        else:
            self.donations = [donation]

    def recent_donation(self):
        return self.donations[-1]
    
    def count_donation(self):
        return len(self.donations)
        
    def avg_donations(self):
        return statistics.mean(self.donations)
        
    def total_donations(self):
        return sum(self.donations)

    def add_donation(self, donation):
        self.donations.append(donation)


    def send_thank_you(self):
        thank_you_email = "\n".join(("Dear {donor},",
                                     "",
                                     "Thanks you for your generous donation of {donation:.2f}.",
                                     "",
                                     "Sincerly,",
                                     "The Weyland-Yutani Corporation"
                                     ))
        return thank_you_email.format(donor = self.name, donation = self.recent_donation())

class DonorCollection(object):
    """
    Any functionality with only one or more donors
    """
    #default values
    donor_db = {
        "William Gates, III": [653772.32, 12.17],
        "Jeff Bezos": [877.33],
        "Paul Allen": [663.23, 43.87, 1.32],
        "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
        }

    def __init__(self, donors = donor_db):
        donor_list = []

        for key, value in donors.items():
            donor_list.append(Donor(key, value))

        self.donor_list = donor_list

    def list_donors(self):
        donor_string = ''
        for donors in self.donor_list:
            donor_string += '{}\n'.format(donors.name)
        return donor_string

    def donor_report(self): 
        report_dict = {"Header": "{0: <28}|{1: ^13}|{2: ^11}|{3: ^15}",
                       "Filler": "-" * 68,
                       "Rows": "{0: <28} ${1: >11.2f}   {2: >9}  ${3: >12.2f}",
                       }
        report_string = "\n"
        report_string += report_dict["Header"].format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
        report_string += "\n"
        report_string += report_dict["Filler"]
        report_string += "\n"
        report_list = [(donors.name, donors.total_donations(), donors.count_donation(), donors.avg_donations()) for donors in self.donor_list]
        for donors in sorted(report_list, key=lambda t: t[1], reverse = True):
            report_string += report_dict["Rows"].format(donors[0], donors[1], donors[2], donors[3])
            report_string += "\n" 
        return report_string
    
    def donor_check(self, donor):
        """Check if donor exists in the DB"""
        for donors in self.donor_list:
            if donors.name == donor.name:
                return False
        return True

    def add_donation(self, donor):
        """Add a donation to the existing amount"""
        for donors in self.donor_list:
            if donors.name == donor.name:
                donors.donations.append(donor.donations[0])
                return
                break

    def add_donor(self, name, donation):
        """Add a donor or add their donation then send a thanks"""
        entry = Donor(name, [donation])
        if self.donor_check(entry):
            self.donor_list.append(entry)
        else:
            self.add_donation(entry)
            entry
            
    def sort_key(self):
        return self.donor.total_donations()
    
    def __eq__(self, other):
         return sum(self.donation) < sum(other.donation)
     
    def __lt__(self, other):
         return sum(self.donation) < sum(other.donation)
    
