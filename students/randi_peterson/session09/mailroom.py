class Donor():
    def __init__(self,name,donations=[]):
        #Creates a donor
        self.name = name
        if type(donations) is list:
            self.donations = donations
        else:
            raise TypeError('Donations must be entered as a list')

    def add_donation(self,donation):
        #Adds donation to existing donor
        self.donations.append(donation)

    def calculate_report(self):
        #Calculates and returns report metrics for Donor
        donation_number = len(self.donations)
        total_given = sum(self.donations)
        avg_gift = total_given/donation_number
        return total_given,donation_number,avg_gift


class DonorCollection():
    def __init__(self):
        #Creates donor database
        self.donor_list = []

    def __iter__(self):
        #Iterates over donor_list
        return self.donor_list.__iter__()

    def add_to_list(self,fullname,new_donation):
        #Finds donor in database or creates a new one
        for donors in self.donor_list:
            if fullname == donors.name:
                donors.add_donation(new_donation)
                return

        #This code is only run if the donor was not already found
        new_donor = Donor(fullname,[new_donation])
        self.donor_list.append(new_donor)

    def add_donor(self,donor: Donor):
        #Adds existing donor object to the list
        self.donor_list.append(donor)

    def create_report(self):
        # Create report data from donor list
        return self.format_report(*self.form_report())

    def form_report(self):
        #Creates report of all donors
        donor_report = dict()
        for donor in self.donor_list:
            donor_report[donor.name] = donor.calculate_report()
        name_lst = list(donor_report.keys())
        name_lst_sorted = sorted(name_lst, key = lambda name:donor_report[name][0],reverse=True)
        return name_lst_sorted, donor_report

    def format_report(self, name_lst_sorted, donor_report):
        # Formats report
        header = ['Name', 'Total Given', '# of Gifts', 'Average Gift']
        header_format = "{:<20}" + "{:^15}" + "{:^15}" + "{:^10}"
        row_name_format = "{:<20}"
        row_data_format = "${:>15.2f}" + "{:^15}" + "${:>10.2f}"

        string_to_print = header_format.format(*header) + '\n'
        string_to_print += '-' * 70 + '\n'

        for name in name_lst_sorted:
            string_to_print += row_name_format.format(name) + row_data_format.format(*donor_report[name]) + '\n'

        return string_to_print

    def print_donors(self):
        #Prints donor names
        donor_names = ''
        for donors in self.donor_list:
            donor_names+= donors.name + '\n'
        return donor_names