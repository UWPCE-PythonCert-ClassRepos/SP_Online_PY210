#----------------------------------------#
#Python 210
# Assignment02: mailroom2.py
# Desc: Allows a user to read, and update a list of donors and thier donations.
#       Allows the user to generate a thank you email or report on historical 
#       summaries of the donors activities. 
# Change Log:
# Johnh, 2020-Nov-22 Script Created 
# Johnh, 2020-Nov-22 Updated menu selection with dictionary variable type  
# Johnh, 2020-
# Johnh, 2020-
# Johnh, 2020-
# Johnh, 2020- 
# Johnh, 2020-
# Johnh, 2020-
# Johnh, 2020-
#----------------------------------------#

import time
import sys


## Donors in the global namespace, dictionary by donor ID as key, first name
# last name and donation history as additional data entries 
## donor 
donors =	{ '001' : ['Merriweather', 'Frank',10,15,100], '002' : ['Tran', 'Thomas',5,17,23], 
              '003' : ['Terrance', 'Stephanie', 31, 48, 108], '004': ['Robidas', 'Sam', 4,90, 101],
              '005' : ['Cohen', 'Sandy', 29, 41, 70], '006' : ['Kemp', 'Shioban', 2, 23000, 19]
}


def userSelection():
    """super basic UI to prompt user and handle selections
    
    Returns: 'entry' a string with value 1, 2, or 3 selected by the user
    """
    print('Enter \'exit\' at anytime to quit')
    print('Select the Menu Option by Number')#Menu Selection Direction Output
    dictOptions = { 1 :'Send a Thank You', 2 : 'Report', 3 : 'Exit'}
    for key in dictOptions:##Prints the options for the usr to select
        val = dictOptions.value(key)
        print(str(key)+ '. ' + val)
    entry = input('enter option by number:')  
    if entry == 'exit':
        quitIt()
    if not entry.isnumeric() or 1 > int(entry) or 3 < int(entry):
        print('You must select a number 1, 2, or 3.')
        time.sleep(1)
        userSelection()
    else: 
        print('You have selected ' + dictOptions[int(entry)-1])
        time.sleep(1)
    return entry

def sendTY():
    """Returns the text of the email with the donor name, description of the 
    donations
    Prompts to enter a 'Full Name' or list, if the name is not part of the 
    list, then add that name to the list of donors and use the name
    Prompt for a donation amount, type as a number and enter into the dictionary
    Generate the Email thanking the donor, print it to terminal
    return to the prompt
    """
    names = list()
    ##Provide for the possible need to format a list of the Donor names
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
                print(key)
                first = donors[key][1]
                last = donors[key][0]
                print('{:{align}{width}}'.format(first, align='<', width=maxLenOfFirst) + \
                ' ' + '{:{align}{width}}'.format(last, align='<', width=maxLenOfLast))
            else: 
                continue
            
        if inputName == 'exit':
            quitIt()
        
        if inputName in names:
            listOrNot = 'y'
            donorID = '00'+str(names.index(inputName)+1)
            ##print('ok')
            break
        else :
            listOrNot = 'n'
        
        if listOrNot == 'n':
            first = inputName[0:inputName.index(' ')]
            last = inputName[inputName.index(' ')+1:]
            addDonor(last, first)
            donorID = list(donors.keys())[-1]
            break
    
    
    for key in donors:
        if donorID == key:
            name = str(donors[key][1]) + ' ' + str(donors[key][0]) + ','
            thing = donors[key]
            getDonations = thing[2:]
    
    
    emailText = {'text1' : "Dear ", 'text2' : "Thank you for your generous donation of ", \
                 'text3' : 'Sincerely,', 'text4' : 'John Hunter'}
    for item in getDonations:
        setDonations = item + ', '
    setDonations=setDonations[:-1]*2
    setDonations.append('.')
    ##emailText1 = "Dear " + name
    ##emailText2 = "Thank you for your generous donation."
    ##emailText3 = "Sincerely," + '\n' + 'John Hunter'
    ##print(emailText1 + '\n'*2 + emailText2 + '\n'*2 + emailText3 )

    ##print('{:{align}{width}}'.format('Donor Name', align='^', width=maxLenOfDonorName) \
         ## +' | Total Donations | Number of Donations | Avg Donation')

    print('{:{align}{width}}'.format(emailText['text1'], align='<', width = 5) + \
            '{:{align}{width}}'.format(name, align='<', width = len(name)) + '\n'*2 + \
            '{:{align}{width}}'.format(emailText['text2'], align='<', width = 40) + \
            '{:{align}{width}}'.format(setDonations, align='<', width = len(setDonations)) + '\n'*2 + \
            '{:{align}{width}}'.format(emailText['text3'], align='<', width = 10) + \
            '{:{align}{width}}'.format(emailText['text4'], align='<', width = 11))## Print the email using format()

def addDonor(last, first):
    choice = 'y'
    donations = list()
    print('Add a Donor by entering the values as requested: ')
    nextKey = '00' + str(int(list(donors.keys())[-1])+1)
    lastName = last
    firstName = first
    while choice == 'y':
        donation = input('Enter a donation amount, enter \'0\' for no donation: ')
        if donation == '0':
            choice = False
        else:
            donations.append(donation)
    newDonor = [lastName, firstName] + donations
    donors[nextKey]= newDonor
    print(newDonor)
    return None 
    
    
def runReport():
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
    ##sortByAltTotal = list()
    donorsTemp = dict()
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
        
        
    
    ##donKeys.reverse()
    ##donVals.reverse()
    donorsTempTwo = dict(zip(donKeys,donVals))
    print(donorsTempTwo)
    
    print('{:{align}{width}}'.format('Donor Name', align='^', width=maxLenOfDonorName) \
          +' | Total Donations | Number of Donations | Avg Donation')
    print('-'*maxLenOfDonorName + '-------------------------------------------------------')
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
        ' ' + '{:{align}{width}}'.format(last, align='<', width=maxLenOfLast) + \
        ' ' + '{:{align}{width}.5}'.format(str(total), align='^', width=17) + \
        ' ' + '{:{align}{width}.5}'.format(str(number), align='^', width=21) + \
        ' ' + '{:{align}{width}.5}'.format(str(average), align='^', width=15))

      
def quitIt(): 
    sys.exit(0)

def main():
    
    while True:
        entry = userSelection()
        if entry == '1':
            sendTY()
        elif entry == '2':
            runReport()
        elif entry == '3':
            quitIt()
        
    if __name__ == '__main__':
        True
main()  

    