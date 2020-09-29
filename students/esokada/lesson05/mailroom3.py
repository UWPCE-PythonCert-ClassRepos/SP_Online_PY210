#imports

import sys

from statistics import mean

from operator import itemgetter


# data structure

donors = {"Usagi":[12.5, 11.17, 130.1], "Ami":[17, 230, 2115], "Rei":[510.1, 50], "Makoto": [324, 22.7], "Minako": [310] }

#functions

def send_thankyou():
    while True:
        donorname = input("Please input a name, 'list' command, or 'c' to cancel:\n")
        if donorname == "c":
            return
        elif donorname == "list":
            print(donors.keys())
        else:
            while True:
                donationamount = input("Please enter a donation amount:\n")
                try:
                    if donationamount == "c":
                        return
                    if donorname in donors:
                        donors[donorname].append(float(donationamount))
                        break
                    else:
                        donors.update({donorname: [float(donationamount)]})
                        break
                except ValueError:
                    print("Please enter the donation amount as a number.")
            letterdict = {"donor_name": donorname, "donation_amount": float(donationamount)}
            print("Dear {donor_name}, thank you for your generous donation of ${donation_amount:.2f}.\n".format(**letterdict))
            break


def write_report():
    titles = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    print(f"{titles[0]:15} {titles[1]:>20} {titles[2]:>10} {titles[3]:>20}")
    #this seemed to be the only place to use a list comprehension:
    reportlines = [[k, sum(v), len(v), sum(v)/len(v)] for k, v in donors.items()]
    for r in sorted(reportlines, key=itemgetter(1), reverse = True):
        print(f"{r[0]:15} {r[1]:>20.2f} {r[2]:>10} {r[3]:>20.2f}")


def batch_letters():
    for k, v in donors.items():
        filetext = f"Dear {k},\nThank you for your donation of ${v[-1]:.2f}. Your total donations to date are ${sum(v):.2f}.\nWe appreciate your generosity to our organization.\nThanks, the Management."
        with open(f"{k}.txt", "w") as f:
            f.write(filetext)


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