#!/usr/bin/env python3
import sys

#Christine Kim
#Python210 Lesson 3 Mailroom Part 1

#Database storing donors' information
givetree = [["Cullen Rutherford", 1500, 4200, 50000],
            ["Alistair Theirin", 200, 80000, 1500000],
            ["Zevran Arainai", 50],
            ["Solona Amell", 2, 500000, 2000000],
            ["Soufehla Adahlena Lavellan", 70, 600]]

#Prompt for user to be displayed
prompt = ("\nWelcome to the Blight Orphans Charity. Plase select from the above options: ")

#method for menu selection
def menu():
    #print menu table
    options = [["Send a Thank You", 1], ["Create a Report", 2], ["Quit", 3]]
    for item in options:
        print("{:<16}{:^3}".format(*item))
    #receive user input
    response = input(prompt)
    #direct user to proper function
    if response == "1":
        thank_you()
    elif response == "2":
        report()
    elif response == "3":
        end()


#method for sending thank you to donor
def thank_you():
    #receive user input donor full name
    Giver = input("\nPlease enter the full name of the donor, or type 'list' to display names on the record: ")
    while Giver.lower() == "list":
        for name in givetree:
            print(name)
        Giver = input("\nPlease enter the full name of the donor: ")

    #prompt for donation amount
    received = int(input("\nPlease enter the amount of donation: "))


    if not search(Giver, received):
    #new donor
        new_entry = [Giver, received]
        givetree.append(new_entry)
    
    #Compose gratitude email
    print("\nDear Ser {},".format(Giver))
    print("Thank you for your generous donation of ${:d}".format(received))
    print("We will make certain your goodwill is directed to aid those affected by the Fifth Blight.")
    print("With regards,")
    print("The Blight Orphans Charity,\n")

#search database
def search(Giver, amt):
    for name in givetree:
        if Giver.lower() == name[0].lower():
            #existing donor
            name.append(amt)
            return True
    return False

#Create donation histroy report for user
def report():
    #print report header
    print("\nBlight Orphans Charity Donation Report")
    header = "\n{:<30}|{:^15}|{:^10}|{:^15}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print(header)
    print("-" * len(header))

    #sort by donation total
    sorted_Giver = sorted(givetree, key=add, reverse=True)

    #summarize value and print report content
    for person in sorted_Giver:
        #Summarize value
        total = sum(person[1:])
        donation_num = len(person[1:])
        average = total / donation_num
        #print content
        print("{:<30}${:>15.2f}{:>10} ${:>15.2f}\n".format(person[0], total, donation_num, average))

#return the key for sorting = total amount of donation
def add(info):
    return sum(info[1:])

#quit the script
def end():
    print("\nThank you for your patronage. Farewell!")
    quit()


#initiate menu selection
def main_menu():
    while True:
        menu()

if __name__ == '__main__':
    main_menu()