#!/usr/bin/env python

# global variables
donors = ['Alex Boone', 'Lebron James', 'Elon Musk', 'Walter White', 'Gordon Ramsay']
donations = [100000, 1000000, 2000000, 500000, 1280000]

# functions

def thank_you():
    name = 'list'
    print("Who would you like to send a thank you to?")
    
    # input donor name
    while name == 'list':
        name = input("Type 'list' to see a list of names or enter a name: ")
        if name == 'list':
            print(donors)
        elif name not in donors:
            donors.append(name)
            donations.append(0)
            index = donors.index(name)
        else:
            index = donors.index(name)

    # enter donation amount
    donation = int(input("Enter a donation amount: "))
    donations[index] += donation
    
    # write email
    email = f"\nDear {name},\n\nThank you for your generous donation. We are very grateful.\n\nBest,\n\nLocal Charity\n"
    print(email)


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
            print("TODO")
        else:
            print("Closing program...")