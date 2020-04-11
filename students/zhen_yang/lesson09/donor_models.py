# donor_models.py
# This module contains the Donor and DonorCollection classes.

thankyou_format1 = "Dear {} {},\n\
    Thank you for your generous donation of ${:,.2f}\n\
    It will be put to very good use.\n\n\
               Sincerely,\n\
                  Zhen "
#scientific format for large amount of money
thankyou_format2 = "Dear {} {},\n\
    Thank you for your generous donation of ${:,.3e}\n\
    It will be put to very good use.\n\n\
               Sincerely,\n\
                  Zhen "

thankyouall_format1 = "Dear {} {},\n\
    Thank you for your generous donation.\n\
    Total:${:,.2f} Number of Gifts:{} Average:${:,.2f}.\n\
    It will be put to very good use.\n\n\
               Sincerely,\n\
                 Zhen\n"

#scientific format for large amount of money
thankyouall_format2 = "Dear {} {},\n\
    Thank you for your generous donation.\n\
    Total:${:,.3e} Number of Gifts:{} Average:${:,.3e}.\n\
    It will be put to very good use.\n\n\
               Sincerely,\n\
                 Zhen\n"

class Donor(object):
    def __init__(self, first_name, last_name, donation):
        self._first_name = first_name
        self._last_name = last_name
        self._donation = [donation]

    @property # attribute: first_name. it is a read only attribute.
    def first_name(self):
        return self._first_name

    @property # attribute: last_name. it is a read only attribute.
    def last_name(self):
        return self._last_name

    @property # attribute: donation
    def donation(self):
        return self._donation

    @property # attribute: total donation for current donor
    def total_amount(self):
        return sum(self._donation)

    @property # attribute: total number of donation for current donor
    def total_gifts(self):
        return len(self._donation)

    def add_donation_amount(self, amount):
        self._donation.append(amount)

    def generate_thankyou_letter(self):
        last_amount = self._donation[len(self.donation) - 1]
        if self.total_amount > 1000000:
            return thankyou_format2.format(self.first_name, self.last_name,
                                           last_amount)
        else:
            return thankyou_format1.format(self.first_name, self.last_name,
                                           last_amount)

    def send_letters(self):
        avg = self.total_amount / self.total_gifts
        if self.total_amount > 1000000:
            return thankyouall_format2.format(self.first_name, self.last_name,
                                              self.total_amount,
                                              self.total_gifts, avg)
        else:
            return thankyouall_format1.format(self.first_name, self.last_name,
                                              self.total_amount,
                                              self.total_gifts, avg)


class DonorCollection(object):
    def __init__(self):
        self._donorList = [] # initialize the donor list

    @property # attribute: donorList
    def donorList(self):
        return self._donorList

    def find_donor(self, new_donor):
        return next((donor for donor in self._donorList
                     if(donor._first_name.lower() ==
                        new_donor._first_name.lower() and
                        donor._last_name.lower() ==
                        new_donor._last_name.lower())), None)

    # update the donors_db
    def update_donors_db(self, new_donor):
        the_donor = self.find_donor(new_donor)
        if the_donor is None: # new_donor is a new donor
            self._donorList.append(new_donor)
            return new_donor # return the new donor
        else:# new_donor is an existing donor
            the_donor.add_donation_amount(new_donor.donation[0])
            return the_donor # return the existing donor

    @staticmethod
    def sort_key(self):
        return (sum(self._donation), self._first_name, self._last_name)

    def sort_donors_db(self):
        return sorted(self._donorList, key=DonorCollection.sort_key)

    def create_report_title(self):
        title_formater = '{:^20s}|{:^15s}|{:^15s}|{:^20s}\n'
        column_list = ['Donor Name', 'Total Amount', 'Num Gifts',
                       'Average Amount']
        title = title_formater.format(*column_list)
        seperate_line = '-' * 71
        title = f'{title}{seperate_line}'
        return (title)

    def create_report_content(self):
        # scientific notation output
        content_formater_1 = '{:<20s} ${:>14,.3e}{:>15d}  ${:>17,.3e}\n'
        content_formater_2 = '{:<20s} ${:>14,.2f}{:>15d}  ${:>17,.2f}\n'
        content_list = []
        for donor in self.sort_donors_db():
            name = [donor._first_name, donor._last_name]
            name = ' '.join(name)
            # big money using scientific notation
            if donor.total_amount > 1000000:
                content = content_formater_1.format(name, donor.total_amount,
                                                    donor.total_gifts,
                                                    (donor.total_amount /
                                                     donor.total_gifts))
            else:
                content = content_formater_2.format(name, donor.total_amount,
                                                    donor.total_gifts,
                                                    (donor.total_amount /
                                                     donor.total_gifts))
            content_list.append(content)
        return ''.join(content_list)# generate the output report string
