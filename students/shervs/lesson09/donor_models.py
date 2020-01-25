import string

class Donor(object):
    #Creats donor   attributes: name , donations
    def __init__(self, name , donation=None):
        self.name = name
        if donation:
            self.donations = donation
        else:
            self.donations =[]
       
    def add_donation(self, new_donation):
        #adds new donation value
        self.donations.append(new_donation)
       
    def sum_donation(self):
        #sums up all donations
        return sum(self.donations)
   
    def num_donation(self):
        #shows numners of donations
        return len(self.donations)
   
    def average_donation(self):
        #calculates average donation
        return self.sum_donation()/self.num_donation()

    def __lt__(self, other):
        # compare sum of donations between two donors
        return self.sum_donation() < other.sum_donation()
   
    def __str__(self):
        return f"{self.name:26s} $ {self.sum_donation():10.2f} {self.num_donation():11d}  $ {self.average_donation():11.2f}"
       
    def letter_content(self):
        #creates contents of thank you letter for each donor
        return f'''Dear {self.name},\n
         Thank you for your donation of ${self.sum_donation()} throughout these years.\n
         Cheers,\n
              -The team'''    

    def letter_file_name(self):    
        #create files name for each thank you letter 
        donor_name = self.name.translate(str.maketrans('', '', string.punctuation)).split()
        file_name = '_'.join(donor_name)+'.txt'
        return file_name

class DonorCollection:
    #attribute: donors 
    def __init__(self):
        self.donors = []
       
    def add_donor(self , donor):
        #adds a new donor
        self.donors.append(donor)
       
    def __str__(self):
        print_list = []
        for donor in self.donors:
            print_list.append(donor.name)
        return '\n'.join(print_list)
   
    def sort(self):
        #Sorts the list of donors based on donnor's sum of donations.
        self.donors.sort(reverse=True)
       
    def add_to_list(self,name ,new_donation):
        #adds a new donation for existing donor, if donor doesn't exists, #creats a new donor
        for donor in self.donors:
            if name == donor.name:
                donor.add_donation(new_donation)
                return
        self.add_donor(Donor(name, [new_donation]))