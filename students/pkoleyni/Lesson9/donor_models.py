class Donor:
    def __init__(self, name, donation):

        self.name = name.title()
        self.donation_list = []

        # Verify Donation value is valid
        if Donor.donation_value_check(donation):
            self.donation_list.append(donation)

    def __repr__(self):
        return "{}".format(self.donation_list)

    def __str__(self):
        return "Donor {} with {} donation".format(self.name, self.max_donation)


    @staticmethod
    def donation_value_check(val):
        """
        Verify donation value is not a string and is greater than zero
        """
        if isinstance(val, (int, float)) and val > 0:
            return True
        else:
            raise ValueError('Invalid Donation value')

    @property
    def max_donation(self):
        """
        return max donation made by a donor by running sum on the donation_list for
        that specific donor
        """
        return sum(self.donation_list)

    @property
    def num_of_donation(self):
        return len(self.donation_list)

    @property
    def avr_donation(self):
        return self.max_donation / self.num_of_donation


    @property
    def add_donation(self):
        return self.donation_list


    @add_donation.setter
    def add_donation(self, new_donation):
        """
        setter to add new donation value to the list of all the donations made by
        specific donor
        """
        if Donor.donation_value_check(new_donation):
            self.donation_list.append(new_donation)


class DonorCollection():

    def __init__(self):
        self.donor_dic = dict()

    def add_donation(self, name, donation):
        if DonorCollection.donation_value_check(donation):
            if self.donor_dic.get(name):
                self.donor_dic[name].add_donation = donation
            else:
                self.donor_dic[name] = Donor(name, donation)


    def find_donor(self,donor):
        if self.donor_dic.get(donor):
            return ('Donor:{}, Donations:{}'.format(donor, self.donor_dic[donor]))
        else:
            print ('Donor not found')

    @property
    def list_of_donors(self):
        return list(self.donor_dic.keys())

    @staticmethod
    def donation_value_check(val):
        """
        Verify donation value is not a string and is greater than zero
        """
        if isinstance(val, (int, float)) and val > 0 :
            return True
        else:
            raise ValueError('Invalid Donation value')

    def sort_key(key):
        """

        :param key: Key defines the item in the list to be used for sorting
        :return:
        """
        return key[1]






