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
#----------------------------------------#

import sys

## Donors in the global namespace, dictionary by donor ID as key, first name
# last name and donation history as additional data entries  
donors =	{ '001' : ['Merriweather', 'Frank',10,15,100], '002' : ['Tran', 'Thomas',5,17,23], 
              '003' : ['Terrance', 'Stephanie', 31, 48, 108], '004': ['Robidas', 'Sam', 4,90, 101],
              '005' : ['Cohen', 'Sandy', 29, 41, 70], '006' : ['Kemp', 'Shioban', 2, 23000, 19]}

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
    maxLenOfFirst=0
    maxLenOfLast=0
    for key in donors:                     
        if (len(donors[key][1])>maxLenOfFirst):    
            maxLenOfFirst = len(donors[key][1])
        if (len(donors[key][0])>maxLenOfLast):    
            maxLenOfLast = len(donors[key][0])
          
    while True:
        inputName= input('Enter full name of donor or \'list\' to request list of donors: ')  
        for key in donors:
            first = donors[key][1]
            last = donors[key][0]
            names.append(first + ' ' + last)  
        
        if inputName == 'list':        
            for key in donors:
                first = donors[key][1]
                last = donors[key][0]
                print('{:{align}{width}}'.format(first, align='<', width=maxLenOfFirst) + \
                ' ' + '{:{align}{width}}'.format(last, align='<', width=maxLenOfLast))
            else: 
                continue
            
        if inputName == 'exit':
            quit_it()
        
        if inputName in names:
            listOrNot = 'y'
            donorID = '00'+str(names.index(inputName)+1)
            break
        else :
            listOrNot = 'n'
        
        if listOrNot == 'n':
            first = inputName[0:inputName.index(' ')]
            last = inputName[inputName.index(' ')+1:]
            add_donor(last, first)
            donorID = list(donors.keys())[-1]
            break
    
    for key in donors:
        if donorID == key:
            name = str(donors[key][1]) + ' ' + str(donors[key][0]) + ','
    
    emailText1 = "Dear " + name
    emailText2 = "Thank you for your generous donation."
    emailText3 = "Sincerely," + '\n' + 'John Hunter'
    print(emailText1 + '\n'*2 + emailText2 + '\n'*2 + emailText3 )

def add_donor(last, first):
    """Adds a donor to the donor dictionary and allows the user to add donation values
    
    Returns: 'None'
    """
    choice = 'y'
    donations = list()
    print('The name submitted is not on the list of donors.')
    print('The donor name will be added, please add donation values: ')
    nextKey = '00' + str(int(list(donors.keys())[-1])+1)
    lastName = last
    firstName = first
    while choice == 'y':
        donation = input('Enter a donation amount, enter \'0\' to stop adding donation values: ')
        if donation == '0':
            choice = False
        else:
            donations.append(donation)
    newDonor = [lastName, firstName] + donations
    donors[nextKey]= newDonor
    print('The new donor has been added:')
    print(newDonor)
    print('The Thank You email for the new donor is:')
    return None 
    
def run_report():
    """Returns a report of the donors by total historical amount
    The report should contain the Donor Name, total donated, number of 
    donations, and average donation amount as values in each row
   """ 
    maxLenOfDonorName=0
    maxLenOfFirst=0
    maxLenOfLast=0
    total = 0
    y = 0
    sortByTotal = list()
    donKeys = list()
    donVals = list()
    listNow = list()
    #sortByAltTotal = list()
    #donorsTemp = dict()
    donorsTempTwo = donors
    
    for key in donorsTempTwo:                     
        if (len(donorsTempTwo[key][1])>maxLenOfFirst):    
            maxLenOfFirst = len(donorsTempTwo[key][1])
        if (len(donorsTempTwo[key][0])>maxLenOfLast):    
            maxLenOfLast = len(donorsTempTwo[key][0])
    
    maxLenOfDonorName = maxLenOfLast + maxLenOfFirst
    
    for key in donorsTempTwo:
        listNow = donorsTempTwo[key]
        listNow = listNow[2:]
        y = len(listNow)
        total=0
        for value in range(y):
            total = total + int(listNow[value])
        sortByTotal.append(total)
    
    x=len(sortByTotal)
    
    for i in range(x):
        maxItem = max(sortByTotal)
        indexOf = sortByTotal.index(maxItem)
        keyOf = '00'+ str(indexOf+1)
        donKeys.append(keyOf)
        donVals.append(donorsTempTwo.get(keyOf))
        sortByTotal[indexOf]=-1
        
    donorsTempTwo = dict(zip(donKeys,donVals))
    
    print('{:{align}{width}}'.format('Donor Name', align='^', width=maxLenOfDonorName) +' |   Total Given   |     Num of Gifts    | Avgerage Gift')
    print('-'*maxLenOfDonorName + '--------------------------------------------------------')
    for key in donorsTempTwo:
        z = len(donorsTempTwo[key]) - 2
        total = 0
        for j in range(z):
            total = total + int(donorsTempTwo[key][j+2])
        number = len(donorsTempTwo[key])-2
        average = total/number
        first = donorsTempTwo[key][1]
        last = donorsTempTwo[key][0]
        print('{:{align}{width}}'.format(first, align='<', width=maxLenOfFirst) + \
        ' ' + '{:{align}{width}}'.format(last, align='<', width=maxLenOfLast) + '$' +\
        ' ' + '{:{align}{width}.5}'.format(str(total), align='^', width=16) + \
        ' ' + '{:{align}{width}.5}'.format(str(number), align='^', width=21) + '$' + \
        ' ' + '{:{align}{width}.5}'.format(str(average), align='^', width=14))
      
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

    