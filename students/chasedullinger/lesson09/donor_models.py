#!/usr/bin/env python3
# PY210 Lesson 09 MailRoom 4 - Chase Dullinger

class Donor:
    """Class to hold information about a specific donor"""

    def __init__(self, name="", donation=None):
        self.name = name
        self.donations = []

        if donation:
            self.add_donations(donation)

    @property
    def total_donations(self):
        """Returns the total amount donated.  Note that this cannot be set
        directly"""
        return sum(self.donations)

    @property
    def number_of_donations(self):
        """Returns total number of donations. Note that this cannot be set
        directly"""
        return len(self.donations)

    @property
    def average_gift(self):
        """Returns average value of donations. Note that this cannot be set
        directly"""
        try:
            return self.total_donations / self.number_of_donations
        except ZeroDivisionError:
            return 0.0

    def add_donations(self, donations):
        """Adds donation(s) to the donor.
        :param donation: int, float, str, or list/tuple thereof containing
                         donation amount(s).  Must be convertible to float.
        """
        if not isinstance(donations, (list, tuple)):
            donations = [donations]  # Wrap non-lists as lists to use same code
                                     # as for lists/tuples.

        for donation in donations:
            if not donation:  # if passed an empty string or list just continue
                continue
            try:
                donation_float = float(donation)
            except ValueError:
                raise ValueError(f"Could not convert to float: {donation}")

            if donation_float < 0:
                raise ValueError(f"Invalid donation, must be greater than or\
 equal to 0 {donation_float}")
            else:
                self.donations.append(donation_float)

    def compose_email(self, donation_id=-1, write_totals=False):
        """ Writes the email note and prints it to the screen.
        :param donation_id: int specifying which donation to write about.
                            default = -1 writes letter for last added donation.
        :param write_totals: bool flag to specify if the total given should be
                            written
        :return: string containing thank you email text """
        if not write_totals:
            amount = self.donations[donation_id]
        else:
            amount = self.total_donations
        email_string = f"\nDear {self.name},\n Thank you for your generous\
 gift of ${amount:.2f}!  It will help Local Charity achieve our mission.\n\
    Best regards,\n\
    Local Charity\n\n"
        return email_string

    def sort_key(self):
        return self.total_donations


class DonorCollection:
    """Class to hold information about all donors"""

    def __init__(self):
        self.donors = []

    def add_donor(self, name, donation=None):
        """Instantiates a new donor object and adds it to the donors list
        :param name: string containing donor's name
        :param donation: int, float, str, or list/tuple thereof containing
                         donation amount(s).  Must be convertible to float.
        """
        if "," in name:  # Remove donor name commas to preserve CSV save
            print("Warning: Comma will be removed from name")
            name = name.replace(",", "")
        if name in self.donor_names:
            raise NameError(f"Can't add {name} to database.\
 Donor already exists")
        else:
            self.donors.append(Donor(name=name, donation=donation))

    def add_donor_object(self, donor_object):
        """Directly adds an existing donor object to the collection
        :param donor_object: donor_models.Donor donor_object
        :returns: None"""
        self.donors.append(donor_object)

    @property
    def donor_names(self):
        """Returns a list of donor names"""
        return [donor.name for donor in self.donors]

    def get_donor_by_name(self, name):
        """Given a name string, returns a donor object.  If donor name
        is not found, raises error"""
        for donor in self.donors:
            if donor.name == name:
                return donor

        raise NameError(f"{name} not found in existing donors")

    def add_donation_to_donor(self, name, donation):
        """Adds a donation to a donor"""
        self.get_donor_by_name(name).add_donations(donation)

    def get_donor_list_text(self):
        """Get text for donor list by looping through existing donors"""
        text_string = "\nCurrent donors are:\n"
        for donor in self.donor_names:
            text_string += f"{donor}\n"
        return text_string

    def create_all_letters(self):
        """Writes letters for all donors and saves them to disk"""
        for donor in self.donors:
            try:
                with open(f"{donor.name}.txt", "w") as f:
                    f.write(donor.compose_email(write_totals=True))
            except IOError:
                print(f"Could not write file for {donor.name}")

    def create_report(self):
        """Display donor list by looping through existing donors in donor_db and
        and show their donation data.
            :param: None
            :return: str Report string
        """
        text_string = "\n"
        text_string += "Donor Name                | Total Given | Num Gifts |\
     Average Gift\n\
    ------------------------------------------------------------------\n"
        for donor in sorted(self.donors, key=Donor.sort_key, reverse=True):
            text_string += f"{donor.name:<26} $ {donor.total_donations:>11.2f}\
 {donor.number_of_donations:>10}  $ {donor.average_gift:>11.2f}\n"

        return text_string

    def save_donor_db(self, filename="donor_db.txt"):
        """Saves donor data in DonorCollection to disk in a simple csv format
        :param filename: optional string specifying filename to save to"""
        try:
            with open(filename, 'w') as fn:
                for donor in self.donors:
                    fn.write(donor.name)
                    fn.write(",")
                    donation_list = [str(donation)
                                     for donation in donor.donations]
                    fn.write(",".join(donation_list))
                    fn.write("\n")
        except IOError:
            print("Could not save donor database")

    def read_donor_db(self, filename="donor_db.txt"):
        """Reads donor data to DonorCollection from disk in a simple csv format
        :param filename: optional string specifying filename to read from"""
        try:
            with open(filename, 'r') as fn:
                lines = fn.readlines()
                for line in lines:
                    pieces = line.rstrip().split(",")
                    name = pieces[0]
                    if len(pieces) > 1:
                        donations = pieces[1:]
                    else:
                        donations = 0
                    self.add_donor(name=name, donation=donations)
        except IOError:
            print("Could not save donor database")
