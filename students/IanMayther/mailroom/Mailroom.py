#!/usr/bin/env python3

#Donors
'''
Paul_Allen = 
donors = 
'''

#Send Thank You

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