import os


class Donor(object):
    """This class handles single donor data"""
    donor = []

    def __init__(self, current_donor_history, donor_name):
        """self.donor is the number of and amount of donations associated with a particular donor, named self.donor"""
        self.donor = current_donor_history
        self.name = donor_name

    @property
    def donor_sum(self):
        """adds up all of the donations of a particular donor"""
        return sum(self.donor)

    @property
    def donor_average(self):
        """averages all of the donations of a particular donor"""
        return sum(self.donor) / len(self.donor)

    @property
    def donor_donations(self):
        """counts the number of all of the donations of a particular donor"""
        return len(self.donor)

    def __str__(self):
        """our default thank you message"""
        return f"\nThank you {self.name} for your donation of ${self.donor_sum:.2f}, your donations make the work "\
            f"of the 'American society for taking donations' possible.\n\n""Sincearly,\n\n""A low paid intern\n "


class DonorCollection(object):
    """Class to handle all of the methods that have to do with multiple donors at once"""

    def __init__(self, donor_list):
        self.donors = donor_list

    def mass_send_thanks(self):
        """this is the method that writes thank you letters to all of our donors, and places them in one folder to
        avoid headache """
        try:
            os.mkdir("Letters")
        except FileExistsError:
            pass
        for item in self.donors:
            with open(f"Letters/{item}.txt", "w+") as letter:
                letter.write(str(Donor(self.donors[item],item)))

    def sorting_function(self):
        """does what the name suggests, it sorts our dictionary of donors"""
        temp_list = []
        for keys, values in self.donors.items():
            temp_list.append([sum(values), keys, len(values), sum(values) / len(values)])
        return sorted(temp_list, reverse=True)

    def update_donor(self,query, new_donate):
        """adds a donation to an existing donors profile"""
        self.donors[query].append(new_donate)

    def add_donor(self,query, new_donate):
        """adds a new donor"""
        self.donors[query] = [new_donate]

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

    def save_file(self, new_donor_list):
        """saves a file, writing a new one if the file name doesnt exist"""
            with open(f"{self.file}.txt", "w+") as donor_file:
                donor_file.write(str(new_donor_list))
