#!/usr/bin/env python

# global variables

# prepare initial data structure for donor data
donors = [{'first_name': 'Arnold', 'last_name': 'Schwarzenegger'}, {'first_name': 'Lebron', 'last_name': 'James'}, {'first_name': 'Elon', 'last_name': 'Musk'}, {'first_name': 'Walter', 'last_name': 'White'}, {'first_name': 'Gordon', 'last_name': 'Ramsay'}]
donations = [100000, 1000000, 2000000, 500000, 1280000]
donation_count = [1, 1, 1, 1, 1]
donor_data = list()
for i in range(len(donors)):
    donor_data.append((donors[i], [donations[i], donation_count[i]]))

# Note: donor_data is a LIST of TUPLES with each tuple containing (dict of first/last name, [donation total, donation count])

# functions

def thank_you():
    """Send a thank you email to the donor."""
    
    print("Who would you like to send a thank you to?")

    # input donor name
    name = 'list'
    while name == 'list':
        name = input("Type 'list' to see a list of names or enter a name: ")

        # run if user inputs 'list'
        if name == 'list':
            list_names = list()
            for item in donor_data:
                list_names.append(item[0]['first_name'] + ' ' + item[0]['last_name'])
            print(list_names)
        # run if name that user inputs is not already in the donor list
        elif not any({'first_name': name.split(' ')[0], 'last_name':name.split(' ')[1]} in t for t in donor_data):
            firstName = name.split(' ')[0]
            lastName = name.split(' ')[1]
            donor_data.append(({'first_name': firstName,'last_name':lastName}, [0, 0]))
            index = len(donor_data) - 1
        # run if name that user inputs is already in the donor list
        else:
            firstName = name.split(' ')[0]
            lastName = name.split(' ')[1]
            for i in range(len(donor_data)):
                if donor_data[i][0]['first_name'] == firstName and donor_data[i][0]['last_name'] == lastName:
                    index = i
                    break

    # enter donation amount
    donation = float(input("Enter a donation amount: "))
    donor_data[index][1][0] += donation
    donor_data[index][1][1] += 1
    
    # write email (using formatted dict values)
    email = "\nDear {first_name} {last_name},\n\nThank you for your generous donation. We are very grateful.\n\nBest,\n\nLocal Charity\n".format(**donor_data[index][0])
    print(email)

def create_report():
    """Create a report of donor data, including total donated, number of donations, and average donation amount."""
    
    # create table heading
    report_headers = '{:<25}{:^5}{:<15}{:^5}{:<10}{:^5}{:<15}'.format('Donor Name', '|', 'Total Given', '|', 'Num Gifts', '|', 'Average Gift')
    table_divider = '-' * 71
    print('\n', report_headers)
    print(table_divider)

    # sort donor data by donations
    def sort_key(donation_data_tup):
        return donation_data_tup[1][0]

    donor_data_sorted = sorted(donor_data, key = sort_key, reverse = True)

    # print donor data
    for i in range(len(donor_data_sorted)):
        firstName = donor_data_sorted[i][0]['first_name']
        lastName = donor_data_sorted[i][0]['last_name']
        donation_avg = donor_data_sorted[i][1][0]/donor_data_sorted[i][1][1]
        print('{:<25}{:^5}${:>14,.2f}{:^5}{:>10}{:^5}${:>14,.2f}'.format(firstName + ' ' + lastName, ' ', donor_data_sorted[i][1][0], ' ', donor_data_sorted[i][1][1], ' ', donation_avg))

    # remain on page until user decides to return to main menu
    q = 'Z'
    while q != 'Q' and q != 'q':
        q = input("\nEnter Q to Quit and return to the main menu: ")
    
def letters_to_all():
    '''Write a letter to every donor and save each one to a file on the disk.'''
    


# main code
if __name__ == '__main__':

    exit_message = "Closing the mailroom for the day..."
    response_dict = {1:thank_you, 2:create_report, 3:letters_to_all, 4:exit}
    response = 0
    while response != 3:
        response = 0
        # display main menu with options    
        options = ["1. Send a Thank You to a single donor", "2. Create a Report", "3. Send letters to all donors", "4. Quit"]
        print(f"----- Main Menu -----\n{options[0]}\n{options[1]}\n{options[2]}\n{options[3]}")
        
        # get and run user response
        while int(response) not in [1, 2, 3, 4]:
            response = int(input("Enter a number: "))
        if response == 4:
            print(exit_message)
        response_dict.get(response)()