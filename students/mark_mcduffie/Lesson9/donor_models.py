#Mark McDuffie
#6/11/20
#Donor class



class Donor(object):

    def __init__(self, name, donation=None):
        """ Initializes the donor object """
        self.name = name
        self.donation = donation if donation is not None else []

    def add_donation(self, amount):
        self.donation.append(amount)


    def print_thanks(self):
        note = (f'Dear {self.name},'
             f'\n \tThank you for your donation of ${self.donation[-1]:.2f}.'
             '\nYour generosity is greatly appreciated, we '
             '\nlook forward to hearing from you again. '
             "\nCheers, \nThe Mailroom")
        return note

class DonorCollection():

    def __init__(self):
        self.donors = {}

    #initializes list of current donor data
    @staticmethod
    def initialize_dict(donor_dict):
        donors = DonorCollection()
        for name, amounts in donor_dict.items():
            donor = Donor(name, amounts)
            donors.add_donor(donor)
        return donors

    #adds new donor
    def add_donor(self, donor):
        self.donors[donor.name] = donor

    #returns list of just donor names
    def donor_list(self):
        list = []
        for names in self.donors:
            list.append(names)
        return '\n'.join(list)

    #Writes new files to save donor thank you messages
    def send_all(self):
        for donor in self.donors.values():
            filename = donor.name + '.txt'
            with open(filename, 'w') as f:
                f.write(Donor.print_thanks(donor))

    #Calculates report data and stores into sorted list
    def make_report(self):
        report = []
        total = 0
        for value in self.donors.values():
            total = sum(value.donation)
            count = len(value.donation)
            average = total / count
            data = (value.name, total, count, average)
            report.append(data)
        report.sort(key=sort_key, reverse=True)
        return report

    #Checks if donor is already in database or not
    def donor_exists(self, name):
        # Search for donor name in donor collection.
        return any(d for d in self.donors.values() if d.name.lower() == name.lower())

def sort_key(donations):
    return donations[1]