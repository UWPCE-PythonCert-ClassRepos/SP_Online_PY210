
# ------------------------------------------------------------------------ #
# Title: Mailroom 2
# Description: Updating mailroom script using dicts and IO files

# ChangeLog (Who,When,What):
# JEmbury,12/12/2020,Created started script
# ------------------------------------------------------------------------ #

# Data
#-----------------------------------------------#
dict_donor_table = {
'Henry Henrickson' : [10,500,25],
'Geraldo Duckworth' : [76],
'Galileo Humpkins' : [22000,100,490],
'Methusela Honeysuckle' : [18,69,76000],
'Lavender Goombs' : [55000,25],
}

#-----------------------------------------------#
# IO methods
#-----------------------------------------------#
def showMenu():
    # shows user list of options
    # return is void
    """  Display a menu of choices to the user
    :return: nothing
    """
    print('''
    Menu of Options
    1) Send a Thank You to a single donor
    2) Create a Report
    3) Send letters to all donors
    4) Quit
    ''')
    print()  # Add an extra line for looks
def getUserChoice():
    # asks user for choice
    # returns integer value of user's choice
    """ Gets the menu choice from a user
    :return: string
    """
    choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
    print()  # Add an extra line for looks
    return choice

def sendThankYou():
    donor = input('Please enter full name of donor >>> ')
    new_donation = int(input('Please enter the donation amount >>> '))
    if donor in dict_donor_table.keys():
        dict_donor_table[donor].append(new_donation)
    else:
        dict_donor_table[donor] = [new_donation]
    print(thankYouLetter(donor, new_donation))

def writeToFile(input_dict):
    for key in input_dict.keys():
        #print(thankYouLetter(key,getDonorData(input_dict[key])[0]))
        with open(key + '.txt','w') as new_file:
            new_file.write(thankYouLetter(key,getDonorData(input_dict[key])[0]))
        new_file.close()
#-----------------------------------------------#
# Processing methods
#-----------------------------------------------#
def getDonorData(lst_gifts):
    # input is a list of donor gift history
    # output is list data in format:
    # [Sum of gifts, num of gifts, average gift amount]
    return [sum(lst_gifts), len(lst_gifts), sum(lst_gifts)/len(lst_gifts)]

def thankYouLetter(donor, amount):
    str_thankyou = f'Dear {donor},\n'\
    f'    Thank you so much for the generous gift of {amount} dollars. '\
    'This donation is going to help us so much for so many reasons. '\
    'You are incredibly nice and are obviously an outstanding person.\n'\
    '    If you are able to make any further donations please feel free '\
    'to access the Python Donation console application. \n'\
    'Sincerely,\n'\
    'The Python Development Team'
    return str_thankyou

def formatRow(info_list):
    return '{:<26} {:<2} {:10.2f} {:>11} {:^2} {:10.2f}'.format(info_list[0],info_list[1],info_list[2],info_list[3], info_list[4], info_list[5])

def createReport():
    header = '{:<25} {:^10} {:^10} {:^10}'.format('Donor Name', '| Total Given', '| Num Gifts', '| Average Gift')
    print(header)
    print('------------------------------------------------------------------')
    for current_donor in dict_donor_table.keys():
        donor_data = getDonorData(dict_donor_table[current_donor])
        new_row = [current_donor, '$', donor_data[0], donor_data[1], "$", donor_data[2]]
        print(formatRow(new_row))

def sendLetters():
    writeToFile(dict_donor_table) # invoke write method with dict

def quitProgram():
    exit() # break out of while loop
dictMenu = {
    1: sendThankYou,
    2: createReport,
    3: sendLetters,
    4: quitProgram
}

#-----------------------------------------------#
# Main
#-----------------------------------------------#
if __name__ == '__main__':
    while(True):
        showMenu()  # Displays menu to console
        dictMenu.get(int(getUserChoice()))()  # Get menu option by dict switch
