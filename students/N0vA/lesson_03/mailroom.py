#!/usr/bin/env python3
import sys
#### Mailroom Project Part 1 ####

# Create list of donors and their donation history
database = [('Bill Gates', [2000000, 250000000]), ('Jeff Bezos', [2000000]), ('Elon Musk', [50000000, 10000000]), ('Howard Schultz', [1000000]), ('Paul Allen', [450000000])]

# Send a thank you
def thank_you():
    
    donor_list = database
    print('Alright.  Which donor would you like to send a thank you card?')
    
    while True:
        person = input('Enter their name here or type "list" to see a list of donors: ')
        past_donor = False

        # Print list option
        if person.lower() == 'list':
            past_donor = True
            for per in donor_list:
                print(per[0])

        else:
            for name in donor_list:
                if person.lower() == name[0].lower():
                    past_donor = True

            # Adding a new donor
            if past_donor == False:
                amount_donated = input('How much was their donation? ')
                amount_donated = int(amount_donated)
                new_record = (person, [amount_donated])
                donor_list = donor_list.append(new_record)


            # Write thank you email        
            email = print(f'Dear {person}:\n\n'
                    'On behalf of your Local Charity, I would like to thank you for your generous donation.'
                    'We appreciate your support not only for us but for our cause.\n\n'
                    'We wish you all the best,\n\n'
                    'Local Charity Persident\n')

            email

            # Exit to main menu
            exit = 'fill'
            while exit != 'quit':
                exit = input('Press any button to return to main menu... ')
                main()

# Create a report of donors
def report():

    # Define sort key
    def sort_key(donor):
        return sum(donor[1])

    # Sort Data
    report_data = database
    sorted_data = sorted(report_data, key=sort_key, reverse=True)

    # Format table
    member_row = '{:<24}{:^5} ${:>14,}{:^5} {:^5}{:^5} ${:>14,.2f}'
    print('Generating report of donors....')
    # Header
    print(""+"-" * 80 + "\n Donor Name"+" " * 19 + "| Total Donated | Num Donations | Average Donation\n"+"-" * 80)

    # Print report
    for per in sorted_data:
        print(member_row.format(per[0], ' ', int(sum(per[1])), ' ', round(len(per[1]),2), ' ', round(sum(per[1])/len(per[1]),2)))
    
    # Exit to main menu
    exit = 'none'
    while exit != 'quit':
        exit = input('Press any button to return to main menu... ')
        main()


def main():

    # Opens up the mailroom
    task = 0
    task = input("\n".join(("What do you need to do?",
          "Please choose from the options below:",
          "1 - Send Thank You Card",
          "2 - Print A Report",
          "3 - Exit",
          ">>> ")))

    # Run functions for tasks based on user's response
    if task == '1':
        thank_you()
    elif task == '2':
        report()
    elif task == '3':
        print('Enjoy the rest of your day!')
        sys.exit()
    else:
        print("Not a valid option!")
        main()
        

# Execute file when running
if __name__ == '__main__':
    main()