#!/usr/bin/env python3

#Donors
donors = [("Morgan Stanely", [0.01, 20.00]),
            ("Cornelius Vanderbilt", [800, 15, 10.00]),
            ("John D. Rockefeller", [7000, 150.00, 25]),
            ("Stephen Girard", [60000]),
            ("Andrew Carnegie", [0.04, 999.99])]


#Send Thank You
def receiver(giver):
    name = giver.lower()
    #Determine Previous Donor
    if name == "list":
        for i in range(len(donors)):
            print(f"[{i+1}] " + donors[i][0])
        existing = True
        while existing:
            num = input("Please select the corresponding number for existing donor? ")
            if num.lower() == 'quit':
                name = 'quit'
                existing = False
            elif (int(num)-1) in range(len(donors)):
                print(f"You selected: {donors[int(num)-1][0]}")
                existing = False
                name = donors[int(num)-1][0]  
    else: #Verify not existing Donor
        name = giver
    return name

#Donor Verification
def ver_don(giver):
    exist = False
    for i in range(len(donors)):
        if giver == donors[i][0]:
            exist = True
        else:
            exist = False
    return exist

#Get Value of Donation
def gift():
    while True:
        try:
            value = float(input("What is the value of the donation: "))
            break      
        except ValueError:
            print("Not a valid donation value")
    return value


#Print Email
def email(TO, gift_amount):
    name = TO
    donation = gift_amount
    body = f"""Greetings {name}\n
\n
Thank you so much for your generous contribution to our charity.\n
It is donors like you who make our work of building schools for ants' possible.\n
With your gift of ${donation}, means (10) or (20) more schools can be built to help the ants learn to read.\n
\n
Sincerely,\n
Derek Zoolander\n
Founder and C.E.O. of Derek Zoolander Charity for Ants Who Can't Read Good (DZCAWCRG)"""
    return body


#Create Report
def print_report(my_List = []):
    #Header
    print("{0:<25s}|{1:^15s}|{2:^15s}|{3:>12s}".format("Donor Name", "Total Given", "# of Gifts","Avg. Gift"))
    print("-" * 72)
    #Table Data
    for i in range(len(my_List)):
        #Process Data
        #Donor
        col = my_List[i][1]
        #Sum Total 
        total = sum(col)
        #Gift Count  
        No_Gifts = len(my_List[i][1])
        #Calc Average
        Ave_Gift = total / No_Gifts
        #Print Table
        print("{0:<25s}${1:>14.2f}{2:>17d}  ${3:>11.2f}".format(my_List[i][0],total, No_Gifts, Ave_Gift, end =''))    
    return

#Main Exicutable
if __name__ == '__main__':
    #Initial Menu
    real_response = False
    donors1 = donors
    while real_response == False:
        directive = input("What would you like to do; [1]Send Thank you, [2]Create Report, [3]Quit: ")
        if directive == "1" or directive == "2" or directive == "3":
            if directive == "1":
                #Launch Send Thank you
                grat = input("Who would you like to send a Thank You to? Enter 'list' for a list of previous donors.  ")
                #Quit Code
                if grat.lower() == "quit":
                    continue
                recipient = receiver(grat)
                if recipient.lower() == "quit":
                    continue
                ver_don(recipient)
                contr = gift()
                if contr == "quit":
                    continue
                if not ver_don:
                    new_donor = [recipient[:-1], (contr)]
                    donors1.append(new_donor)
                    print(email(new_donor[0][0],new_donor[0][1]))
                else:
                    for i in range(len(donors)):
                        if recipient == donors[i][0]:
                            donors[i][1].append(contr)
                            print(donors)
                    print(email(recipient, contr))
            elif directive == "2":
                #Launch Create Report
                print("Create Report")
                print_report(donors1)
            elif directive == "3":
                #Quit
                print("Quitter")
                real_response = True
        else:
            print("Please select one of the options above")