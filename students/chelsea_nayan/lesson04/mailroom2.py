# chelsea_nayan, UWPCE Python 210, Lesson04: Mailroom, Pt 2
# Dictionary of donors and their donations
donors_dict = {
'Man Mannington': [123234.12, 120000.00, 70000000],
'Soupe Ballinger': [1.00],
'Yufus Lordgagger': [100.00, 200.00, 300.00],
'Prince Variety': [1.50, 2.00],
'Malakai Maitai': [10000000, 300000, 354132]
}

# Prints out a "Thank you" note to a previous or new donor. Updates donation histories.
def thankyou():
    name = input('Please provide a full name. > ')
    while name == 'list': # Prints out the current list of donors when input value = 'list'
        #current = (sublist[0] for sublist in donors)
        for key in donors_dict:
            print(key)
        name = input('Here is a list of current donors. Please provide a full name. > ')

    check = 0
    amount = input('Donation amount: > ')
    # Checks to see if name is on the current donor list
    if name in donors_dict.keys(): # If donor name is on the list, add donation amount to sublist
        donors_dict.get(name).append(float(amount))
        check = 1 # Updates to 'remember' there was a donor name in the list
    if check == 0: # Runs when a donor name was not on the list, adds donor name and amount
        donors_dict[name] = [float(amount)]
    print(f'Thank you {name} for your generous donation of ${float(amount):.2f}.')

# Prints a report on the list of donors sorted by their historical donation amount which includes (1) donor name, (2) total sum of donations, (3) number of donations and (4) average donation ... Do not use dictionaries? This was hard.
def report():

    # This sorts the donor list by the sum of their donations, from highest total to least
    # This makes an iterable of the donor name and then a list of their donations
    sorted_dict = sorted(donors_dict.items(), key=lambda elem: sum(elem[1]), reverse=True)

    # Creates separate lists of the four donation summary columns
    donor_names, total_given, num_gifts, average_gift = [], [], [], []
    for sublist in sorted_dict:
        donor_names.append(sublist[0])
        total_given.append(f"{sum(sublist[1]):.2f}") # Formatted to two decimals
        num_gifts.append(len(sublist[1]))
        average_gift.append(f"{sum(sublist[1])/len(sublist[1]):.2f}")

    # Ensures a list of type string to use string methods
    col1, col2, col3, col4 = [str(i) for i in donor_names], [str(i) for i in total_given], [str(i) for i in num_gifts], [str(i) for i in average_gift]

    # Gets the maximum number of characters in an element in each column to estimate how much spacing there needs to be in the header
    max_donor_names, max_total_given, max_num_gifts, max_average_gift = len(max(col1, key=len)), len(max(col2, key=len)), len(max(col3, key=len))+len("| Num Gifts"), len(max(col4, key=len))

    # Prints out the header for the report
    heading = ("Donor Name".ljust(max_donor_names, ' ') + "|  Total Given ".ljust(max_total_given+3, ' ') + "|  Num Gifts ".ljust(max_num_gifts, ' ')+ "|  Average Gift".ljust(max_average_gift+3, ' '))
    separation = ("-"*len(heading))
    print(heading)
    print(separation)

    # Prints out the rest of the report from most total given to least
    for i in range(len(donor_names)):
        print(f"{donor_names[i].ljust(max_donor_names,' ')}  $ {str(total_given[i]).rjust(max_total_given, ' ')} {str(num_gifts[i]).rjust(max_num_gifts, ' ')}  $ {str(average_gift[i]).rjust(max_average_gift, ' ')} ")

# Generates a thank you letter and writes it to a disk as a text file
def send():
    print('Sending letters...')

    for name in donors_dict.keys():
        amount = sum(donors_dict.get(name))
        txt_name = name.replace(" ", "_")
        output = (f'{txt_name}.txt')
        with open(output, 'w') as f:
               f.write(
f'''Dear {name},

        Thank you for your super, duper total donation of ${float(amount):.2f}.
        I will buy so many things for myself.

            You're the best,
                - Chelsea
''')
    print('Sent the letters!')

if __name__=='__main__': # the interpreter puts this to the top of the module?
    #Prompts the user to one of four actions

    #This is a switch-case dictionary! Note there is no paranthesis after the functions
    arg_dict = {'1': thankyou,
                '2': report,
                '3': send,
                '4': quit
    }

    # A loop to prompt the user for a response
    while True:
        response = input('''
Choose one of four actions:
[1] Send a Thank You
[2] Create a Report
[3] Send letters to everyone
[4] Quit
''')
        arg_dict.get(response)()
