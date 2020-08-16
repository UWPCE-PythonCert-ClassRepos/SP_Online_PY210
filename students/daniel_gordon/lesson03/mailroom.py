#!/bin/user/env python3
DEBUG = True

#Generate list of donors
#I'm inclined to use a dictonary of lists, but we haven't covered that yet
donors = ["Nick Esen", [1800, 720],
          "Sabina", [1500],
          "Marceline Theodosia", [30000, 500000, 100],
          "Rafat Rein", [1500000],
          "Kevin Bith", [150, 1200, 750]]

#Promt user to select action
menu = "(S)end a Thank You | (C)reate a Report | (Q)uit > "
actions = ['S', 'C', 'Q']
option = input(menu).upper()
while option not in actions:
    print("That is not an option")
    option = input(menu).upper()
if DEBUG: print(f"{option} is chosen")

#Send a Thank You interface
if option == 'S':
    #Find out who to thank
    name = input("Enter Donors Full Name> ")
    while name == 'list':
        print(donors[::2])
        name = input("Enter Doners Full Name> ")
    if name in donors:
        send_to = donors.index(name)
    else:
        send_to = len(donors)
        donors.append(name)
        donors.append([])
    #Enter ammount
    money = input("Enter ammount donated> ")
    donors[send_to+1].append(money)
    