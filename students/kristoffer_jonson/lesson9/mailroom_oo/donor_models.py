'''
Donor Class
Class responsible for donor data encapsulation
This class holds all the information about a single donor, and  attributes,
properties, and methods to provide access to the donor-specific information
including donor name, sum of donations, number of donations.
:param donor: Name of donator
:param donation: List of donations
'''

class Donor():
    def __init__(self,donor,donations=[]):
        self.donor = donor
        self.donations = donations

    @property
    def sum_donations(self):
        total_donations = sum(self.donations)
        return total_donations

    @property
    def num_donations(self):
        number_of_donations = len(self.donations)
        return number_of_donations

    def enter_donation(self, donation):
        self.donations.append(donation)


'''
DonorCollection Class
Class responsible for donor collection data encapsulation
This class holds all of the donor objects, as well as methods to add a new
donor, search for a given donor, and list donors. Class holds function to
gnerate eports about multiple donors.
'''
class DonorCollections():
    def __init__(self):
        self.donor_list = []

    def add_donor(self, donor, donation):
        self.donor_list.append(Donor(donor,donation))

    def add_donation(self,name,donation):
        for donor in self.donor_list:
            if donor.donor == name:
                donor.enter_donation(donation)

    def list_donors(self):
        '''
        Create list of donors in donor database
        '''
        list_donors = ''
        for donor_name in self.donor_list:
            list_donors += donor_name.donor
            list_donors += '\n'
        return list_donors

    def create_card(self, donor, donation):
        """
        Create thank you card text
        :param donor: Name of donator
        :param donation: Amount of donation
        """
        card_text = ['Dear {}:','','Thank you for your generosity in your gift of ${:.2f}.  \
        It will go long way in supporting this charity.','']
        card_text = card_text + ['Sincerely,','','','','Kristoffer Jonson']
        card_text = "\n".join(card_text)
        card_text = card_text.format(donor,donation)
        return card_text

    def create_report(self):
        """
        Create string for formatted report of donors and amounts donated
        """
        report_text = 'Donor Name                | Total Given | Num Gifts | Average Gift' + \
        '\n'
        report_text += '------------------------------------------------------------------' + \
        '\n'
        format_string = '{:<26} $ {:>11.2f}{:>12d} $ {:>11.2f}' + '\n'
        for donor in self.donor_list:
            report_text += format_string.format(donor.donor,donor.sum_donations,\
                                                donor.num_donations,\
                                                donor.sum_donations/donor.num_donations)
        return report_text

