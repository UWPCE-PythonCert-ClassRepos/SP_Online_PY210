
'''
Donor models for the object-oriented mailroom assignment.
'''

from operator import itemgetter


class Donor():
    '''
    Class for individual donors. Includes name, donations, and other information
    pertaining to a single donor.
    '''

    def __init__(self, name, donations=None):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("name must be entered as a string")
        if donations is None:
            self.donations = []
        else:
            if isinstance(donations, list) is False:
                raise TypeError("donations must be entered as a list")
            for i in donations:
                if isinstance(i, (int, float)) is False:
                    raise ValueError("donation must be entered as a number")
            self.donations = donations

    def add_donation(self, donation):
        '''Add a donation to the donor's list of donations.'''
        if isinstance(donation, (int, float)) is False:
            raise ValueError("donation must be entered as a number")
        self.donations.append(float(donation))

    @property
    def total_donations(self):
        '''Return total of donor's donations.'''
        return sum(self.donations)

    def write_indiv_letter(self):
        '''Generate a thank-you letter to the donor for their latest donation.'''
        return f"Dear {self.name}, thank you for your generous donation of " \
        f"${self.donations[-1]:.2f}."


class DonorCollection():
    '''
    Class for collection of donors. Includes all operations that require
    knowledge of multiple donors. The client code accesses individual
    donors through this collection.
    '''

    def __init__(self):
        self.collection = []

    def add_donor(self, name, donations=None):
        '''Add a new donor to the collection.'''
        self.collection.append(Donor(name, donations))

    def get_donor(self, name):
        '''Return the donor if present, otherwise return False.'''
        for a in self.collection:
            if a.name == name:
                return a
        else:
            return False

    def display_donors(self):
        '''Display donors and donations as a string.'''
        donorlist = ""
        for a in self.collection:
            donorlist += f"{a.name}: {a.donations}"
            donorlist += "\n"
        return donorlist

    def generate_report(self):
        '''Generates a formatted report of donors, total given, num gifts, and average gift.'''
        final_report = ""
        titles = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
        formatted_titles = f"{titles[0]:15} {titles[1]:>20} {titles[2]:>10} {titles[3]:>20}\n"
        final_report += formatted_titles
        reportlines = []
        for a in self.collection:
            try:
                reportlines.append([a.name, a.total_donations,
                len(a.donations), a.total_donations/len(a.donations)])
            except ZeroDivisionError:
                reportlines.append([a.name, 0, 0, 0])
        sortedlines = sorted(reportlines, key=itemgetter(1), reverse = True)
        for r in sortedlines:
          final_report += f"{r[0]:15} {r[1]:>20.2f} {r[2]:>10} {r[3]:>20.2f}\n"
        return final_report

    def batch_letters(self):
        '''Generate a thank-you letter for each donor and save to current directory.'''
        for a in self.collection:
            filetext = f"Dear {a.name},\nThank you for your donation of ${a.donations[-1]:.2f}." \
            f" Your total donations to date are ${a.total_donations:.2f}. " \
            "We appreciate your generosity to our organization.\nThanks, the Management."
            with open(f"{a.name}.txt", "w") as f:
                f.write(filetext)