'''
Andrew Garcia
Mailroom Classes
8/22/19
'''


# formats a donor, creating a thank you note
class Donor(object):
    def __init__(self, donor_name, donation):
        self.name = donor_name
        self.donation = donation

    def thank_you_donor(self):
        return """Dear {},
        Thank you for your donation of ${:.2f}. It is greatly appreciated!
            From, Your Favorite Charity.""".format(self.name, self.donation)


# organizes all donor information
class DonorCollection(object):
    def __init__(self):
        self.all_donations = {}

    def add_donor(self, donor):  # adds single donor made from Donor class
        if donor.name in self.all_donations:
            self.all_donations[donor.name] += [donor.donation]
        else:
            self.all_donations[donor.name] = [donor.donation]

    def list_donors(self):  # lists all donor names
        donor_list = []
        for key in self.all_donations:
            donor_list += [key]
        return donor_list

    def sort_donors(self):  # sorts donors based on total donation amount
        sorting_donors = []
        for item in self.all_donations:
            donation_amount = len(self.all_donations[item])
            total_donations = sum(self.all_donations[item])
            average_donation = total_donations / donation_amount
            sorting_donors.append([item, total_donations, donation_amount, average_donation])

        def sort_key(sorting_donors):
            return sorting_donors[1]

        highest_donations = sorted(sorting_donors, key=sort_key)
        highest_donations.reverse()
        return highest_donations





