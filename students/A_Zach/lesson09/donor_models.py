class Donor():
    """Class defining information about a given donor"""
    
    def __init__(self, name, donation = []):
        # set a donor name
        self.name = name
        # set donation
        if type(donation) is list:
            self.donation = donation
        else:
            raise TypeError("Donations must be provided in a list")
       
       
    def new_donation(self, new_donation):
        # Add a new donation    
        if type(new_donation) is int or type(new_donation) is float:
            self.donation.append(new_donation)
        else:
            raise TypeError("Donations must be a number")


class DonorCollection():
    """Class defining the orginization of donors and their donations"""
    
    def __init__(self):
        # define a dictionary for donors and their donations
        self.donor_list = []
    
    
    def new_donor(self, donor: Donor):
        # Add a new donor
        self.donor_list.append(donor)
    
    
    def sort_donation(self, name, donation):
        # If donor is in list, append donation, if not, add donor and donation
        for donor in self.donor_list:
            if donor.name == name.title():
                donor.new_donation(donation)
                return
        new_donor = Donor(name.title(), [donation])
        self.new_donor(new_donor)
    
    def list_donors(self):
        # Generate text list of donors name to be printed
        donor_list_text = ''
        for donor in self.donor_list:
            donor_list_text += donor.name + "\n"   
        return donor_list_text
    

    def compose_email(self, name):
        # Compose and save a generic thank you email
        for donor in self.donor_list:
            if donor.name == name.title():
                email = f"\n\nDear {donor.name},\n\n\tWe appreciate your generous donations totaling ${sum(donor.donation):.2f}.\n\nThank you,\nAndrew\n\n" 
                with open(f"Thank_You_to_{donor.name}.txt", 'w+') as f:
                    f.write(email)
        return email
        
    
    def email_all(self):
        for donor in self.donor_list:
            self.compose_email(donor.name)
    
    
    def build_report(self):
        report = []
        [report.append((donor.name, sum(donor.donation), len(donor.donation), sum(donor.donation)/len(donor.donation))) for donor in self.donor_list]
        return report
        