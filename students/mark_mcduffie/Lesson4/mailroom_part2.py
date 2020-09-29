'''
Mark McDuffie
3/20/19
Mailroom part 2

It should have a data structure that holds a list of your donors and a history of the
amounts they have donated. This structure should be populated at first with at least five donors,
with between 1 and 3 donations each. You can store that data structure in the global namespace.
The script should prompt the user (you) to choose from a menu of 3 actions:
“Send a Thank You”, “Create a Report” or “quit”.

*edited from mailroom part 1, uses dicts where appropriate
'''

#Original Donor list, used and added upon in the program
#conatins two columns for first and last name, and up to 3 more for donation amounts
donors = {
          "Jim Johnson": [20000.0, 3500.0, 1600.0],
          "Mike Lee": [10000.0, 450.0, 1000.0],
          "Joe Smith": [100.0, 50.0],
          "Bob Miller": [900.0, 1200.0],
          "Steve James": [100000.0]
          }

#The script should prompt the user (you) to choose from a menu of 3 actions:
#“Send a Thank You”, “Create a Report” or “quit”
def prompt():
    choice = input("You have the following options: \n 1: Send a Thank You \n 2: Send Letters to all Donors "
                   "\n 3: Create a Report \n 4: Quit \n")
    return choice

#Prints a nicely formatted email to donor
def print_email(name, amount):
    print("Dear {},\n \tThank you for your donation of ${:,.2f}. \nYour generosity is greatly appreaciated, "
          "we \nlook forward to hearing from you again. \nCheers, \nThe Mailroom".format(name, amount))

#Used in Thank you method, allows us to access just a list of donor names to check
def donor_names(donors):
    for key in donors.keys():
        name = key
        print(name)

#Checks whether the new donor already exists in the list or not
def exists(name):
    for i in donors:
        if name == i[0]:
            return True

#thank you method allows user to add donor and/or donation amount to the list
#Calls other methods print_list, and exists, to show formatted list, and check if donor exists
def single_thank_you():
    donor = input("Please enter Donor name (first and last), \nor enter 'list' if you want to see the full list of Donors. \n")
    if donor.lower() == 'list':         #shows formatted list if user wants to check
        donor_names(donors)
    else:
        amount = float(input("How much did " + donor + " donate? "))
        if donor in donors:
            donors[donor].append(amount)
        else:
            donors[donor] = [amount]      #Appends new donor and amount if donor does not exist
        print_email(donor, amount)  #Method to end official letter once name and donation are entered
    return main()

#Sends a thank you to ever donor on the list, creating individual text files
def send_all():
    import os
    recipients = []
    for item in donors.items():
        recipients.append({'name': item[0], 'total': str(sum(item[1]))})
    for recipient_name in recipients:
        with open('{name}.txt'.format(**recipient_name), 'w') as f:
            f.write("Dear {name},\n \tThank you for your donation of ${total}. "
                    "\nYour generosity is greatly appreaciated, we \nlook forward to hearing from you again. "
                    "\nCheers, \nThe Mailroom".format(**recipient_name))
    print("Letter were created and are in the {} directory.".format(os.getcwd()))
#Creates a well formatted report, counting every person's donation and calcuting their average
def report():
    import operator
    for (value) in donors.values(): #sorts list based on amount given by each individual
        total = 0
        for i in value:
            total = total + i
        value = total
    sorted_donors = sorted(donors.items(), key=operator.itemgetter(1), reverse=True)
    print("Donor Name" + " "*16 +"| Total Given | Num Gifts | Average Gift")
    print("-" * 66)
    for i in sorted_donors:
        name = i[0]
        total = sum(i[1])           # adds all donations for each name
        count = len(i[1])           # counts the total number of gifts for each donor
        avg = total / count
        print("{:<25} ${:>12.2f}  {:>9d}   ${:>11.2f}".format(name, total, count, avg))
    return main()

#Main function for interactions
def main():
   while True:
        choice = int(prompt())
        choice_Dict = {
            1: single_thank_you,
            2: send_all,
            3: report,
            4: quit
        }
        if choice in choice_Dict:
            choice_Dict.get(int(choice))()
        else:
            print("Please enter a choice number between 1 and 4")


if __name__ == '__main__':
    main()