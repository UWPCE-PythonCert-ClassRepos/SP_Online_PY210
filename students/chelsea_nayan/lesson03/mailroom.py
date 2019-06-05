# chelsea_nayan, UWPCE Python 210, Lesson03: Mailroom Pt

# Lists of donors and their donations
donors = [
['Man Mannington', 123234.12, 120000.00, 70000000],
['Soupe Ballinger', 1.00],
['Yufus Lordgagger', 100.00, 200.00, 300.00],
['Prince Variety', 1.50, 2.00],
['Malakai Maitai', 10000000, 300000, 354132]
]

# Prints out a "Thank you" note to a previous or new donor. Updates donation histories.
def thankyou():
    name = input('Please provide a full name. > ')
    check = 0
    while name == 'list': # Prints out the current list of donors when input value = 'list'
        #current = (sublist[0] for sublist in donors)
        for sublist in donors:
            print(sublist[0])
        name = input('Here is a list of current donors. Please provide a full name. > ')
    for sublist in donors: # Checks to see if name is on the current donor list
        if sublist[0] == name: # If donor name is on the list, add donation amount to sublist
            amount = input('Donation amount: > ')
            sublist.append(float(amount))
            check = 1 # Updates to 'remember' there was a donor name in the list
            break
    if check == 0: # Runs when a donor name was not on the list, adds donor name and amount
        amount = input('Donation amount: > ')
        donors.append([name, float(amount)])
    print(f'Thank you {name} for your generous donation of ${float(amount):.2f}.')


# Prints a report on the list of donors sorted by their historical donation amount which includes (1) donor name, (2) total sum of donations, (3) number of donations and (4) average donation ... Do not use dictionaries? This was hard.
def report():

    # This sorts the donor list by the sum of their donations, from highest total to least
    def getTotal(element):
        return sum(element[1:])
    donors.sort(key=getTotal, reverse=True)
    print(donors)

    # Creates separate lists of the four donation summary columns
    donor_names, total_given, num_gifts, average_gift = [], [], [], []
    for sublist in donors:
        donor_names.append(sublist[0])
        total_given.append(f"{(sum((sublist[1:]))):.2f}") # Formatted to two decimals
        num_gifts.append((len(sublist)-1))
        average_gift.append(f"{(sum(sublist[1:])/(len(sublist)-1)):.2f}")

    # Ensures a list of type string to use string methods
    col1, col2, col3, col4 = [str(i) for i in donor_names], [str(i) for i in total_given], [str(i) for i in num_gifts], [str(i) for i in average_gift]

    # Gets the maximum number of characters in an element in each column to estimate how much spacing there needs to be in the header
    max_donor_names, max_total_given, max_num_gifts, max_average_gift = len(max(col1, key=len)), len(max(col2, key=len)), len(max(col3, key=len))+len("| Num Gifts"), len(max(col4, key=len))

    print(max_donor_names, max_total_given, max_num_gifts, max_average_gift)

    # Prints out the header for the report
    heading = ("Donor Name".ljust(max_donor_names, ' ') + "|  Total Given ".ljust(max_total_given+3, ' ') + "|  Num Gifts ".ljust(max_num_gifts, ' ')+ "|  Average Gift".ljust(max_average_gift+3, ' '))
    separation = ("-"*len(heading))
    print(heading)
    print(separation)

    # Prints out the rest of the report from most total given to least
    for i in range(len(donor_names)):
        print(f"{donor_names[i].ljust(max_donor_names,' ')}  $ {str(total_given[i]).rjust(max_total_given, ' ')} {str(num_gifts[i]).rjust(max_num_gifts, ' ')}  $ {str(average_gift[i]).rjust(max_average_gift, ' ')} ")

if __name__=='__main__': # the interpreter puts this to the top of the module?
    #Prompts the user to one of three actions
    while True:
        response = input('''
Choose one of three actions:
[1] Send a Thank You
[2] Create a Report
[3] Quit
''')
        if response == '1':
            thankyou()
        elif response == '2':
            report()
        elif response == '3':
            quit()
