# chelsea_nayan, UWPCE Python 210
#Lesson09: Object-Oriented Mailroom (Command Line Interface, AKA CLI)

"""
Includes all user interaction functions and main program flow
"""
import sys # Use to quit out of menu
from mailroom_oo import Donor
from mailroom_oo import DonorCollection as DC

donors = DC.initial_donors = {
'Man Mannington': [123234.12, 120000.00, 70000000],
'Soupe Ballinger': [1.00],
'Yufus Lordgagger': [100.00, 200.00, 300.00],
'Prince Variety': [1.50, 2.00],
'Malakai Maitai': [10000000, 300000, 354132]
}

# ------------ Send a Thank You ---------------- #

def list_thankyou():
    name = input("Please provide a full name. Type 'list' if you want a current list of donors. > ")
    while name == 'list': # Print out the current list of donors when input value = 'list'
        for key in donors:
            print(key)
        name = input('Here is a list of current donors. Please provide a full name. > ')
    return name

# Update the donation amount for the donor
def update_thankyou():
    amount = input('Donation amount: > ')
    while not isinstance(amount, float):
        try:
            amount = float(amount)
        except ValueError:
            amount = input("Please enter in a number for the donation. > ")
            continue
    return amount

# Send a thank you to the donor
def check_thankyou(name, amount): # Check to see if name is on the current donor list
    check = 0
    if name in donors.keys(): # If donor name is on the 'list', add donation amount to value
        donors.get(name).append(float(amount))
        check = 1 # Update to 'remember' there was a donor name in the list
    if check == 0: # Run when a donor name was not on the list, add donor name and amount
        donor = Donor(name, amount)
        name.add_donation(float(amount))
        # donors[name] = [float(amount)]
    pair = [name, amount]
    return pair

# Generate thank you note
def note_thankyou(pair):
    text = (f'Thank you {pair[0]} for your generous donation of ${float(pair[1]):.2f}.')
    return text

# Print out a "Thank you" note to a previous or new donor.
def thankyou():
    print(note_thankyou(check_thankyou(list_thankyou(), update_thankyou())))


# ------------ Create a Report ---------------- #

# Calculate the maximum lengths of each column for spacing considerations
def setup_report(donor_names, total_given, num_gifts, average_gift):
    col1, col2, col3, col4 = [str(i) for i in donor_names], [str(i) for i in total_given], [str(i) for i in num_gifts], [str(i) for i in average_gift]
    # Get the maximum number of characters in an element in each column to estimate how much spacing there needs to be in the header
    max_donor_names, max_total_given, max_num_gifts, max_average_gift = len(max(col1, key=len)), len(max(col2, key=len)), len(max(col3, key=len))+len("| Num Gifts"), len(max(col4, key=len))
    dataset = [max_donor_names, max_total_given, max_num_gifts, max_average_gift]
    return dataset

# Print the header
def header_report(dataset):
    heading = ("Donor Name".ljust(dataset[0], ' ') + "|  Total Given ".ljust(dataset[1]+3, ' ') + "|  Num Gifts ".ljust(dataset[2], ' ')+ "|  Average Gift".ljust(dataset[3]+3, ' '))
    separation = ("-"*len(heading))
    header = heading +  "\n" + separation
    return header

# Sort the donor list by the sum of their donations, from highest total to least
# Make an iterable of the donor name and then a list of their donations
def sort_report(donors):
    sorted_dict = sorted(donors.items(), key=lambda elem: sum(elem[1]), reverse=True)
    return sorted_dict

def report():
    # Sort donor list by sum of their donations (high to low)
    sort_report(donors)

    # Create separate lists of the four donation summary columns
    donor_names, total_given, num_gifts, average_gift = [], [], [], []
    for sublist in sort_report(donors):
        donor_names.append(sublist[0])
        total_given.append(f"{sum(sublist[1]):.2f}") # Format to two decimals
        num_gifts.append(len(sublist[1]))
        average_gift.append(f"{sum(sublist[1])/len(sublist[1]):.2f}") # Format to two decimals

    dataset = setup_report(donor_names, total_given, num_gifts, average_gift)

    # Print the header
    print(header_report(dataset))

    # Print the summary tables
    for i in range(len(donor_names)):
        print(f"{donor_names[i].ljust(dataset[0],' ')}  $ {str(total_given[i]).rjust(dataset[1], ' ')} {str(num_gifts[i]).rjust(dataset[2], ' ')}  $ {str(average_gift[i]).rjust(dataset[3], ' ')} ")

# ------------ Send letters to everyone ---------------- #

def text_send(name, amount):
    text = f'''
    Dear {name},

        Thank you for your super, duper total donation of ${float(amount):.2f}.
        I will buy so many things for myself.

            You're the best,
                - Chelsea
    '''
    return text

# Generate a thank you letter and write it to a disk as a text file
def send():
    print('\nSending letters...')

    for name in donors.keys():
        amount = sum(donors.get(name))
        txt_name = name.replace(" ", "_")
        output = (f'{txt_name}.txt')
        with open(output, 'w') as f:
            f.write(text_send(name, amount))

    print('\nSent the letters!')

# ------------ Quit ---------------- #

# Exit the program
def quit():
    print("See ya later, gater!")
    sys.exit(0)


# ------------ Run the Main Program ---------------- #

if __name__=='__main__':

    # Switch
    arg_dict = {1: thankyou,
                2: report,
                3: send,
                4: quit
    }

    # A loop to prompt the user for a response of one of four options
    while True:
        response = input('''
    Choose one of four actions:
    [1] Send a Thank You
    [2] Create a Report
    [3] Send letters to everyone
    [4] Quit
    ''')
        try:
            response = int(response)
        except ValueError:
            print("Input must be an integer from 1-4, please try again.")
            continue
        arg_dict.get(response)() # Execute the method if possible!
