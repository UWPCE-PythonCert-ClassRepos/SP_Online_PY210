'''This program is the command line interface for the donor class'''

import donor_models as d

'''Strings for the CLI inputs'''
action_input = 'Choose an action: \n\n1 - Send a Thank You to a single donor.' +
               ' \n2 - Create a Report. \n3 - Send letters to all donors. \n4 - Quit \n> '
name_input = 'What is the full name > '
donation_input = 'What is the donation amount > '
rename_input = 'Name is not in Donors list. Are you sure you want to add? > '

'''Initializes a list of donors in the donor collection'''
donor_list = d.DonorCollection(d.Donor('Alan', 234.32, 23433.93, 46480.43),
                               d.Donor('Ben', 565.34, 233905.49),
                               d.Donor('Charlie', 213820.43),
                               d.Donor('Dan', 238924.23, 970597.44, 291.49),
                               d.Donor('Eddy', 1830.32, 2084.49))


def writeonedonor():
    '''Function to send thank you to single donor'''
    name = input(name_input)
    #Keeps looping until list isn't selected
    while name == 'list':
        print(donor_list.donor_names)
        name = input(name_input)
    #Checks name for donor list. If it isn't there, it prompts user to make sure they want to add donor
    if name not in donor_list.donor_names:
        name_prompt = ''
        while name_prompt.lower() != 'yes' and name_prompt.lower() != 'no':
            name_prompt = input(rename_input)
            if name_prompt.lower() == 'yes':
                donor_list.add_donor(name)
            elif name_prompt.lower() == 'no':
                print('Type another name\n')
                return writeonedonor()
            else:
                print('Invalid response, type yes or no\n')
    #Prompts for donation
    donation = input(donation_input)
    #Gets donor in collection
    new_donor = donor_list.get_donor(name)
    #Adds donations to donor
    new_donor.add_donation(donation)
    new_donor.write_donor()

'''Creates report for all donors'''
def createareport():
    print(donor_list.report)

'''Writes to all donors'''
def writealldonors():
    donor_list.write_donors()

def quit():
    '''Quits the program'''
    print('Quitting this menu\n')
    return 'exit menu'

def main_response(action, dictionary):
    '''Invokes the script'''
    while True:
        #Error handle will loop until input is valid
        try:
            response = input(action)
            if dictionary[response]() == 'exit menu':
                break
        except KeyError:
            print('\nInvalid input, try again\n')

'''User choices'''
response_dict = {'1': writeonedonor, '2': createareport, '3': writealldonors, '4': quit}

'''Main interation'''
if __name__ == '__main__':
    main_response(action_input, response_dict)