"""
Author: Philip Behrend
File: Object-oriented mailroom CLI
Date: 11/8/19
"""

from mailroom_oo import Donor, DonorCollection

def get_name(donor_list):
    """ This function collects user input and returns name variable"""
    donors = [i.name for i in donor_list.donors]
    input_name = input("Type full name: ")
    if input_name == "list":
        print(list(donors))
        return(input_name)
    else:
        return(input_name)

def thank_you(name):
    """Returns a thank-you message to a single donor"""
    return("Esteemed {}, thank you for your generous donation".format(name))

def donation(): 
    """Collects the user's donation input"""
    valid = False
    while not valid:
        try:
            donation_response = round(float(input("Type donation amount: ")),2)
            valid = True
        except ValueError:
            print("Not a valid response. Please input a number.")
    return donation_response

def send_thanks(donor_list):
    """Prints thank-you for a single donor"""
    name_response = 'list'
    while name_response == 'list':
        name_response = get_name(donor_list)
    donor_list.add_donor(name_response)
    print(thank_you(name_response))

def create_report(donor_list):
    """Creates report of metrics: Sum donations, average and total donations"""
    donor_list.donors.sort(reverse=True)
    headers = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
    
    print('{:<16}| {:^14}|{:^14}| {:^14}'.format(*headers))
    print('-'*65)
    for i in donor_list.donors:
        print('{:<18} ${:>12,.2f} {:>14}   ${:>12,.2f}'.format(i.name,i.total_donated,i.avg_donation,i.num_donations))

def send_all_letters(donor_list):
    """Sends letters to each donor"""
    for i in donor_list.donors:
        letter = thank_you(i.name)
        filename = '{}.txt'.format(i.name)
        with open(filename, 'w') as f:
            f.write(letter)

def quit_program(donor_dict):
    return "quit"

if __name__=="__main__":
    donor_list = DonorCollection()
    donor_list.add_donor('henry',50)
    donor_list.add_donor('george',[500,3000])
    donor_list.add_donation('jill',[40,34534,676,788])


    response = 0
    while response != 'quit':
        while response not in [1,2,3,4]:
            response = int(input("1. Send a thank-you to single donor\n2. Create a report\n3. Send Letters\n4. Quit Program\n"))
        
        arg_dict = {1: send_thanks, 2: create_report, 3: send_all_letters, 4: quit_program}
        response = arg_dict.get(response)(donor_list)
