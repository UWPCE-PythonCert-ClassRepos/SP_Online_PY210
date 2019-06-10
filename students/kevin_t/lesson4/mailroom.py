#Opening prompt function
def opening_screen():
    #Tell the user what their options are. Ask for an input.
    print('')
    print('Welcome to the mailroom tool. Please select an action:')
    print('1 - Send a Thank You')
    print('2 - Create a Report')
    print('3 - Send letters to all donors')
    print('4 - Quit')
    #Send user input back to main function to be analyzed.
    return input()

#'Send thank you' function
def send_thank_you(donor_info):
    #Ask for a donor's name. If user requests 'list', display existing donors and request action agin.
    while True:
        name = input("Please enter a donor's name to thank (List to see existing donors, Quit to exit): ").title()
        if name == 'List':
            for donor in donor_info:
                print(donor)
        #When user inputs something besides list, pass it on.
        else:
            break
    #If user entered 'quit', skip all this
    if name != 'Quit':
        #Ask the donor's donation amount
        amount = float(input("Please enter donation amount: "))
        #If an existing donor, add the amount to the end of their previous list.
        if name in donor_info:
            donor_info[name].append(amount)
        #If new donor, add their name to donor list and add the donation amount.
        else:
            donor_info[name] = [amount]

        #Write the message, using the donor's name and amount.
        print(f'Dear {name},')
        print('    We would like to thank you for your gracious donation of ${:.2f}.'.format(amount))
        print('                      Sincerely, this non-profit')

#Create report function
def create_report(donor_info):
    #Header
    print('{:<20} | {:^10} | {:^10} | {:>15}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print ('-'*65)
    donor_report = []
    #Count donor's number of donations and calculate total donation.
    for name in donor_info:
        total = float(sum(donor_info[name]))
        number = len(donor_info[name])
        average = total/number

        #Create a list of donor history and information
        donor_report.append([total, number, average, name])

    #Sort the list by the first value (Total Gift)
    donor_report = sorted(donor_report,reverse=True)

    # Display each donor's name and information. Controlled for format
    for i in range(len(donor_info)):
        print('{:<20} $ {:>15.2f}   {:>10} $ {:>15.2f}'.format(donor_report[i][3], donor_report[i][0], donor_report[i][1], donor_report[i][2]))

def send_letters_to_all_donors(donor_info):
    for name in donor_info:
        if len(donor_info[name]) == 1:
            gift_description = 'gift of $' + str(donor_info[name][0])
        else:
            values = ''
            for donations in range(len(donor_info[name])):
                if donations == len(donor_info[name])-1:
                    values = values + 'and ' + '$' + str(donor_info[name][donations])
                else:
                    values = values + '$' + str(donor_info[name][donations]) + ', '
            gift_description = 'gifts of ' + values
        with open(name + '.txt', 'w') as file:
            file.write(f'Dear {name},\n')
            file.write(f'   Thank you for your kind {gift_description}.\n')
            file.write('                      Sincerely, this non-profit')

    pass

#Main function
if __name__ == '__main__':
    #Establish existing donor list
    donor_information = [["Bill Gates", 345678, 454540], ["Mark Zuckerberg", 6487, 4978,5487,1678], ["Jeff Bezos", 842], ["Paul Allen", 425, 3523], ["Kanye West", 4, 1235234]]
    #Declare donor names and amounts as separate lists
    donor_info = {}

    #Break donor information into names and amounts lists
    for donor in donor_information:
        donor_info [donor[0]] = donor [1:]

    switch_dict = {
        '1': send_thank_you,
        '2': create_report,
        '3': send_letters_to_all_donors
    }

    #Prompt the user to do something. Stay here unless user selects a quit item.
    while True:
        #Call the opening screen function
        user_selection = opening_screen()
        #Analyze responses and call related function or quit.
        if user_selection in switch_dict:
            switch_dict[user_selection](donor_info)
        elif user_selection == '4':
            break
        else:
            print('Please select a value 1-4')
        # if user_selection == '1' or user_selection == 'send a thank you':
        #     send_thank_you(donor_names, donor_amounts)
        # elif user_selection == '2' or user_selection == 'create a report':
        #     create_report(donor_names, donor_amounts)
        # elif user_selection == '3' or user_selection == 'quit':
        #     break
        #If user input does not match, just ask again
        # else:
        #     pass