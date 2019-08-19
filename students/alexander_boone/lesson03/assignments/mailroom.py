#!/usr/bin/env python

# global variables
donors = ['Arnold Schwarzenegger', 'Lebron James', 'Elon Musk', 'Walter White', 'Gordon Ramsay']
donations = [100000, 1000000, 2000000, 500000, 1280000]
donation_count = [1, 1, 1, 1, 1]
donor_data = list()
for i in range(len(donors)):
    donor_data.append((donors[i], [donations[i], donation_count[i]]))

# functions

def thank_you():
    """Send a thank you email to the donor."""
    
    print("Who would you like to send a thank you to?")

    # input donor name
    name = 'list'
    while name == 'list':
        name = input("Type 'list' to see a list of names or enter a name: ")
        if name == 'list':
            list_names = list()
            for item in donor_data:
                list_names.append(item[0])
            print(list_names)
        elif not any(name in t for t in donor_data):
            donor_data.append((name, [0, 0]))
            index = donor_data.index((name, [0, 0]))
        else:
            for i in range(len(donor_data)):
                if donor_data[i][0] == name:
                    index = i
                    break

    # enter donation amount
    donation = float(input("Enter a donation amount: "))
    donor_data[index][1][0] += donation
    donor_data[index][1][1] += 1
    
    # write email
    email = f"\nDear {name},\n\nThank you for your generous donation. We are very grateful.\n\nBest,\n\nLocal Charity\n"
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
        donation_avg = donor_data_sorted[i][1][0]/donor_data_sorted[i][1][1]
        print('{:<25}{:^5}${:>14,.2f}{:^5}{:>10}{:^5}${:>14,.2f}'.format(donor_data_sorted[i][0], ' ', donor_data_sorted[i][1][0], ' ', donor_data_sorted[i][1][1], ' ', donation_avg))

    # remain on page until user decides to return to main menu
    q = 'Z'
    while q != 'Q' and q != 'q':
        q = input("\nEnter Q to Quit and return to the main menu: ")
    

# main code
if __name__ == '__main__':

    response = 0
    while response != 3:
        response = 0
        # display main menu with options    
        options = ["1. Send a Thank You", "2. Create a Report", "3. Quit"]
        print(f"----- Main Menu -----\n{options[0]}\n{options[1]}\n{options[2]}")
        
        # get user response
        while int(response) not in [1, 2, 3]:
            response = int(input("Enter a number: "))

        # run function based on response
        if response == 1:
            thank_you()
        elif response == 2:
            create_report()
        else:
            print("Closing the mailroom for the day...")