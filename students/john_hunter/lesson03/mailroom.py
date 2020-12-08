#----------------------------------------#
#Python 210
# Assignment01: mailroom.py
# Desc: Allows a user to read, and update a list of donors and thier donations.
#       Allows the user to generate a thank you email or report on historical 
#       summaries of the donors activities. 
# Change Log:
# Johnh, 2020-Sept-22 Script Created 
# Johnh, 2020-Sept-22 Header and basic functions defined  
# Johnh, 2020-Sept-22 Some previous text UI work copied from other script
# Johnh, 2020-Sept-24 Basic clean up to get the script to execute, added main
# Johnh, 2020-Sept-26 Definition of the send thank you function
# Johnh, 2020-Oct-21 Code satsfies all requirements 
# Johnh, 2020-Oct-22 Readablity Review, comments cleanup, SoC formatting
# Johnh, 2020-Oct-22 Tested, passed
# Johnh, 2020-Oct-23 Review Git commit procedure
# Johnh, 2020-Nov-23 Added to Git and submitted
# Johnh, 2020-Nov-27 Refactor for style snake_case naming of functions
# Johnh, 2020-Dec-6  Refeactor for list to be used instead of Dictionary
#----------------------------------------#

import sys

## Donors in the global namespace

donors = [['Frank Merriweather', 10, 15, 100], ['Thomas Tran', 5, 17, 23], \
          ['Stephanie Terrance', 31, 48, 108], ['Sam Robidas', 4, 90, 101], \
          ['Sandy Cohen', 29, 41, 70], ['Shioban Kemp', 2, 23000, 19]]

def user_selection():
    """Basic UI to prompt user and handle selections
    
    Returns: 'entry' a string with value 1, 2, or 3 selected by the user
    """
    options = ('Send a Thank You', 'Create a Report', 'quit')
    print('Enter \'exit\' at anytime to quit')
    print('Select the Menu Option by Number')#Menu Selection Direction Output
    for item in options:##Prints the options for the user to select
        index = options.index(item)
        print(str(index+1)+ '. ' + item)
    entry = input('enter option by number:')  
    if entry == 'exit':
        quit_it()
    if not entry.isnumeric() or 1 > int(entry) or 3 < int(entry):
        print('You must select a number 1, 2, or 3.')
        user_selection()
    else: 
        print('You have selected ' + options[int(entry)-1])
    return entry

def send_ty():
    """Returns the text of the email with the donor name, description of the 
    donations
    Prompts to enter a 'Full Name' or list, if the name is not part of the 
    list, then add that name to the list of donors and use the name
    Prompt for a donation amount, type as a number and enter into the dictionary
    Generate the Email thanking the donor, print it to terminal
    return to the prompt
    """
    names = list()
    #Format a list of the Donor names
    maxLenOfName=0
    
    for i in range(1,len(donors)):                     
        if (len(donors[i][0])>maxLenOfName):    
            maxLenOfName = len(donors[i][0])

    while True:
        inputName= input('Enter full name of donor or \'list\' to request list of donors: ')  
        for j in range(len(donors)):
            names.append(donors[j][0])  
        
        if inputName == 'list':        
            for k in range(len(donors)):
                name = donors[k][0]
                print('{:{align}{width}}'.format(name, align='<', width=maxLenOfName))
            else: 
                continue
        
        if inputName == 'exit':
            quit_it()
        
        if inputName in names:
            listOrNot = 'y'
            break
        
        else :
            listOrNot = 'n'
        if listOrNot == 'n':
            add_donor(inputName)
            listOrNot = 'n'
            moreDonations = 'n'
            break
    masDonations = 'Would you like to add more donations for ' + inputName + '? y/n: ' 
    if listOrNot == 'y':
        moreDonations = input(masDonations)    
    if moreDonations == 'y':
        totals = add_donations(inputName)
    else:
        totals = 0
        for z in range(len(donors)):
            if inputName == donors[z][0]:
                for c in range(len(donors[z])-1):
                    totals = totals + int(donors[z][c+1])
                break

    
    emailText1 = "Dear " + inputName
    emailText2 = "Thank you for your generous donation(s) of $" + str(totals) + '.'
    emailText3 = "Sincerely," + '\n' + 'John Hunter'
    print(emailText1 + '\n'*2 + emailText2 + '\n'*2 + emailText3 )

def add_donor(name):
    """Adds a donor to the donor dictionary and allows the user to add donation values
    
    Returns: 'None'
    """
    choice = 'y'
    donations = list()
    print('The name submitted is not on the list of donors.')
    print('The donor name will be added, please add donation values: ')
    while choice == 'y':
        donation = input('Enter a donation amount, enter \'0\' to stop adding donation values: ')
        if donation == '0':
            choice = False
        else:
            donations.append(donation)
    donations.insert(0,name)
    newDonor = donations
    donors.append(newDonor)
    print('The new donor has been added:')
    print(newDonor)
    print('The Thank You email for the new donor is:')
    return None 

def add_donations(name):
    donations = list()
    donation = int()
    while True:
        donation = int(input('Enter a donation amount, enter \'0\' to stop adding donation values: '))
        if donation == 0:
            break
        else:
            int(donation)
            donations.insert(-1,donation)
    for i in range(len(donors)):
        if name == donors[i][0]:
            donors[i] = donors[i] + donations
            break
    print(donors[i])
    return sum(donors[i][1:])

def run_report():
    """Returns a report of the donors by total historical amount
    The report should contain the Donor Name, total donated, number of 
    donations, and average donation amount as values in each row
   """ 
    maxLenOfName=0
    total = 0
    y = 0
    sortByTotal = list()
    listNow = list()
    donorsTempTwo = donors
    
    for i in range(len(donorsTempTwo)):                     
        if (len(donorsTempTwo[i][0])>maxLenOfName):    
            maxLenOfName = len(donorsTempTwo[i][0])
    
    for j in range(len(donorsTempTwo)):
        listNow = donorsTempTwo[i]
        listNow = listNow[1:]
        y = len(listNow)
        total=0
        for value in range(y):
            total = total + int(listNow[value])
        sortByTotal.append(total)
    
    x=len(sortByTotal)
    
    for k in range(x):
        maxItem = max(sortByTotal)
        indexOf = sortByTotal.index(maxItem)
        sortByTotal[indexOf]=-1
    
    print('{:{align}{width}}'.format('Donor Name', align='^', width=maxLenOfName) + \
          ' |   Total Given   |     Num of Gifts    | Avgerage Gift')
    print('-'*maxLenOfName + '--------------------------------------------------------')
    for l in range(len(donorsTempTwo)):
        z = len(donorsTempTwo[l]) - 1
        total = 0
        for m in range(z):
            total = total + int(donorsTempTwo[l][m+1])
        number = len(donorsTempTwo[l])-1
        average = total/number
        jeff = donorsTempTwo[l][0]
        #last = donorsTempTwo[l][0]
        print('{:{align}{width}}'.format(jeff, align='<', width=maxLenOfName) + \
        ' ' + '$' + ' ' + '{:{align}{width}.5}'.format(str(total), align='^', width=16) + \
        ' ' + '{:{align}{width}.5}'.format(str(number), align='^', width=21) + '$' + \
        ' ' + '{:{align}{width}.2f}'.format(average, align='^', width=14))
      #print("{:#.6g}".format(i))
def quit_it(): 
    sys.exit(0)

def main():
    
    while True:
        entry = user_selection()
        if entry == '1':
            send_ty()
        elif entry == '2':
            run_report()
        elif entry == '3':
            quit_it()
        
if __name__ == '__main__':
    main()  

    