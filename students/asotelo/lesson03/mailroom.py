#!/usr/bin/env python3

import getpass
username = getpass.getuser()

'''
Author: Alex Sotelo
Exercise 3.2
Requirement: https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/mailroom-part1.html
'''

donors = [("Alex Sotelo", [175, 180]), ("Juan Hirano", [200]), ("Elon Musk", [12500, 14000, 19000]),
          ("Akira Toriyama", [20, 80, 120]), ("Charles Darwin", [10, 20]), ("Gordon Ramsey", [100000])]


def thank_you():
    while True:
        thanks_query = input(f"Welcome {username}! Either type 'list' to view the list of donors or your full name to "
                             f"make a donation. \n").title()
        if thanks_query == 'List':
            print("Here is a list of our donors:")
            for donor in donors:
                print(donor[0])
            break
        elif thanks_query in ["Exit", "Cancel", "Quit", "Bye", "Stop"]:
            return
        elif len(thanks_query.split()) > 1:
            for donor in donors:

                if donor[0] == thanks_query:
                    try:
                        re_donate = int((input(f"Welcome back, {thanks_query}, how much would you like to "
                                               f"donate this time? \n")))
                        if re_donate <= 0:
                            print("Please don't waste our time. \n")
                            break
                        else:
                            donor[1].append(re_donate)
                            print(
                                f"Hey {thanks_query}, you're awesome. \n"
                                f"We appreciate you donating ${re_donate}. \n"
                                f"So far, you've given us ${sum(donor[1])}. \n"
                                f"Y U No give more? \n")
                            return
                    except ValueError:
                        print("Sorry, please type a number. Try again. \n")
                        break
            else:
                new_donor = int((input(f"Hey {thanks_query}, thank you for your interest in "
                                       f"donating for the first time. \n"
                                       f"How much would you like to donate? \n" )))
                if new_donor <= 0:
                    print("Please don't waste our time. \n")
                    break
                else:
                    donors.append((thanks_query, [new_donor]))
                    print(
                        f"Hey {thanks_query}, you're awesome. \n"
                        f"We appreciate you donating ${new_donor} for the first time. \n"
                        f"Y U No give more? \n")
                    return
        elif len(thanks_query.split()) == 1:
            print(f"Hey {thanks_query.title()}, please type your full name -- that means first AND last name. \n")
            continue
        else:
            print(f"Please type something. Literally anything. \n")
        continue

def create_report():
    headers = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
    print(f"Welcome {username}! Here is your report. \n")
    print(f"{headers[0]:<25} | {headers[1]} | {headers[2]} | {headers[3]}")
    print("-"*66)
    for data in donors:
        print(f"{data[0]:<25} | ${float(sum(data[1])):>10} | {len(data[1]):>9} | "
              f"${(float(sum(data[1]))/len(data[1])).__round__(2):>11}")

def main():
    while True:
        response = input(
            "\nWelcome to the Pythongs local charity. \nPlease choose a function:\n\n"
            "A -- Send a Thank You\n"
            "B -- Create a Report\n"
            "C -- Quit\n").title()
        if response == "A":
            thank_you()
        elif response == "B":
            create_report()
        elif response == "C" or "Quit":
            exit()
        else:
            print("Not a valid option!")

if __name__ == '__main__':
    main()