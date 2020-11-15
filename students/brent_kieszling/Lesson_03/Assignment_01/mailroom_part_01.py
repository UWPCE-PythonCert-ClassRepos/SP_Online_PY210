#-------------------------------------------#
#Tittle: mailroom_part_01, PYTHON210 - Assignment 01
#Desc: Mailroom Part 1
#Change Log: (Who, When, What)
#Brent Kieszling, <2020-Nov-8>, created file and developed print_,menu
#Brent Kieszling, <2020-Nov-10>, developed: update_donors, display_donors, and thank_you
#Brent Kieszling, <2020-Nov-11>, finished remaining functions, tested options 1-3
#-------------------------------------------#

#DATA---------------------------------------


person_1 = ["William Gates, III", 23000.00, 23000.00]
person_2 = ["Mark Zuckerberg", 30000.00]
person_3 = ["Jeff Bezos", 20000.00, 20000.00]
person_4 = ["Paul Allen", 22000.00, 22000.00]
person_5 = ["Scrooge McDuck", 3245649.03, 1234567.89, 11.01]
person_6 = ['Cher', 1337101.00]
lst_donors = [person_1, person_2, person_3, person_4, person_5, person_6]


#PROCESS------------------------------------
def print_menu():
    """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
    """
    print("Main Menu\n\n[1] Send a thank you letter.\n[2] Create a report.\n[3] Exit program.")

def update_donors(lst_group, person, money):
    """Update a list of donors with a new donation
    
        Args:
            lst_group(list): List of lists containing donors and their contribution.
            person(str): Name of donor.
            money(float): Most recent donation.
            
        Returns:
            lst_group(list): Updated list of donors.
    """
    check_new = 0
    for item in lst_group:
        if item[0] == person:
            item.append(money)
            check_new +=1
    #Add new donor if not found in current list
    if check_new == 0:
        new_donor = [person, money]
        lst_group.append(new_donor)
    return lst_group
    

def thank_you(lst_person):
    """Display a thank you letter for a donor.
    
        Args:
            lst_person(list): List containing a donor and their donations.
            
        Returns:
            letter(str): Thank you letter for a donor.
    """
    letter = """
    Dear {donor},
    
    Thank you for your most recent donation of {last:.2f}. We are humbled by your 
    lifetime contribution of {total:.2f}.
    
    Sincerly,
    Making Good Things Happen"""
    return letter.format(donor = lst_person[0], last = lst_person[-1], total = sum(lst_person[1:]))
    
def find_donor(lst_group, person):
    """Update a list of donors with a new donation
    
        Args:
            lst_group(list): List of lists containing donors and their contribution.
            person(str): Name of donor.
            
        Returns:
            lst_person(list): List containing a donor and their donations.
    """
    for item in lst_group:
        if person == item[0]:
            lst_person = item
            return lst_person

def display_donors(lst_group):
    """Display all donors on record.
    
        Args:
            lst_person(list): List containing a donor and their donations.
            
        Returns:
            None
    """
    print("Current donors are:")
    for item in lst_group:
        print(item[0])

def display_report(lst_people):
    """Format a list of lists containing donor metrics.
    
    Args:
        lst_people (list): List of lists containing a donor's name, total
            contribution, number of contributions, and anverage contribution.
        
    Returns:
        None
    """
    
    formatted_header = "{name:<20} | {total:<10} | {gifts:<9} | {average:<10}"
    formatted_row = "{:<20} $ {:<10.2f}   {:^9}  $ {:>10.2f}"

    print('==================== Donor Report: ==========================')
    print(formatted_header.format( name = "Donor Name", total = "Total Given",\
                                  gifts = "Num Gifts", average = "Average Gift"))
    print('-------------------------------------------------------------')
    for item in lst_people:
        print(formatted_row.format(*item))
    print('==============================================================')
    print()

def donor_stats(lst_group):
    """Create list of lists containing key donor stats.
    
        Args:
            lst_group(list): List of lists containing donors and their contribution.
        
        Returns:
            lst_stats(list): List of lists containing a donor's name, total
                contribution, number of contributions, and average contribution.
    """
    lst_stats = []
    for item in lst_group:
        name = item[0]
        total = sum(item[1:])
        number_contributions = len(item)-1
        average = total/number_contributions
        donor_stats = [name, total, number_contributions, average]
        lst_stats.append(donor_stats)
    #Sort lst_stats in reverse order using the inner list value at position 1 (total)
    lst_stats.sort(reverse = True, key = lambda x: x[1])
    return lst_stats


#PRESENTATION INPUT/OUTPUT------------------

if __name__ == '__main__':
    while True:
        print_menu()
        choice = int(input("Please select from 1, 2, or 3: "))
        
        #[3] Exit program
        if choice == 3:
            break
        
        #[1] Write thank you
        elif choice == 1:
            while True:
                name = input("Please enter a name to create a thank you letter. To see current donors type 'list'.\n")
                print()
                if name == 'list':
                    display_donors(lst_donors)
                    print()
                else:
                    donation = float(input("Enter the new donation ammount: "))
                    #Add new donation to active list of donors.
                    lst_donors = update_donors(lst_donors, name, donation)
                    #Retrieve individual's donation history
                    donor = find_donor(lst_donors, name)
                    #Display thank you
                    print(thank_you(donor))
                    print()
                    break
            
        #Display report
        elif choice == 2:
            #Retrive donor stats
            donor_info = donor_stats(lst_donors)
            display_report(donor_info)
            
        else:
            print("That is not a valid option.")



