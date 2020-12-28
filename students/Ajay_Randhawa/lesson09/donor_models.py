class Donor():
    '''
    this class parses information for a single donor from the donorCollection class
    it also creates the donor objects
    '''
    def __init__(self, name, donation):
        self.name = name
        self.donation_count = 1
        self.total_donation = donation
        global x
        if x != 1:
            self.send_thankyou(name, donation)
        self.avg_donation = self.average_donation(donation, self.donation_count)

    def send_thankyou(self, donor, donation):
        return print(f'\nThank you {donor} for your generous donation of {donation}\n')
    
    def average_donation(self, donation, count):
        average_donation = round(donation / count)
        return average_donation

    def add_donation(self, donor, donation):
        self.donation_count = self.donation_count + 1
        self.total_donation = self.total_donation + donation
        self.avg_donation = self.average_donation(self.total_donation, self.donation_count)
        self.send_thankyou(donor, donation)



class DonorCollection(): 
    """
    Stores the data for all donors. At initilizaiton, takes a dict and parses the data 
    in the class.
    """
    def __init__(self, dict1):
        self.donorlist = {}
        self.instance = []
        self.donorlist = dict1
        print(dict1)
        global x
        for donor, donation in self.donorlist.items():
            # self.instance_name = donor.replace(" ", "_")
            x = 1
            self.instance_name = Donor(donor, donation[0])
            self.instance.append(self.instance_name)
            
            self.instance_name.donation_count = donation[1]
            self.instance_name.avg_donation = donation[2]
        x = 0

    def add_donation(self, name, donation):
        '''
        append method to store new donors or update values. it updates the donor instaces from
        within this method
        '''
        count = -1
        for donor, new_donation in self.donorlist.items():
            count = count + 1

            if (donor.lower()) == (name.lower()):
                # print("\n*We found you in our records*")
                self.instance_name = self.instance[count]
                self.instance_name.add_donation(donor, donation)
                new_donation[0] += donation
                new_donation[1] += 1
                new_donation[2] = round(new_donation[0] / new_donation[1])
                break
        else:
            # self.instance_name = name.replace(" ", "_")
            self.instance_name = Donor(name, donation)
            self.instance.append(self.instance_name)
            self.donorlist[name] = [self.instance_name.total_donation, self.instance_name.donation_count, self.instance_name.avg_donation]
                
    def sort_list(self, some_list):
        """
        sorts the list by total donation in descending order
        """
        sorted_list = sorted(some_list.items(), key=lambda t: t[1][0], reverse=True)
        return sorted_list

    def letters_toAllDonors(self):
        """
        create letters for each donor in the current directory
        """
        for donor, (total, number, average) in self.donorlist.items():
            filename = donor.replace(" ", "_") + ".txt"
            letter = "Dear %s,\n\n    Thank you for your very kind donation of %s.\n    It will be put to very good use.\n\nSincerely, \n-The Team"%(donor, total)
            with open(filename, 'w') as g:
                g.write(str(letter))
        print("\n *Letters created in current directory*\n")

