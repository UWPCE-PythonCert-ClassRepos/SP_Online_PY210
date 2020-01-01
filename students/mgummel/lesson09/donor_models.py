#! /usr/bin/env python3


class Donor(object):

    def __init__(self, donor_name, donation):
        """
        Instantiates an object of type Donor using donor's
        fullname and initial donation amount

        :param donor_name: The full name of the donor
        :type donor_name: str
        :param donation: Donation amount
        :type donoation: float
        """
        if isinstance(donor_name, str):
            self._full_name = donor_name
        else:
            raise TypeError("Donor Name must be type str")

        if isinstance(donation, float):
            self._donations = [donation]
        else:
            raise TypeError("Donation must be of type float")
        self._total_donation = donation

    @property
    def total_donation(self):
        """
        Returns the total amount that a donor has
        donated across all donations.
        """
        return self._total_donation

    @property
    def num_of_donations(self):
        """
        Returns the length of the list _donations. This is the 
        equivalent to the number of donations.
        """
        return len(self._donations)

    @property
    def avg_donation(self):
        """
        Returns the average donation amount
        """
        return self._total_donation / self.num_of_donations

    @property
    def last_donation(self):
        """
        Returns the last donation amount the a donor's list of donations
        """
        return self._donations[-1]

    @property
    def filename(self):
        """
        Returns the name of a file that will be generated with email
        templates.
        """
        translator = {ord(" "): "_", ord(","): None}
        return f'{self._full_name.translate(translator)}.txt'

    @property
    def data(self):
        """
        Returns a tuple of organized information that can be used to
        display donor metrics
        """
        return (self._full_name, self.total_donation, self.num_of_donations, self.avg_donation)

    def add_donation(self, donation_amt):
        """
        adds the donation amount to the database.

        :param donation_amt: amount to add to new donation
        :type sponsor: float
        """

        self._donations.append(donation_amt)
        self._total_donation += donation_amt

    def __str__(self):
        """
        Returns a templated email based on donor and donation
        amount to be sent to the donor.
        """
        email_template = '\n'.join((f'\n\nDear {self._full_name},\n',
                                    f'Thank you for your very kind donation of ${self.last_donation:.2f}.\n',
                                    'It will be put to very good use.\n',
                                    '           Sincerely,',
                                    '             -The Team\n'))
        return email_template


class DonorCollection(object):

    def __init__(self, *args: Donor):
        """
        Instantiates an object of type Donor Collection. 
        Creates a list of Donor objects based on the the number
        of Donors listed in the arguments.

        :param *args: Accepts Donor type only.
        :type *args: Donor(object)
        """
        self.donor_list = list()

        for donor in args:
            if isinstance(donor, Donor):
                self.donor_list.append(donor)
            else:
                raise TypeError(
                    "Donor Collections must be instantiated with Donor object")

    def generate_list_of_names(self):
        """
        Returns a list of names in the Donor Collection for user 
        to add donations to particular Donor
        """
        names = [donor._full_name for donor in self.donor_list]
        name_selection = "\n".join(
            ["{}"] * len(self.donor_list)).format(*names)
        return name_selection

    def add_donor(self, new_donor: Donor):
        """
        Adds a new Donor to the DonorCollection
        """
        self.donor_list.append(new_donor)

    def find_donor(self, existing_donor):
        """
        Finds a Donor in the list of Donors and returns
        that object. Returns None if existing_donor is not 
        found.

        :param existing_donor: Full name of the donor
        :type existing_donor: str
        """
        donor_object = None
        for donor in self.donor_list:
            if existing_donor == donor._full_name:
                donor_object = donor
                break
        return donor_object

    def report_data(self):
        """
        Returns a list of tuples(Donor class properties) that can be easily
        printed in a formatted manner.
        """
        report = [donor_obj.data for donor_obj in self.donor_list]
        return report

    def letters_to_send(self, dir_path):
        """
        Creates text files to send to each donor that exists in the 
        DonorCollection instance

        :param dir_path: The directory where the .txt files will be created
        :type dir_path: str
        """
        for donor in self.donor_list:
            with open(f'{dir_path}/{donor.filename}', 'w', encoding='utf-8') as email:
                email.write(donor.__str__())


def main():
    pass


if __name__ == '__main__':
    main()