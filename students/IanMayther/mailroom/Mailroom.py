#!/usr/bin/env python3

#Donors
donors = [("Morgan Stanely", [0.01, 20.00]),
            ("Cornelius Vanderbilt", [800, 15, 10]),
            ("John D. Rockefeller", [7000, 150, 25]),
            ("Stephen Girard", [60000]),
            ("Andrew Carnegie", [0.04, 999.99])]


#Send Thank You
def send_thank_you():
    option = input("List or New:")
    option.lower()
    if option == "list":
        for i in range(len(donors)):
            print(donors[i][0])
    elif option == "new":
        print("They didn't give anything!")
    recipient = input("Who would you like to send a Thank You to?")
    name = recipient
    for i in range(len(donors)):
        if name == donors[i][0]:
            name = donors[i][0]
        else:
            name = ""
    pass

#Create Report

#Main Exicutable
if __name__ == '__main__':
    #Initial Menu
    real_response = False
    while real_response == False:
        directive = input("What would you like to do; [1]Send Thank you, [2]Create Report, [3]Quit:")
        if directive == "1" or directive == "2" or directive == "3":
            if directive == "1":
                #Launch Send Thank you
                print("Send Thank You")
                send_thank_you()
                
                real_response = True
            elif directive == "2":
                #Launch Create Report
                print("Create Report")
                real_response = True
            elif directive == "3":
                #Quit
                print("Quiter")
                real_response = True
        else:
            print("Please select one of the options above")