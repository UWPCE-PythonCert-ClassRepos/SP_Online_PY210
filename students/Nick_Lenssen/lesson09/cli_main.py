from sys import exit
import donor_models as dm

my_donors = dm.DonorCollection()

def create_report():
    """uses my_donors total data structure to create report"""
    print(my_donors.create_report())

def send_thanks_to_all():
    """calls to function in DonorCollection"""
    print (my_donors.send_thanks_all())

def get_donation_amount():
    """prompts user for an amount to donate or to go back to original prompt"""
    while True:
        amount = input("\nPlease enter in the amount you want to donate or c to go to original prompt: ")
        try:
            if amount == 'c': #if user goes clears, nothing is returns to get_thanks_info
                return
            else:
                amount = int(amount)
            return amount
        except ValueError:
            print ('\nPlease enter an integer amount to donate')

def get_donor_info():
    """prompts user for name or to go back"""
    while True:
        full_name = input("\n\nPlease enter a name for a Thank You to go out or c to go to orginal: ")
        if full_name == 'list':
            print (my_donors)
        elif full_name == 'c':
            return
        else:
            amount = get_donation_amount()
            if not amount: #if get donation returns nothing, return nothing back to main
                return
            else:
                d_1 = check_donor_list_names(full_name)
                d_1.add_donation(amount)
                print (d_1.send_thank_you(amount))

def check_donor_list_names(name):
    """Goes through each name in my_dpnors to see if the donor has a history"""
    for i, x in enumerate(my_donors.list_donors):
        if x.name == name:
            return my_donors.list_donors[i]
    else:
        donor_new = dm.Donor(name)
        my_donors.add_donors(donor_new)
        return donor_new

def main():
    switch_func_dict = {
        'a': get_donor_info,
        'b': create_report,
        'c': send_thanks_to_all,
        'd': exit_program
    }
    while True:
        try:
            num = input(prompt)
            switch_func_dict.get(num)()
        except TypeError:
            print ('\nPlease enter in a letter a-d\n')

def exit_program():
    print ('Goodbye')
    exit()

def initialize_donor_dict():
    d1 = dm.Donor('Jeff Bezos')
    d2 = dm.Donor('William Gates, III')
    d3 = dm.Donor('Paul Allen')
    d4 = dm.Donor('Mark Zuckerberg')
    d1.add_donation(1000,400)
    d2.add_donation(100,90)
    d3.add_donation(556,4.9)
    d4.add_donation(1010,400.9, 99900)
    my_donors.add_donors(d1,d2,d3,d4)

prompt = "\n".join(("Please choose from below options:",
          "a - Record a donation",
          "b - Create a report",
          "c - Send a Thank you to all donors",
          "d - Exit",
          ">>> "))

if __name__ == "__main__":
    initialize_donor_dict()
    main()
