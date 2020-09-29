import pathlib

class Donor:

    def __init__(self, full_name):
        self.name = full_name
        self.donations = []

    @property
    def total_donation(self):
        """sum of donation history property"""
        return sum(self.donations)

    @property
    def num_donation(self):
        """number of donations with a donors history"""
        return len(self.donations)

    @property
    def ave_donation(self):
        """average donation of a donor's history"""

        if self.num_donation == 0:
            return 0
        else:
            return (self.total_donation/self.num_donation)

    def add_donation(self, *args):
        """add donation amount to a donor object"""
        for i in args:
            self.donations.append(i)

    def __lt__(self, other):
        """sorts the order"""
        return self.total_donation < other.total_donation

    def __repr__(self):
        return self.name

    def send_thank_you(self, money_amount):
        """Sends a thank you note when a donation is made."""
        return "Thank you {} for your donation amount of {} $. We thank you for your support".format(self.name, money_amount)


class DonorCollection:

    """
    A class containing information of a list of Donor objects
    """

    def __init__(self, donors=[]):
        """Create a collection of donor objects."""
        self.donor_obs_list = donors

    @property
    def list_donors(self):
        """Return a list of all donors in the collection."""
        return self.donor_obs_list

    @list_donors.setter
    def list_donors(self, donors = []):
        self.donor_obs_list.extend(donors)

    def add_donors(self, *args):
        """Add a donor to the collection."""
        self.list_donors.extend(args)

    def __repr__(self):
        names = [donor.name for donor in self.list_donors]
        return ', '.join(names)

    def send_thanks_all(self):
        pth = str(pathlib.Path.cwd())+'/' 
        for this_ob in self.list_donors:
            mydestin = self.make_mydestin(this_ob.name, pth) #underscore after any part of the name
            with open(mydestin, "w") as myfile:
                myfile.write(self.write_thanks_to_all(this_ob.name, this_ob.total_donation))

    def make_mydestin(self, name, pth):
        return pth + name.replace(", ", "_").replace(" ", "_")+".txt"

    def write_thanks_to_all(self, name, total):
        my_text = "Dear {},\n\t Thank you for your kind donation of {}\n. It will be put to good use\n\tSincerely\n\t\tThe team"\
                    .format(name, total)
        return my_text

    def create_report(self):
        """Generate a tabular report of donors in the collection"""
        report_lines =[]
        header ='\n{:<19}|{:^13}|{:^13}|{:>13}\n'.format("Donor Name",
                "Total Given","Num Gifts", "Average Gift")
        report_lines.append(header)
        report_lines.append('-'*len(header))
        report_lines.append('\n')
        donor_sort = sorted(self.list_donors, reverse = True)
        for this_ob in donor_sort:
            name, num = this_ob.name, this_ob.num_donation
            total, ave = this_ob.total_donation, this_ob.ave_donation
            report_str = '{:<19} ${:>13}{:>13}  ${:>12,.2f}\n'.format(name,
                          total,num,ave)
            report_lines.append(report_str)
        return "".join(report_lines)




