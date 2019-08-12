#imports

import sys

from statistics import mean

from operator import itemgetter

# data structure

donors = [["Usagi", [12.5, 11.17, 130.1]], ["Ami", [17, 230, 2115]],
["Rei", [510.1, 50]], ["Makoto", [324, 22.7]], ["Minako", [310]]]


#functions

def send_thankyou():
    while True:
        donorname = input("Please input a name:\n")
        if donorname == "C":
            return
        if donorname == "list":
            for i in donors:
                print(i[0])
        else:
            break
    donationamount = input("Please enter a donation amount:\n")
    if donationamount == "C":
        return
    for d in donors:
        if d[0] == donorname:
            break
    else:
        donors.append([donorname, []])
    for d in donors:
        if d[0] == donorname:
            d[1].append(float(donationamount))
    print(f"Dear {donorname}, thank you for your generous donation of ${float(donationamount):.2f}.\n")

def write_report():
    titles = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    print(f"{titles[0]:15} {titles[1]:>20} {titles[2]:>10} {titles[3]:>20}")
    reportlines = []
    for d in donors:
        dname = d[0]
        dtotal = sum(d[1])
        dnum = len(d[1])
        davggift = dtotal/dnum
        reportlines.append([dname, dtotal, dnum, davggift])
    for r in sorted(reportlines, key=itemgetter(1), reverse = True):
        print(f"{r[0]:15} {r[1]:>20.2f} {r[2]:>10} {r[3]:>20.2f}")

def quit_program():
    print("Goodbye!")
    sys.exit()

#main flow

def main():
    while True:
        response = input("Select an action: 1 - Send a Thank You, 2 - Create a Report, or 3 - Quit\nReturn to main menu any time by entering 'C'\n")
        if response == "1":
            send_thankyou()
        elif response == "2":
            write_report()
        elif response == "3":
            quit_program()
        else:
            print("Please select from actions 1, 2, or 3!")


if __name__ == "__main__":
    main()