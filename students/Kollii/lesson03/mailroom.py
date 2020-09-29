# Mailroom PART - 1
import sys

donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ]

def options_menu():
    print("\n".join(("Welcome to the XYZ Charity!",
          "Please choose from below options:",
          "1 - Send a Thank you Note",
          "2 - Create a Report",
          "3 - Quit",
          ">>> ")))
    option = input('')
    return option

def find_name(donor_name):
    for name in donor_db:
        if donor_name.lower() == name[0].lower():
            return name
    return None

   
def send_thankyou():
    output = input ("Enter the donor's FULL NAME "
                        "or 'List' - to see ALL Donors Names)> ")

    while output.lower() == "list":
        for names in donor_db:
            print(names[0])
        output = input ("Please enter a  FULL Name ")
                        
    donor= find_name(output)
    if donor is None:
        donor = (output,[])
        donor_db.append(donor)
    
    donation_Amt = float(input ("Enter the Amount for donation "))
    donor[1].append(float(donation_Amt))

    print_thankyou(output, donation_Amt)    

def print_thankyou(name, amount):
    print(f'\nDear {name.title()},')
    print(f'Thank you for your generous donation of ${amount:,.2f}' +
          '\nWe appreciate your support.' +
          '\n\nRegards,\nXYZ Charity Team\n')      

def create_report():
    """Generate a tabular report of donation history"""

    header ='\n{:<18}|{:^13}|{:^13}|{:>13}'.format("Donor Name", "Total Given",
                                                   "Num Gifts", "Average Gift")
    print("XYZ Charity: Donation history report")
    print(header)
    print('-'*len(header))
    donor_sort = sorted(donor_db, key = sort_key, reverse = True)
    for entry in donor_sort:
        total = sum(entry[1])
        num = len(entry[1])
        average = total/num
        print('{:<18} ${:>12,.2f}{:>13}  ${:>12,.2f}'.format(entry[0],total,num,average))
    print('')

def sort_key(entry):
    return sum(entry[1])


def quit_menu():
    print("Good bye")
    sys.exit()

def main_menu():
    while True:
        option = options_menu()
        if option == '1':
            send_thankyou()
        elif option == '2':
            create_report()
        elif option == '3':
            quit_menu()
        else: 
           print("Not a valid option. Please select a valid option")

if __name__ == "__main__":
    main_menu()
