#!/usr/bin/env python3

import sys

donors = [("Bill Gates", [653772.32, 12.17]),
          ("Jeff Bezos", [877.33]),
          ("Paul Allen", [663.23, 43.87, 1.32]),
          ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
          ("Tim Cook", [1563.32, 8976.54])]

prompt = "\n".join(("Welcome to the mailroom!",
          "Please choose from below options:",
          "1 - Send a thank you",
          "2 - Create a report",
          "3 - Quit",
          ">>> "))


def donor_list():
    """Returns a list of the donor names from donors"""
    donor_names = [i[0] for i in donors]
    return donor_names
    

def add_donation(name, donation):
    """
    Appends the donation to the donation list, or adds a new donor and donation
    
    Parameters:
    name(str): name of the donor
    donation(int): value of the donation
    
    """
    
    #this is a placeholder for the index of an existing donor
    ind = -1
    
    #find the index of a donor, if user selects an existing donor
    for i in donors:
        if name in i:
            ind = donors.index(i)
            
    #if donor exists (index>=0), append to the donation list in the tuple. If new, add a new donor and donation        
    if ind >= 0:
        donors[ind][1].append(donation)
    else:
        donors.append((name,[donation]))
            
          
            


def thankyou_email(name, donation):
    """Prints the letter with the user inputted name and donation """

    print("""
    Dear {},
    Thank you very much for the generous donation of ${:,.2f}
    It is very much appreciated. 
    Respectfully,
        
    Eric G.
    """.format(name, donation))


def thank_you():
    """
    Asks user for a name, list of donors, or to quit.
    If a name, prompts user for a donation and prints 
    the thank you email
    
    """
    
    while True:
        thanks = input("Please enter full name, type 'list' to see all names, or enter 'q' to quit: ").title()
        if thanks == 'Q':
            break
        elif thanks == 'List':
            print(donor_list())
        else:
            donation = input("Please enter in a donation, or 'q' to quit: ")
            if donation == "q":
                break
            else:
                add_donation(thanks, int(donation))
                thankyou_email(thanks, int(donation))
                #print(donors)
                break

  

def sort_key(items):
    """Sort key for the sorted list in create report"""
    return items[1]

def create_report():
    """
    Creates a formatted and aligned report of each donor,
    total given, number of gifts, and average gift, sorted
    by total given (large to small)

    """

    new_list = []
    for i in range(len(donors)):
        sum_don = sum(donors[i][1])
        len_don = len(donors[i][1])
        average = sum_don/len_don
        new_list.append([donors[i][0], sum_don, len_don, average])
    sorted_list = sorted(new_list, key=sort_key, reverse=True)
    print()
    print("{:<25s}|{:>15s} |{:>10s} | {:>12s}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print(68 * '-')
    for x in sorted_list:
        print("{:<25s}|${:>14.2f} |{:>10.0f} |${:>12.2f}".format(*x))
    print()

def exit_program():
    print("Good Bye")
    sys.exit()

def main():
    """Controls flow of program; prompts user for selection and breaks if quit"""
    while True:
        response = input(prompt)
        if response == '1':
            thank_you()
        elif response == '2':
            create_report()
        elif response == '3':
            exit_program()


if __name__ == "__main__":
    main()


