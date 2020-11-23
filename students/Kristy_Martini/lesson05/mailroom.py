import operator
import os

class Report:
    def __init__(self):
        """ Report class holds the list of all donors and information associated with them."""
        self.donors = dict()
        Kristy = Donor("Kristy Martini", 0, 3, 3000)
        Mikey = Donor("Mike Martini", 0, 7, 3424834)
        Cathy = Donor("Cathy Martini", 0, 7, 63833)
        Bill = Donor("Bill Martini", 0, 10, 60000)
        Nick = Donor("Nick Martini", 0, 50, 47484949)

        initial_donors = [Kristy, Mikey, Nick, Bill, Cathy]
        [self.add_donor(donor) for donor in initial_donors]

    def add_donor(self, Donor):
        """ Add new donor to report"""
        self.donors[Donor.name] = Donor
    
    def sort_donors(self, new_report):
        """ Sorts donors by total gift value given"""
        new_report.unsorted_list = list(new_report.donors.values())
        new_report.sorted_list = sorted(new_report.unsorted_list, key=operator.attrgetter('total_gift_value'), reverse=True)
        new_report.sorted_dict = dict()
        for donor in new_report.sorted_list:
            new_report.sorted_dict[donor.name] = donor

    def create_report(self, new_report):
        """ Display donor report to the user"""
        new_report.sort_donors(new_report)

        print("Donor Name          | Total Given   | Num Gifts | Average Gift")
        print("--------------------------------------------------------------")
        for value in new_report.sorted_dict.values():
            line_str = '{0:21}'.format(value.name) + "$" + '{0:14}'.format(value.total_gift_value) + '{0:12}'.format(value.num_gifts) + " $" + '{0:12}'.format(value.average_gift)
            print(line_str)
        print("\n")
        prompt_user(new_report)

class Donor:
    """ Donor class stores the info associated with each donor"""
    def __init__(self, name, gift_value=0, num_gifts=1, total_gift_value=0):
        self.name = name
        self.gift_value = gift_value
        self.num_gifts = num_gifts
        self.total_gift_value = total_gift_value
        try:
            self.average_gift = self.total_gift_value/self.num_gifts
        except ZeroDivisionError:
            self.average_gift = 0

    def add_gift(self, amount):
        """ Add gift amount to a donor already present in database"""
        self.total_gift_value = self.total_gift_value + amount
        self.num_gifts += 1
        self.average_gift = self.total_gift_value/self.num_gifts

def check_name(new_report=None):
    """ Check the name of the donor before sending a thank you, add to donor list if they do not exist"""
    if new_report is None:
        new_report = Report()
    print("To whom would you like to send a thank you?")
    name_to_thank = input("Please enter the full name of the donor you'd like to thank, or enter 'list' to view a list of current donors: ")
    if name_to_thank == "quit":
        prompt_user(new_report)
    if name_to_thank == "list":
        new_report.create_report(new_report)
        print("Would you like to thank a donor from this list?")
        name_to_thank= input("Please enter the full name of the donor you'd like to thank, or enter 'quit' to exit: ")
        if name_to_thank == "quit":
            prompt_user(new_report)
    try: 
        donor = new_report.donors[name_to_thank]
    except KeyError:
        print(name_to_thank, " is a new donor. They will be added to our database.")
        newDonor = Donor(name_to_thank, 0, 0, 0)
        new_report.add_donor(newDonor)
        donor = new_report.donors[newDonor.name]
    finally:
        donation_amount = input("Please enter the donation amount for which you want to thank this donor: ")
        if donation_amount == "quit":
            prompt_user(new_report)
        donor.add_gift(int(donation_amount))
        send_thank_you(donor)
        prompt_user(new_report)

def send_thank_you(donor):
    """ Print a thank you to the donor"""
    output_dir = os.getcwd()
    output_file = donor.name + ".txt"
    with open(os.path.join(output_dir, output_file), 'w') as f:
        f.write("Thank you " + donor.name + " for your charitable gift to our organization.\n We could not operate without the generostiy of donors like yourself.")
        f.write("Your generous gift of " + str(donor.total_gift_value) + " will allow us to continue to serve our community in the hopes of a better world")

def send_thank_you_multiple(new_report):
    [send_thank_you(donor) for donor in new_report.donors.values()]
    prompt_user(new_report)

def quit_program(new_report=None):
    quit()

def prompt_user(new_report=None):
    if new_report is None:
        new_report = Report()

    """ Displays menu of user options"""
    arg_dict = {"1": check_name, 
                "2": new_report.create_report, 
                "3": send_thank_you_multiple, 
                "4": quit}

    print("Hello! Welcome to the donation portal. You may enter 'quit' any time you are prompted to return to this screen.")
    print("What would you like to do today?")
    print("1. Send a Thank You to a single donor.")
    print("2. Create a Report.")
    print("3. Send letters to all donors.")
    print("4. Quit")
    choice = input("Please enter the number associated with your choice: ")
    
    try:
        arg_dict[choice](new_report)
    except KeyError:
        prompt_user(new_report)

if __name__ == "__main__":
    prompt_user()