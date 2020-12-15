lst_donor_table = [
['Henry Michalson',10,500,25],
['Phil Hutch',76],
['Galileo Humpkins',22000,100,490],
['Methusela Honeysuckle',18,69,76000],
['Lavender Goombs',55000,25],
['test',1]
]
def showMenu():
    # shows user list of options
    # return is void
    """  Display a menu of choices to the user
    :return: nothing
    """
    print('''
    Menu of Options
    1) Send a Thank You
    2) Create a Report
    3) quit
    ''')
    print()  # Add an extra line for looks
def getUserChoice():
    # asks user for choice
    # returns integer value of user's choice
    """ Gets the menu choice from a user
    :return: string
    """
    choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
    print()  # Add an extra line for looks
    return choice

def sendThankYou():
    lst_donors = []
    for current_donor in lst_donor_table:
        lst_donors.append(current_donor[0])
    donor =''
    while(len(donor)<1):
        donor = input('Please enter full name of donor >>> ')
        if donor == 'list':
            print(lst_donors)
            donor = ''
    new_donation = int(input('Please enter the donation amount >>> '))
    if donor in lst_donors:
        for i in range(0, len(lst_donors)):
            if lst_donors[i] == donor:
                lst_donor_table[i].append(new_donation)
    else:
        lst_donor_table.append([donor, new_donation])
    str_thankyou = f'Thank you, {donor} for the generous gift of {new_donation}. You are incredibly nice.'
    print(str_thankyou)

def getDonorData(donor_name):
    for current_donor in lst_donor_table:
        if current_donor[0] == donor_name:
            lst_gifts = current_donor[1:]
    return [sum(lst_gifts), len(lst_gifts), sum(lst_gifts)/len(lst_gifts)]

def formatRow(info_list):
    return '{:<26} {:<2} {:10.2f} {:>11} {:^2} {:10.2f}'.format(info_list[0],info_list[1],info_list[2],info_list[3], info_list[4], info_list[5])
def createReport():
    header = '{:<25} {:^10} {:^10} {:^10}'.format('Donor Name', '| Total Given', '| Num Gifts', '| Average Gift')
    print(header)
    print('------------------------------------------------------------------')
    for current_donor in lst_donor_table:
        donor_data = getDonorData(current_donor[0])
        new_row = [current_donor[0], '$', donor_data[0], donor_data[1], "$", donor_data[2]]
        print(formatRow(new_row))


if __name__ == '__main__':
    while(True):
        showMenu()  # Shows menu
        strChoice = getUserChoice()  # Get menu option
        if (strChoice.strip() == '1'):
            sendThankYou()
        elif(strChoice.strip() == '2'):
            createReport()
        elif(strChoice == '3'):
            break   # and exit
