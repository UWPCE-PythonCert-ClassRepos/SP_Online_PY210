#!/usr/bin/env python3
'''mailroom.py for lesson03, Gerry Gabrisch, started 4/2/2020'''

import sys

#a list of existing donations...
donations = [('Eric Idle', [200.00, 500.00, 150.50]), 
             ('John Cleese', [1000, 5000, 20]), 
             ('Graham Chapman', [10000]), 
             ('Terry Jones', [50, 600, 1000, 20]), 
             ('Michael Palin', [100, 200]), 
             ('Terry Gilliam',[3000])]

def SendThanks(donations):
    '''adds a donation amount  and sends an email thankyou.  If the donor does not already exist
       a new element in the donations list will be created'''
    #get the donor name and convert the first letters of the name to upper case...
    donor_name = input('Enter a donor name now, or type "List" for a list of donors.>').title()

    #get a new list with all the donors...I did this just to avoid having to add multiple iterators below...
    donorsOnly = MakeDonorList(donations)     
    
    if donor_name == 'List':
        #if the user types List then call the ListDonors() and print all the names on a new line...
        ListDonors(donorsOnly)
    #if this name is not already a donor then make a new donor element and get the donation amount...
    if donor_name not in donorsOnly and donor_name != 'List':
        donations = MakeNewDonor(donations, donor_name)
    #this calls the function to take a donation... 
    TakeDonation(donations, donor_name)
            
def CreateReportList(donations):
    '''this creates a report in the required formatting using f strings...'''
    #this list holds the name, donation total, donation count, and donation average...
    reportList = []
    #for every donator build a new element with the values stated above...
    for i in donations:
        userName = i[0] 
        #count the number of donations.
        donationCount = len(i[1])
        #sum the donations
        donationTotal = sum(i[1])
        thisUsersReport = (userName, donationTotal, donationCount, donationTotal/donationCount)
        #Sort the list based on total donations...
        reportList.append(thisUsersReport)
    #call the sorting function...
    reportList = SortList(reportList)
    #call the report format function...
    ReportFormatAndPrint(reportList)

def ReportFormatAndPrint(reportList):
    '''takes the sorted report and formats and prints the report to the screen... '''
    #print the report header
    print('\nDonor Name                | Total Given | Num Gifts | Average Gift')
    #for every donator get the donation stats, format and print them...
    for item in reportList:
        print(f'{item[0]:26} ${item[1]:>12.2f} {item[2]:>11}  ${item[3]:>11.2f}')
    print()
    
def SortList(reportList):
    '''sorts the list using itemgetter from highest donor to lowest..'''
    from operator import itemgetter
    #sorting sorts from lowest to highest unless you use the reverse option...
    reportList = sorted(reportList, key=itemgetter(1), reverse=True)
    return reportList

def MakeDonorList(donations):
    '''this just makes a new list of donor names so I don't have to write multiple iterators...'''
    donorsOnly = []
    for i in donations:
        donorsOnly.append((i[0]))  
    return donorsOnly

def ListDonors(list):
    '''prints the donor's names using this cool \n.join trick...'''
    print('\n'+'\n'.join(list)+'\n')

def MakeNewDonor(donations, donor_name):
    '''make a new donor record if the user name is not an existing donor...'''
    #make a new list to hold the new donor and append the name to this list...
    new_donor = []
    #add the donor to element position 0...
    new_donor.append(donor_name)
    #now append this list to hold the donations...
    new_donor.append([])
    #add the new donor record to the list of all donations...
    donations.append(new_donor)
    return donations
    
def TakeDonation(donations, donor_name): 
    '''gets a new donation amount and calls the email formatter...'''
    donationAmount = float(input('Please enter a donation amount >'))
    #find the donor and add this donation to their list of donations...    
    for i in donations:
        if i[0] == donor_name:
            i[1].append(donationAmount)
            #call the mail format function...
            FormatMailer(i)
    

def FormatMailer(i):
    '''print the thank you email to the screen....'''
    print()
    print(f'Dear {i[0]},\nThank you.  The Ministry of Silly Walks appreciates your donation of ${i[1][-1]:.2f}.\nRespectfully\nGerry\nGerry@MinistryofSillyWalks.com')
    print()


def main():
    while True:
        promp_response = input('Would you like to \n1: Take a donation and send a Thank You \n2: Create a Report or \n3: Quit? Enter a number now.>')
        if promp_response == '1':  
            SendThanks(donations)
        if promp_response == '2':
            CreateReportList(donations)
        if promp_response == '3':
            print('Exiting this program. Goodbye')
            sys.exit()    
if __name__ == "__main__":
    main()  

    