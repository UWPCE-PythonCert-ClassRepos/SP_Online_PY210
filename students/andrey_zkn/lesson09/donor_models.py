
from operator import itemgetter


class Donor(object):

    def __init__(self, name, donation_amt=None):
        """ Initializes the donor object """
        self.name = name
        self.donation_amt = donation_amt if donation_amt is not None else []

    def add_donation(self, amount):
        """ Add donation amount """
        self.donation_amt.append(amount)


    def print_thank_you_message(self):
        """ Print Thank You message """
        message = (f'\nDear {self.name},'
               f'\n\nThank you for your generous donation of ${self.donation_amt[-1]:.2f}.' 
               '\nWe value your contribution and support.' 
               '\n\nSincerely,\n\nNew Horizon Charity Director\n')
        return message

    def sort_key(self):
        return sum(self.donation_amt)



class DonorCollection():
    """ Initialize donors dictionary """
    def __init__(self):
        self.donors = {}

    @staticmethod
    def initialize_donors_dict(donor_data):
        # create a new collection object
        donors = DonorCollection()                     
        for name, amounts in donor_data.items():     
            donor = Donor(name, amounts)            
            # add the new donor to the collection
            donors.add(donor)
        return donors  

    def add(self, donor):
        """ Add donor to the collection """
        self.donors[donor.name] = donor

    def list_of_donors(self):
        """ Generate a list of donors """
        lod=[]
        for name in self.donors:
            lod.append(name)
        return '\n'.join(lod)
      
    def send_letters_to_all(self):
        """ Save donor letters to files """
        for donor in self.donors.values():
            filename = donor.name + '.txt'
            with open(filename, 'w') as f:
                f.write(Donor.print_thank_you_message(donor))
    
    def create_report(self):
        """ Generate a donation history report """
        header ='\n{:<20}|{:^15}|{:^15}|{:>15}'.format("Donor Name", "Total Given",
                                                   "Num Gifts", "Average Gift")
        print("Donation Report")
        print(header)
        print('-'*len(header))
        for entry in self.donors.values():
            total = sum(entry.donation_amt)
            num = len(entry.donation_amt)
            avg = total/num
            print('{:<20} ${:>14,.2f}{:>14}  ${:>16,.2f}'.format(entry.name,total,num,avg))
        print('')
  
    def donor_exists(self, name):
        #Search for donor name in donor collection.    
        return any(d for d in self.donors.values() if d.name.upper() == name.upper())