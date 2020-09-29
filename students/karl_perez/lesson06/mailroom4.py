#!/usr/bin/env python3
#Mailroom part 3
import sys  

#donors
donors = [["Krystal Perez", 50.00, 250.00],
    ["Eddie Lau", 32.50],
    ["Jimmy Jack", 200.00, 350.00, 400.00],
    ["Grace Cool", 120.00, 75.00],
    ["Adriel Molina", 45.00, 450.00]]



# menu prompt
def menu():
    #Tell the user what their options are. Ask for an input.
    print('')
    print('Welcome to the mailroom tool. Please select an action:')
    print('1 - Send a Thank You')
    print('2 - Create a Report')
    print('3 - Send letters to all donors')
    print('4 - Quit')
    #Send user input back to main function to be analyzed.
    return input()




# Send a thank you
def send_thanks(donor_comprehension):
    print("To view current donors, type 'list' ")
    #Ask for a donor's name. If user requests 'list', display existing donors and request action agin.
    while True:
        names = input("Please provide the Full Name of a donor:")
        if names.lower() == 'list':
            list_donors(donor_comprehension)
        #When user inputs something besides list, pass it on.
        else:
            break
    #If user entered 'quit', skip all this
    if names != 'Quit':
        #Ask the donor's donation amount
        amount = float(input("Please enter donation amount: "))
        update_dict(donor_comprehension, names, amount)
        print(thank_you_short(names, amount))


def list_donors(donor_comprehension):
    for donor in donor_comprehension:
        print(donor)


def thank_you_short(names, amount):
    ty_text_short = f'Dear {names}, thanks for your generosity in the amount of ${amount:.2f}'
    return ty_text_short


def update_dict(donor_comprehension, names, amount):
    if names in donor_comprehension:
        donor_comprehension[names].append(amount)
        return donor_comprehension
    else:
        donor_comprehension[names] = [amount]
        return donor_comprehension


#create a report that calculate Donor Name, Total Given, Number of donatons, and the avarage amount of thier donations
def write_a_report(donor_comprehension):
    Title = "\n{:<12}{:<6}{:<15}{}{:<10}{}{:<10}".format(*('Donor Name','|','Total Given','|','Num Gifts','|','Average Gift'))
    print(Title)
    print ('-'*len(Title))
    #Create donor report using comprehension
    donor_report = [calculator(donor_comprehension,names) for names in donor_comprehension]
    #Sort the list by the first value (Total Gift)
    donor_report = sorted(donor_report,reverse=True)
    for i in range(len(donor_comprehension)):
        print('{:<20} $ {:>15.2f}   {:>10} $ {:>15.2f}'.format(donor_report[i][3], donor_report[i][0], donor_report[i][1], donor_report[i][2]))




#New function to calculate report (makes comprehension more readable)
def calculator(donor_comprehension, names):
    total = float(sum(donor_comprehension[names]))
    number = len(donor_comprehension[names])
    average = total/number
    return total, number, average, names


#Create report function
def generate_report(donor_comprehension):
    #Create donor report using comprehension
    donor_report = [calculator(donor_comprehension,name) for name in donor_comprehension]
    #Sort the list by the first value (Total Gift)
    donor_report = sorted(donor_report,reverse=True)
    return donor_report



def generate_thank_you_long(donor_comprehension, name):
    if len(donor_comprehension[name]) == 1:
        gift_description = 'gift of $' + str(donor_comprehension[name][0])
    else:
        values = ''
        for donations in range(len(donor_comprehension[name])):
            if donations == len(donor_comprehension[name]) - 1:
                values = values + 'and ' + '$' + str(donor_comprehension[name][donations])
            else:
                values = values + '$' + str(donor_comprehension[name][donations]) + ', '
        gift_description = 'gifts of ' + values
    return (f'Dear {name},\n   We appreciate your generosity in the donation amount of ${gift_description}.\n Sincerely, The Charity Team')

def send_letters_to_all(donor_comprehension):
    for name in donor_comprehension:
        ty_text = generate_thank_you_long(donor_comprehension, name)
        with open(name + '.txt', 'w') as file:
            file.write(ty_text)

def exit_program(donor_comprehension):
    print("Bye!")
    sys.exit()  # exit the interactive script




if __name__ == "__main__":

#Create donor dictionary using comprehension
    donor_comprehension = {donor[0] : donor[1:] for donor in donors}

    dispatch = {"1": send_thanks, "2": write_a_report, "3": send_letters_to_all, "4": exit_program}

#Prompt the user to do something. Stay here unless user selects a quit item.
    while True:
    #Call the opening menu function
        user = menu()
    #Analyze responses and call related function or quit.
    #if user in switch_dict:
        try:
            dispatch[user](donor_comprehension)
        except KeyError:
            print('Please select a value 1-4')

