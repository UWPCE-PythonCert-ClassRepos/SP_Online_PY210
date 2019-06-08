#Opening prompt function
def opening_screen():
    #Tell the user what their options are. Ask for an input.
    print('')
    print('Welcome to the mailroom tool. Please select an action:')
    print('1. Send a Thank You')
    print('2. Create a Report')
    print('3. Quit')
    #Send user input back to main function to be analyzed.
    return input()

#'Send thank you' function
def send_thank_you(donor_names, donor_amounts):
    #Ask for a donor's name. If user requests 'list', display existing donors and request action agin.
    while True:
        name = input("Please enter a donor's name to thank (List to see existing donors, Quit to exit): ").title()
        if name == 'List':
            for donor in donor_names:
                print(donor)
        #When user inputs something besides list, pass it on.
        else:
            break
    #If user entered 'quit', skip all this
    if name != 'Quit':
        #Ask the donor's donation amount
        amount = float(input("Please enter donation amount: "))
        #If an existing donor, add the amount to the end of their previous list.
        if name.title() in donor_names:
            donor_amounts[donor_names.index(name)].append(amount)
        #If new donor, add their name to donor list and add the donation amount.
        else:
            donor_names.append(name)
            donor_amounts.append([amount])

        #Write the message, using the donor's name and amount.
        print(f'Dear {name},')
        print('    We would like to thank you for your gracious donation of ${:.2f}.'.format(amount))
        print('                      Sincerely, this non-profit')

#Create report function
def create_report(donor_names, donor_amounts):
    #Header
    print('{:<20} | {:^10} | {:^10} | {:>15}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print ('-'*65)
    donor_info = []
    #Count donor's number of donations and calculate total donation.
    for i, name in enumerate(donor_names):
        total = sum(donor_amounts[i])
        number = len(donor_amounts[i])
        average = total/number
        #Create a list of donor history and information
        donor_info.append([total, number, average, name])
    #Sort the list by the first value (Total Gift)
    donor_info = sorted(donor_info,reverse=True)
    # Display each donor's name and information. Controlled for format
    for i in range(len(donor_info)):
        print('{:<20} $ {:>10.2f}   {:>10} $ {:>15.2f}'.format(donor_info[i][3], donor_info[i][0], donor_info[i][1], donor_info[i][2]))

#Main function
if __name__ == '__main__':
    #Establish existing donor list
    donor_information = [["Bill Gates", 345678, 454540], ["Mark Zuckerberg", 6487, 4978,5487,1678], ["Jeff Bezos", 842], ["Paul Allen", 425, 3523], ["Kanye West", 4, 1235234]]
    #Declare donor names and amounts as separate lists
    donor_names = []
    donor_amounts = []
    #Break donor information into names and amounts lists
    for donor in donor_information:
        donor_names.append(donor[0])
        donor_amounts.append(donor[1:])

    #Prompt the user to do something. Stay here unless user selects a quit item.
    while True:
        #Call the opening screen function
        user_selection = opening_screen().lower()
        #Analyze responses and call related function or quit.
        if user_selection == '1' or user_selection == 'send a thank you':
            send_thank_you(donor_names, donor_amounts)
        elif user_selection == '2' or user_selection == 'create a report':
            create_report(donor_names, donor_amounts)
        elif user_selection == '3' or user_selection == 'quit':
            break
        #If user input does not match, just ask again
        else:
            pass