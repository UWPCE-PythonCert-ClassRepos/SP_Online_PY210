import argparse
import os

class Report:
    def __init__(self):
        """ Report class holds the list of all donors and information associated with them."""
        self.donors = list()
        Kristy = Donor("Kristy Martini", 0, 3, 3000)
        Mikey = Donor("Mike Martini", 0, 7, 3424834)
        Cathy = Donor("Cathy Martini", 0, 7, 63833)
        Bill = Donor("Bill Martini", 0, 10, 60000)
        Nick = Donor("Nick Martini", 0, 50, 47484949)
        
        initial_donors = [Kristy, Mikey, Nick, Bill, Cathy]
        for donor in initial_donors:
            self.add_donor(donor)

    def add_donor(self,Donor):
        """ Add new donor to report"""
        self.donors.append(Donor)

    def create_report(self):
        """ Display donor report to the user"""
        print("Donor Name          | Total Given   | Num Gifts | Average Gift")
        print("--------------------------------------------------------------")
        for donor in self.donors:
            name_sapce = 19 - len(donor.name)
            total_space = 12 - len(str(donor.total_gift_value))
            num_space = 10 - len(str(donor.num_gifts))
            average_space = 10 - len(str(donor.average_gift))
            print(donor.name, " "*name_sapce, "$", " "*total_space, donor.total_gift_value,
                 " "*num_space, donor.num_gifts, "$", " "*average_space, donor.average_gift)
        print("\n")

class Donor:
    """ Donor class stores the info associated with each donor"""
    def __init__(self, name, gift_value=0, num_gifts=1, total_gift_value=0):
        self.name = name
        self.gift_value = gift_value
        self.num_gifts = num_gifts
        self.total_gift_value = total_gift_value
        if self.num_gifts == 1:
            self.average_gift = self.gift_value
        else:
            self.average_gift = self.total_gift_value/self.num_gifts

    def add_gift(self, amount):
        """ Add gift amount to a donor already present in database"""
        self.total_gift_value = self.total_gift_value + amount
        self.num_gifts += 1
        self.average_gift = self.total_gift_value/self.num_gifts

def check_name(newReport):
    """ Check the name of the donor before sending a thank you, add to donor list if they do not exist"""
    print("To whom would you like to send a thank you?")
    name_to_thank = input("Please enter the full name of the donor you'd like to thank, or enter 'list' to view a list of current donors: ")
    if name_to_thank == "quit":
        prompt_user(newReport)
    donor_found = False
    if name_to_thank == "list":
        newReport.create_report()
        print("Would you like to thank a donor from this list?")
        name_to_thank= input("Please enter the full name of the donor you'd like to thank, or enter 'quit' to exit: ")
        if name_to_thank == "quit":
            prompt_user(newReport)
    for donor in newReport.donors:
        if donor.name == name_to_thank:
            donor_found = True
            donation_amount = input("Please enter the donation amount for which you want to thank this donor: ")
            if donation_amount == "quit":
                prompt_user(newReport)
            donor.add_gift(int(donation_amount))
            send_thank_you(name_to_thank, donation_amount)
            prompt_user(newReport)
    if donor_found == False:
        print(name_to_thank, " is a new donor. They will be added to our database.")
        donation_amount = input("Please enter the donation amount for which you want to thank this donor: ")
        if donation_amount == "quit":
            prompt_user(newReport)
        newDonor = Donor(name_to_thank, int(donation_amount), 1, int(donation_amount))
        newReport.add_donor(newDonor)
        send_thank_you(name_to_thank, donation_amount)
        prompt_user(newReport)
    
def send_thank_you(name, donation_amount):
    """ Print a thank you to the donor"""
    print("Thank you ", name, " for your charitable gift to our organization. We could not operate without the generostiy of donors like yourself.")
    print("Your contribution of ", donation_amount, " will allow us to continue to serve our community in the hopes of a better world")

def prompt_user(newReport=None):
    """ Displays menu of user options"""
    print("Hello! Welcome to the donation portal. You may enter 'quit' any time you are prompted to return to this screen.")
    print("What would you like to do today?")
    print("1. Send a Thank You")
    print("2. Create a Report")
    print("3. quit")
    choice = input("Please enter the number associated with your choice: ")
    if choice == "1":
        if newReport is None:
            newReport = Report()
        check_name(newReport)
    elif choice == "2":
        if newReport is None:
            newReport = Report()
        newReport.create_report()
        prompt_user(newReport)
    elif choice == "3":
        quit()
    
if __name__ == "__main__":
    prompt_user(None)