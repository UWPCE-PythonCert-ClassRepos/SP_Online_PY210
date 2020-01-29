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
    while True:
        names = input("Please provide the Full Name of a donor:")
        if names.lower() == 'list':
            for e in donor_comprehension:
                print(e)
        else:
            break
    try:
        amount = input("Please enter a donation amount:\n")
    except ValueError:
        print("\n Invalid Amount. Please Enter a valid number \n")    
    if names in donor_comprehension:
        donor_comprehension[names].append(float(amount))   
    else:
        donor_comprehension.update({names: [float(amount)]})
    letter = {"donor_name": names, "donation_amount": float(amount)}
    print("Dear {donor_name}, we appreciate your generosity in the donation amount of ${donation_amount:.2f}.\n".format(**letter))





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




def send_letters_all(donor_comprehension):
    for name in donor_comprehension:
        if len(donor_comprehension[name]) == 1:
            gift = str(donor_comprehension[name][0])
        else:
            values = ''
            for donations in range(len(donor_comprehension[name])):
                if donations == len(donor_comprehension[name])-1:
                    values = values + 'and ' + '$' + str(donor_comprehension[name][donations])
                else:
                    values = values + '$' + str(donor_comprehension[name][donations]) + ', '
            gift = values
        with open(name + '.txt', 'w') as file:
            file.write(f'Dear {name},\n We appreciate your generosity in the donation amount of ${gift}.\n Sincerely, The Charity Team')



def exit_program(donor_comprehension):
    print("Bye!")
    sys.exit()  # exit the interactive script




if __name__ == "__main__":

#Create donor dictionary using comprehension
    donor_comprehension = {donor[0] : donor[1:] for donor in donors}

    dispatch = {"1": send_thanks, "2": write_a_report, "3": send_letters_all, "4": exit_program}

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

