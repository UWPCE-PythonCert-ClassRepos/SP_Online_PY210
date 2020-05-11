#!/usr/bin/env python3
'''mailroom.py for lesson03, Gerry Gabrisch, started 4/2/2020'''

import sys
from operator import itemgetter

#a list of existing donations...
donations = [('Eric Idle', [200.00, 500.00, 150.50]), 
             ('John Cleese', [1000, 5000, 20]), 
             ('Graham Chapman', [10000]), 
             ('Terry Jones', [50, 600, 1000, 20]), 
             ('Michael Palin', [100, 200]), 
             ('Terry Gilliam',[3000])]

def send_thanks(donations):
    '''adds a donation amount  and sends an email thankyou.  If the donor does not already exist
       a new element in the donations list will be created'''
    #get the donor name and convert the first letters of the name to upper case...
    donor_name = input('Enter a donor name now, or type "List" for a list of donors.>').title()

    #get a new list with all the donors...I did this just to avoid having to add multiple iterators below...
    donors_only = make_donor_list(donations)     
    
    if donor_name == 'List':
        #if the user types List then call the list_donors() and print all the names on a new line...
        list_donors(donors_only)
    #if this name is not already a donor then make a new donor element and get the donation amount...
    else:
        if donor_name not in donors_only:
            donations = make_new_donor(donations, donor_name)
        #this calls the function to take a donation... 
        take_donation(donations, donor_name)
            
def create_report_list(donations):
    '''this creates a report in the required formatting using f strings...'''
    #this list holds the name, donation total, donation count, and donation average...
    report_list = []
    #for every donator build a new element with the values stated above...
    for i in donations:
        user_name = i[0] 
        #count the number of donations.
        donation_count = len(i[1])
        #sum the donations
        donation_total = sum(i[1])
        thisUsersReport = (user_name, donation_total, donation_count, donation_total/donation_count)
        #Sort the list based on total donations...
        report_list.append(thisUsersReport)
    #call the sorting function...
    report_list = sort_list(report_list)
    #call the report format function...
    report_format_and_print(report_list)

def report_format_and_print(report_list):
    '''takes the sorted report and formats and prints the report to the screen... '''
    #print the report header
    print('\nDonor Name                | Total Given | Num Gifts | Average Gift')
    #for every donator get the donation stats, format and print them...
    for item in report_list:
        print(f'{item[0]:26} ${item[1]:>12.2f} {item[2]:>11}  ${item[3]:>11.2f}')
    print()
    
def sort_list(report_list):
    '''sorts the list using itemgetter from highest donor to lowest..'''
    
    #sorting sorts from lowest to highest unless you use the reverse option...
    report_list = sorted(report_list, key=itemgetter(1), reverse=True)
    return report_list

def make_donor_list(donations):
    '''this just makes a new list of donor names so I don't have to write multiple iterators...'''
    donors_only = []
    for i in donations:
        donors_only.append((i[0]))  
    return donors_only

def list_donors(list):
    '''prints the donor's names using this cool \n.join trick...'''
    print('\n'+'\n'.join(list)+'\n')

def make_new_donor(donations, donor_name):
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
    
def take_donation(donations, donor_name): 
    '''gets a new donation amount and calls the email formatter...'''
    donation_amount = float(input('Please enter a donation amount >'))
    #find the donor and add this donation to their list of donations...    
    for i in donations:
        if i[0] == donor_name:
            i[1].append(donation_amount)
            #call the mail format function...
            format_mailer(i)
    
def format_mailer(i):
    '''print the thank you email to the screen....'''
    print()
    print(f'Dear {i[0]},\nThank you.  The Ministry of Silly Walks appreciates your donation of ${i[1][-1]:.2f}.\nRespectfully\nGerry\nGerry@MinistryofSillyWalks.com')
    print()

def get_user_input():
    promp_response = input('Would you like to \n1: Take a donation and send a Thank You \n2: Create a Report or \n3: Quit? Enter a number now.>')
    if promp_response == '1':  
        send_thanks(donations)
    elif promp_response == '2':
        create_report_list(donations)
    elif promp_response == '3':
        print('Exiting this program. Goodbye')
        sys.exit()
    else:
        print('Invalid Entry')    

def main():
    while True:
        get_user_input()
        
if __name__ == "__main__":
    main()  

    