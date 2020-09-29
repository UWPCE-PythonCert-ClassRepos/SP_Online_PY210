import os


class Donor(object):
    """This class handles single donor data"""

    def __init__(self, current_donor_history, donor_name):
        """self.donor is the number of and amount of donations associated with a particular donor, named self.donor"""
        self.donations = current_donor_history
        self.name = donor_name

    @property
    def donor_sum(self):
        """adds up all of the donations of a particular donor"""
        return sum(self.donations)

    @property
    def donor_average(self):
        """averages all of the donations of a particular donor"""
        return sum(self.donations) / len(self.donations)

    @property
    def donor_donations(self):
        """counts the number of all of the donations of a particular donor"""
        return len(self.donations)

    def message(self):
        """our default thank you message"""
        return f"\nThank you {self.name} for your donations totaling ${self.donor_sum:.2f}, your donations make the " \
            f" work of the 'American society for taking donations' possible.\n\n""Sincearly,\n\n""A low paid intern\n "

    def update_donor(self, new_donate):
        """adds a donation to an existing donors profile"""
        self.donations.append(new_donate)


class DonorCollection(object):
    """Class to handle all of the methods that have to do with multiple donors at once"""

    def __init__(self, donor_list):
        self.donors = {donor.name: donor for donor in donor_list}

    def mass_send_thanks(self):
        """this is the method that writes thank you letters to all of our donors, and places them in one folder to
        avoid headache """
        try:
            os.mkdir("Letters")
        except FileExistsError:
            pass
        for item in self.donors:
            with open(f"Letters/{self.donors[item].name}.txt", "w+") as letter:
                letter.write(self.donors[item].message())

    def sorting_function(self):
        """does what the name suggests, it sorts our dictionary of donors"""
        temp_list = []
        for item in self.donors:
            temp_list.append([self.donors[item].donor_sum, self.donors[item].name, self.donors[item].donor_donations,
                              self.donors[item].donor_average])
        return sorted(temp_list, reverse=True)

    def update_donor(self,query, new_donate):
        """adds a donation to an existing donors profile"""
        for item in self.donors:
            if self.donors[item].name == query:
                self.donors[item].update_donor(new_donate)

    def add_donor(self,query, new_donate):
        """adds a new donor"""
        self.donors.update({query: Donor([new_donate],query)})

    def list_donors(self):
        """lists the donors"""
        temp_list=""
        for donor in self.donors:
            temp_list += f"{donor}\n"
        return temp_list


class FileHandling(object):
    """class dealing with handling files like opening and saving"""

    def __init__(self, chosen_file):
        self.file = chosen_file

    def open_file(self):
        """opens a file, if it doesn't exist it yells at you"""
        try:
            with open(f"{self.file}.txt", "r") as donor_list:
                return donor_list.read()
        except FileNotFoundError:
            return "file not found"

    def save_file(self, new_donor_collection_object):
        """saves a file, writing a new one if the file name doesnt exist"""
        temp_dict = {new_donor_collection_object.donors[item].name:new_donor_collection_object.donors[item].donations
                   for item in new_donor_collection_object.donors}
        with open(f"{self.file}.txt", "w+") as donor_file:
            donor_file.write(str(temp_dict))
