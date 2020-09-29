from donor import Donor
from operator import itemgetter

class DonorDb: 
    """
    Class DonorDb is Donor database class meant to hold all Donor objects. 
    Donor objects represents a Donor with it's associated properties
    """
    def __init__(self): 
        self.database = {} 
        self.add_db_sample()

    def add_db_sample(self): 
        """
        Function adds sample data to the database. This is meant to be 
        called by __init__ in order to simplify testing
        """

        data = [
            ('William', 'Gates', [50000.0, 500.12]), 
            ('Mark', 'Zuckerberg', [20000.0, 8500.99]), 
            ('Jeff', 'Bezos', [100000.0, 40000.0, 700.99]), 
            ('Paul', 'Allen', [200000.0, 1440.0, 300.00]), 
            ('Bill', 'Gates', [30000.0, 70000.0, 450.0])
        ]
        
        for info in data: 
            donor = Donor()
            donor.fname = info[0]
            donor.lname = info[1]
            key = donor.fname + ' ' + donor.lname
            donor.donation_history.extend(info[2])
            self.database[key] = donor

    def add_donor(self, donor): 
        """
        Function adds donor to the database.
        raises an exception if donor.fname or 
        donor.lname arguments are not given.

        param: donor: Donor object 

        return: None
        """

        try: 
            key = donor.fname + ' ' + donor.lname
            self.database[key] = donor
        except TypeError: 
            raise TypeError('donor.fname and donor.lname are required arguments')
        
    def search(self, donor): 
        """
        Function searches for a donor in the donor database. 
        If donor is not found, function returns a None type
        If donor is found, donor object is returned. 

        param: donor: donor to search for 

        return: None if not found, Donor Object if found
        """

        try: 
            key = donor.fname + ' ' + donor.lname 
        except TypeError: 
            raise TypeError('donor.fname and donor.lname are required arguments')
        else: 
            return self.database.get(key)
    
    def list_donors(self): 
        """
        Function returns a list of donors in the donors database
        
        return: a 'list' of donor names
        """

        return list(self.database) #keys represent donor.fname + ' ' + donor.lname
    
    def send_letters(self): 
        """
        Function sends a letter to all donors in the donor database 
        """

        for donor in self.database.values(): #values are donor objects
            with open( donor.fname + '_' + donor.lname + '.txt', 'w') as file_object: 
                file_object.write(donor.letter())
    
    def statistics(self): 
        """
        Function creates returns a summary list, 
        that contains the total, average and number of 
        gifts a donor has contributed. 

        Return: List of tuples with each donor summary in sorted order
        """
        summary_of_donations = [
            (
                donor,
                sum(self.database[donor].donation_history), 
                len(self.database[donor].donation_history), 
                sum(self.database[donor].donation_history) / len(self.database[donor].donation_history)
            )
            for donor in list(self.database)
        ]
        
        #sort summary_of_donations by average, which is indexed by 3 i.e
        #[("bill", 10, 2, 30.5)], save results in descending order

        summary_of_donations_sorted = sorted(summary_of_donations, key=itemgetter(3), reverse=True)

        return summary_of_donations_sorted