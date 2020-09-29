#imports

import sys

from statistics import mean

from operator import itemgetter


# data structure

donors = {
            "Usagi":[12.5, 11.17, 130.1],
            "Ami":[17, 230, 2115],
            "Rei":[510.1, 50],
            "Makoto": [324, 22.7],
            "Minako": [310]
            }

#Send a Thank You

def send_thankyou():
    while True:
        donorname = input("Please input a name, 'list' to see names, or 'c' to cancel:\n")
        if donorname == "c":
            return
        elif donorname == "list":
            print(show_donorlist(donors))
        else:
            add_donor(donorname, donors)
            while True:
                donationamount = input("Please enter a donation amount:\n")
                if donationamount == "c":
                    return
                try:
                    amount = float(donationamount)
                except ValueError:
                    print("Please enter the donation amount as a number.")
                else:
                    update_donor(donorname, donors, amount)
                    print(write_oneletter(donorname, amount))
                    return


def show_donorlist(donors):
    donorlist = []
    for key, value in donors.items():
        donorlist.append(key)
    return donorlist


def add_donor(donorname, donors):
    if donorname not in donors:
        donors.update({donorname: []})


def update_donor(donorname, donors, amount):
    donors[donorname].append(amount)


def write_oneletter(donorname, amount):
    letterdict = {"donor_name": donorname, "donation_amount": amount}
    lettercontent = "Dear {donor_name}, thank you for your generous donation of ${donation_amount:.2f}.\n".format(**letterdict)
    return lettercontent


#Create a Report

def write_report():
    print(create_rows(donors))


def create_rows(donors):
    final_report = ""
    titles = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    formatted_titles = f"{titles[0]:15} {titles[1]:>20} {titles[2]:>10} {titles[3]:>20}\n"
    final_report += formatted_titles
    reportlines = []
    for k, v in donors.items():
        try:
            reportlines.append([k, sum(v), len(v), sum(v)/len(v)])
        except ZeroDivisionError:
            reportlines.append([k, sum(v), len(v), 0])
    sortedlines = sorted(reportlines, key=itemgetter(1), reverse = True)
    for r in sortedlines:
        final_report += f"{r[0]:15} {r[1]:>20.2f} {r[2]:>10} {r[3]:>20.2f}\n"
    return final_report


#Generate Letters to All Donors

def batch_letters():
    for k, v in donors.items():
        filetext = batch_letters_text(k, v)
        batch_letters_files(k, filetext)


def batch_letters_text(k, v):
    return f"Dear {k},\nThank you for your donation of ${v[-1]:.2f}. Your total donations to date are ${sum(v):.2f}.\nWe appreciate your generosity to our organization.\nThanks, the Management."


def batch_letters_files(k, filetext):
    with open(f"{k}.txt", "w") as f:
            f.write(filetext)


#Quit

def quit_program():
    print("Goodbye!")
    sys.exit()


#menus

def menu_selection(main_prompt, main_dispatch):
    while True:
        response = input(main_prompt)
        try:
            main_dispatch[response]()
        except KeyError:
            print("Please enter a number that corresponds to a menu option.")


#prompts

main_prompt = ("Select an action: 1 - Send a Thank You, 2 - Create a Report, 3 - Generate letters to all donors, or 4 - Quit\nReturn to main menu any time by entering 'c'\n")

main_dispatch = {"1": send_thankyou,
                 "2": write_report,
                 "3": batch_letters,
                 "4": quit_program
                 }



if __name__ == "__main__":
    menu_selection(main_prompt, main_dispatch)