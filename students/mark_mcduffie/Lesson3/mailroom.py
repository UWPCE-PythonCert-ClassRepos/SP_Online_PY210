'''
Mark McDuffie
3/20/19
Mailroom part 1

It should have a data structure that holds a list of your donors and a history of the
amounts they have donated. This structure should be populated at first with at least five donors,
with between 1 and 3 donations each. You can store that data structure in the global namespace.
The script should prompt the user (you) to choose from a menu of 3 actions:
“Send a Thank You”, “Create a Report” or “quit”.
'''
#Original Donor list
#conatins two columns for first and last name, and up to 3 more for donation amounts
donors = [["Jim Johnson", 20000.0, 3500.0, 1600.0],\
          ["Mike Lee", 10000.0, 450.0, 1000.0],\
          ["Joe Smith", 100.0, 50.0],\
          ["Bob Miller", 900.0, 1200.0],\
          ["Steve James", 100000.0]]

#The script should prompt the user (you) to choose from a menu of 3 actions:
#“Send a Thank You”, “Create a Report” or “quit”
def prompt():
    choice = input("You have the following options: \n 1: Send a Thank You \n 2: Create a Report \n 3: Quit \n")
    return choice


#Method that sorts lost based on amount given by each individual
def sort_list(donors):
    from operator import itemgetter             #itemgetter used to define which column is being sorted
    donors.sort(key=itemgetter(1), reverse=True)
    return donors

#Prints a nicely formatted email to donor
def print_email(name, amount):
    print("Dear {},\n \tThank you for your donation of ${:,.2f}. \nYour generosity is greatly appreaciated, we \nlook forward to hearing from you again. \nCheers, \nThe Mailroom".format(name, amount))

#Used in Thank you method, allows us to access just a list of donor names to check
def donor_names():
    for i in donors:
        name = i[0]
        print(name)

#Checks whether the new donor already exists in the list or not
def exists(name):
    for i in donors:
        if name == i[0]:
            return True

#thank you method allows user to add donor and/or donation amount to the list
#Calls other methods print_list, and exists, to show formatted list, and check if donor exists
def thank_you(donors):
    donor = input("Please enter Donor name (first and last), \nor enter 'list' if you want to see the full list of Donors. \n")
    if donor.lower() == 'list':         #shows formatted list if user wants to check
        donor_names()
    else:
        amount = float(input("How much did " + donor + " donate? "))
        if exists(donor):
            for i in donors:            #Appends new amount if donor exits
                i.append(amount)
        else:
            donors.append([donor,amount])       #Appends new donor and amount if donor does not exist
        print_email(donor, amount)              #Method to end official letter once name and donation are entered


#Creates a well formatted report, counting every person's donation and calcuting their average
def report(list):
    print("Donor Name" + " "*16 +"| Total Given | Num Gifts | Average Gift")
    print("-" * 66)
    for i in donors:
        total = 0           # establishes a loop that selects each donor
        name = i[0]         # get donor name
        donations = i[1:]
        for j in donations: # loop inside for loop, this counts each donation for each donor
            total = total + j
        count = len(donations)  # counts the total number of gifts for each donor
        avg = total / count
        print("{:<25} ${:>12.2f}  {:>9d}   ${:>11.2f}".format(name, total, count, avg))


#Main function for interactions
if __name__ == '__main__':
    answer = True
    while (answer == True):
        choice = prompt()
        if choice == '1':
            thank_you(donors)
        elif choice == '2':
            sort_list(donors)
            report(donors)
        elif choice == '3':
            answer = False
        else:
            print("Please select an option number (1,2,3) ")