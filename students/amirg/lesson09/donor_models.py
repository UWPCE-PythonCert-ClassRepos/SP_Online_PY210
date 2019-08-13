'''This program has the object orientated classes for donor and donorcollection'''

'''Donor object'''
class Donor(object):
    #Attributes for name of donor and list of donations
    def __init__(self, donor, *args):
        self.donor = donor
        self.donations = args

    #Sum of donations for one donor
    @property
    def sum(self):
        return sum(self.donations)

    #Average of donations for one donor
    @property
    def avg(self):
        return sum(self.donations)/len(self.donations)

    #Number of donations for one donor
    @property
    def num_donations(self):
        return len(self.donations)

    #Adds donation for one donor
    def add_donation(self, donation):
        try:
            donation = float(donation)
            if donation >= 0:
                self.donations = self.donations + (donation,)
            else:
                raise ValueError('Donation must be a positive number')
        except:
            raise ValueError('Donation must be a positive number')

    #Returns the last donor a donor made
    @property
    def last_donation(self):
        try:
            return self.donations[-1]
        except:
            raise IndexError('There are no donations')

    #Thank you note for one donor
    @property
    def donor_text(self):
        return 'Dear {},\n\n Thank you for your generous donation of ${:.2f}! \n It will be put to very good use. \n\nSincerely, \nThe Team\n'.format(self.donor, self.last_donation)

    #Writes thank you note to one donor
    def write_donor(self):
        with open('{}.txt'.format(self.donor), 'w+') as f:
            f.write(self.donor_text)
        f.close()

    #Defines less than for purposes of sorting function
    def __lt__(self, other):
        return self.sum < other.sum

    #Representation of donor object
    def __repr__(self):
        return self.donor

'''DonorCollection object'''
class DonorCollection(object):
    #Initializes list of donor objects
    def __init__(self, *args):
        self.donors = list(args)

    #Returns string of all names of donors in donorcollection
    @property
    def donor_names(self):
        return ('\n').join([i.donor for i in self.donors])

    #Adds donor object to donorcollection
    def add_donor(self, name):
        self.donors.append(Donor(name))

    #Gets a donor object for a donor name input
    def get_donor(self, name):
        try:
            temp = ''
            for i in self.donors:
                if i.donor == name:
                    temp = i
                    break
                if i == self.donors[-1]:
                    raise IndexError('Donor is not in list')
            return temp
        except:
            raise IndexError('Donor is not in list')

    #Returns string for report of all donors
    @property
    def report(self):
        middle_string = ''
        #Title string of the report
        top_string = '\n' + '{:20}'.format('Donor Name') + '  ' + 'Total Given' + '  ' + 'Num Gifts' + '  ' + 'Average Gift' + '\n' + '\n'
        #List comprehension
        self.donors.sort(reverse = True)
        #List comprehension for donor information output
        middle_string = ['{:20}'.format(self.donors[i].donor) + ' $' + '{:11.2f}'.format(self.donors[i].sum) + '  ' + 
                         '{:9.0f}'.format(self.donors[i].num_donations) + ' $' + '{:12.2f}'.format(self.donors[i].avg)
                         + '\n' for i in range(len(self.donors))]
        final_string = top_string + ''.join(middle_string)
        return final_string

    #Writes thank you notes to all donors
    def write_donors(self):
        [i.write_donor() for i in self.donors]

        




        
