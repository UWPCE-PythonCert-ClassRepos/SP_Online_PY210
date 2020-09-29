import sys

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

def generate_thank_you_text_short(name, amount):
    ty_text_short = f'Dear {name}, thanks for the ${amount:.2f}'
    return ty_text_short

def update_dictionary(donor_info, name, amount):
    if name in donor_info:
        donor_info[name].append(amount)
        return donor_info
    else:
        donor_info[name] = [amount]
        return donor_info

def list_donors(donor_info):
    for donor in donor_info:
        print(donor)

#'Send thank you' function
def send_thank_you(donor_info):
    #Ask for a donor's name. If user requests 'list', display existing donors and request action agin.
    while True:
        name = input("Please enter a donor's name to thank (List to see existing donors, Quit to exit): ").title()
        if name == 'List':
            list_donors()
        #When user inputs something besides list, pass it on.
        else:
            break
    #If user entered 'quit', skip all this
    if name != 'Quit':
        #Ask the donor's donation amount
        amount = float(input("Please enter donation amount: "))
        update_dictionary(donor_info, name, amount)
        print(generate_thank_you_text_short(name, amount))

#New function to calculate report (makes comprehension more readable)
def calculate_report(donor_info, name):
    total = float(sum(donor_info[name]))
    number = len(donor_info[name])
    average = total/number

    return total, number, average, name

#Create report function
def generate_report(donor_info):
    #Create donor report using comprehension
    donor_report = [calculate_report(donor_info,name) for name in donor_info]
    #Sort the list by the first value (Total Gift)
    donor_report = sorted(donor_report,reverse=True)
    return donor_report

#Print report function
def print_report(donor_info):
    donor_report = generate_report(donor_info)

    #Header
    print('{:<20} | {:^10} | {:^10} | {:>15}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print ('-'*65)
    #Print report
    for i in range(len(donor_report)):
        print('{:<20} $ {:>15.2f}   {:>10} $ {:>15.2f}'.format(donor_report[i][3], donor_report[i][0], donor_report[i][1], donor_report[i][2]))

def generate_thank_you_text_long(donor_info, name):
    if len(donor_info[name]) == 1:
        gift_description = 'gift of $' + str(donor_info[name][0])
    else:
        values = ''
        for donations in range(len(donor_info[name])):
            if donations == len(donor_info[name]) - 1:
                values = values + 'and ' + '$' + str(donor_info[name][donations])
            else:
                values = values + '$' + str(donor_info[name][donations]) + ', '
        gift_description = 'gifts of ' + values
    return (f'Dear {name},\n   Thank you for your kind {gift_description}.\n                      Sincerely, this non-profit')

def send_letters_to_all_donors(donor_info):
    for name in donor_info:
        ty_text = generate_thank_you_text_long(donor_info, name)
        with open(name + '.txt', 'w') as file:
            file.write(ty_text)

def quit_program(donor_info):
    print("Leaving mailroom")
    sys.exit()

#Main function
if __name__ == '__main__':
    #Establish existing donor list
    donor_information = [["Bill Gates", 345678, 454540], ["Mark Zuckerberg", 6487, 4978,5487,1678], ["Jeff Bezos", 842], ["Paul Allen", 425, 3523], ["Kanye West", 4, 1235234]]

    #Create donor dictionary using comprehension
    donor_info = {donor[0] : donor[1:] for donor in donor_information}

    switch_dict = {
        '1': send_thank_you,
        '2': print_report,
        '3': send_letters_to_all_donors,
        '4': quit_program
    }

    #Prompt the user to do something. Stay here unless user selects a quit item.
    while True:
        #Call the opening screen function
        user_selection = opening_screen()
        #Analyze responses and call related function or quit.
        #if user_selection in switch_dict:
        try:
            switch_dict[user_selection](donor_info)
        except KeyError:
            print('Please select a value 1-4')
