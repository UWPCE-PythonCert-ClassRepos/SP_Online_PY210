"""
Programming In Python - Lesson 9 Assignment 1: Object Oriented Mail Room
Code Poet: Anthony McKeever
Start Date: 09/10/2019
End Date: 09/15/2019
"""

import os.path

from support import Helpers
from support import FileHelpers

class Donor():
    """
    A class representing a donor.
    """

    def __init__(self, name, donations):
        """
        Initializes a Donor object.

        :self:          The Class.
        :name:          The name of the donor.
        :donoations:    The donations the donor has made.
        """
        self.name = name
        self.donations = [d for d in donations]

    
    def accept_donation(self, amount):
        """
        Accept a donation from the donor.

        :amount:    The amount they donated.
        """
        self.donations.append(amount)


    @property
    def total_donations(self):
        """
        Return a sum of the donations.
        """
        return sum(self.donations)


    @property
    def average_donation(self):
        """
        Return the average donation by the donor.
        """
        return self.total_donations / len(self)


    @classmethod
    def from_string(cls, in_value):
        """
        Instantiate a donor from a string.

        :cls:       The class
        :in_value:  The string to parse into a donor.
                    Expected format:
                        Name,Donation_1,Donation_2,Donation_3,Donation_4
                    
                    Donations should be in a floatable number.

                    Example:
                        Jelissa Jelly,100.00,20.0,30.35,40
        """
        in_value = in_value.split(',')
        name = in_value[0]
        donations = [float(d) for d in in_value[1:]]
        self = cls(name, donations)
        return self

    
    @property
    def to_summary(self): 
        """
        Return the donor's summary.
        """
        return (self.name, f"{self.total_donations:.02f}",
                len(self), f"{self.average_donation:.02f}")


    def get_email(self, template):
        """
        Return the donor's email.
        
        :self:      The Class
        :template:  The email template to use.
        """
        donation = f"{self.donations[-1]:.02f}"
        return template.format(self.name, donation)


    def __len__(self):
        """
        Return the count of the donations.
        """
        return len(self.donations)


    def __str__(self):
        """
        Return the donor in a string.
        This is not the donor's summary.  This will return an output format of the
        Donor's name and donations.

        Example Output:
            Jelissa Jelly,100.01,200.00,345.67
        """
        donations = ",".join([f"{d:.02f}" for d in self.donations])
        return f"{self.name},{donations}"


    def __lt__(self, other):
        """
        Return if this donor is less than another donor based on donations.
        """
        tuple_self = (self.total_donations, self.average_donation) 
        tuple_other = (other.total_donations, other.average_donation)
        return tuple_self < tuple_other

    
    def __eq__(self, other):
        """
        Return if the donor is equal to another donor.
        """
        return self.to_summary == other.to_summary


class Donor_Collection():
    """
    A wrapper class representing a collection of Donors.
    """

    def __init__(self, list_donors, email_template):
        """
        Instantiate a Donor Collection

        :self:              The class
        :list_donors:       The list of donors in the collection.
        :email_template:    The path to the email template for donors.
        """
        self.donors = list_donors
        self.email_template = FileHelpers.open_file(email_template, type(str()))


    @classmethod
    def from_file(cls, file_path, email_template):
        """
        Instantiate a Donor Collection from the contents of a CSV File.

        :cls:               The class
        :file_path:         The path to the donor list CSV
        :email_template:    The path to the email template for donors.
        """
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"No file exists at path: {file_path}")

        donors = [Donor.from_string(c) for c in FileHelpers.open_file(file_path, type(Donor))]

        self = cls(donors, email_template)
        return self


    def handle_donation(self, name):
        """
        Handles accepting a donoation for a donor.

        :self:  The Class
        :name:  The name of the donor who's donating.
        """
        donation = 0.0
        while donation <= 0.0:
            amount = Helpers.safe_input("How much did they donate?")
            
            if amount.lower() == "cancel":
                return
            
            donation = Helpers.validate_donation(amount)

        donor = self[name]

        if donor is not None:
            donor.accept_donation(donation)
        else:
            donor = Donor(name, [donation])
            self.donors.append(donor)

        Helpers.print_email(donor.get_email(self.email_template))
    
    @property
    def donor_summary(self):
        """
        Return the list of donor summaries.
        """
        return [d.to_summary for d in self.donors]


    @property
    def get_names(self):
        """
        Return a list of donor names.
        """
        donors = "\n\t".join([d.name for d in self.donors])
        return f"\t{donors}"


    def write_donors(self, file_path, msg=None):
        """
        Writes the donors to a file.

        :self:      The Class
        :file_path: The path of the output file.
        :msg:       The message to tell the user when the save is successful.
        """
        content = "\n".join([str(d) for d in self.donors])
        FileHelpers.write_file(file_path, content, msg)


    def save_to_file(self, file_path):
        """
        Save the donors to a file.  Will save to the execution director if save attempt fails.

        :self:      The Class
        :file_path: The path of the output file.
        """
        dir_name = os.path.dirname(file_path)
        if not os.path.isdir(dir_name):
            raise NotADirectoryError(f"No directory exists at: {dir_name}")

        try:
            msg = f"Donor list backed up to: {file_path} successfully."
            self.write_donors(file_path, msg)
        except Exception as e:
            new_file_path = os.path.join(os.path.curdir, "donor_list.csv")

            msg = str(f"Could not write file to: {file_path}\n"
                      f"The donor list has been backed up to: {new_file_path}")

            self.write_donors(file_path, msg)
            raise IOError(msg) from e
    

    def __getitem__(self, index):
        """
        Return the item at the index.
        Acceptable Index: Strings, integers, and slices.
        """
        if isinstance(index, str):
            return next((d for d in self.donors if d.name == index), None)
        else:
            return  self.donors[index]


    def __len__(self):
        """
        Return the length of the donor list.
        """
        return len(self.donors)
