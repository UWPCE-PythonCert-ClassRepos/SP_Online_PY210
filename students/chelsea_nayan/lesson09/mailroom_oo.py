# chelsea_nayan, UWPCE Python 210
#Lesson09: Object-Oriented Mailroom
#Goal: Refactor the mailroom program using classes to help organize the considerations

# Hold information about a single donor, provide access to the donor-specific information that is needed
class Donor():
    def __init__(self, name, donations = []):
        self.name = name
        if type(donations) is list:
            self.donations = donations
        else:
            raise TypeError('Please enter as a list!')

    # Add a donation to a donor
    def add_donation(self, donation):
        self.donations.append(donation)

    #donor_names, total_given, num_gifts, average_gift = [], [], [], []
    def donation_nums(self):
        num_gifts = len(self.donations)
        total_given = sum(self.donations)
        average_gift = total_given / num_gifts
        donation_nums_for_report = [total_given, num_gifts, average_gift]
        return donor_info


# Hold donor objects and methods, add new donors, search for a donor, generate a report about a donor
class DonorCollection():
    def __init__(self):
        self.donor_list = []

    # Return a list of donor names
    def donor_names(self):
        self.names[]
        return [donor[0] for donor in self.donor_list]

    # Add donor information for report
    def add_donor(self, donor):
        self.donor_list.append(donor.name, donor_info)

    def setup_report(donor_names, total_given, num_gifts, average_gift):
        col1, col2, col3, col4 = [str(i) for i in donor_names], [str(i) for i in total_given], [str(i) for i in num_gifts], [str(i) for i in average_gift]
        # Get the maximum number of characters in an element in each column to estimate how much spacing there needs to be in the header
        max_donor_names, max_total_given, max_num_gifts, max_average_gift = len(max(col1, key=len)), len(max(col2, key=len)), len(max(col3, key=len))+len("| Num Gifts"), len(max(col4, key=len))
        dataset = [max_donor_names, max_total_given, max_num_gifts, max_average_gift]
        return dataset

    # Print the header
    def header_report(dataset):
        heading = ("Donor Name".ljust(dataset[0], ' ') + "|  Total Given ".ljust(dataset[1]+3, ' ') + "|  Num Gifts ".ljust(dataset[2], ' ')+ "|  Average Gift".ljust(dataset[3]+3, ' '))
        separation = ("-"*len(heading))
        header = heading +  "\n" + separation
        return header

    # Sort the donor list by the sum of their donations, from highest total to least
    # Make an iterable of the donor name and then a list of their donations
    def sort_report(donors_dict):
        sorted_dict = sorted(donors_dict.items(), key=lambda elem: sum(elem[1]), reverse=True)
        return sorted_dict

    def print_donors(self):
        #Prints donor names
        donor_names = ''
        for donors in self.donor_list:
            donor_names += donors.name + '\n'
        return donor_names

    # Send the intial donor dictionary to DonorCollection
    @staticmethod
    def initial_donors(donor_info):
        donors = DonorCollection()
        for name, amounts in donor_info.items():
        donor = Donor(name, amounts)
        donors.add(donor)
        return donors
