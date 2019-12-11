#!/usr/bin/env python3

import sys

donors =    {"William Gates, III": [65000.00,10.00],
            "Mark Zuckerberg": [1442.25, 4000.00, 5000.00],
            "Jeff Bezos": [877.33],
            "Paul Allen": [400.00, 200.0000, 10.00],
            "Joe Smithe": [1000.00, 2000.00]
            }


def send_thank_you():
    #send a thank you

    #which donor
    donor = select_donor()

    #exception handling for user input
    loop = True
    while loop:
        donation = input("How much is the gift?\n")
        try:
            if float(donation):
                break
        except ValueError:
            print("\nNot a good value!\n")

    if donor in donors.keys():
        donors[donor].append(float(donation))
    else:
        add_donor(donor, donation)

    #print thank you email
    print(get_thankyou_text(donor))

def add_donor(donor, donation):
    donors[donor] = [float(donation)]

def select_donor():
    #select the donor for the thank you email

    while True:
        answer = input("Which donor to send Thank You to?\n"
                         "(Type 'list' to show list of donors)\n").title()
        if answer.lower() == "list":
            print(get_donor_list())
        else:
            break
    return answer

def get_donor_list():
    strList = ""
    for d in donors:
        strList = strList + "{}\n".format(d)
    return strList

def send_letters():
    for d in donors:
        with open(f'{d}.txt', 'w') as f:
            f.write(get_thankyou_text(d))

def get_thankyou_text(name):
    strLetter = "\n".join(("Dear {},\n".format(name),
      "\nThank you for donating!  Your generous donation will be used to fulfill our mission.\n",
      "We look forward to updating you on how your funds are used throughout the year.\n",
      "\nBest Regards,\n",
      "\nCharity1\n"))
    return strLetter

def create_report():
    #print a list of donors, sorted by total donations

    #sorted donors by total of gifts
    def sort_key(d):
        return sum(donors[d])

    sdonors = sorted(donors, key=sort_key, reverse=True)

    #formatting
    head_form = "{:^20}|" * 4
    grid_form = "-" * 21 * 4
    print(head_form.format(
          "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print(grid_form)

    #print donors and their gifts
    for d in sdonors:
        print(get_report_line(d))

def get_report_line(d):
    dname = d
    dtotal = sum(donors[d])
    num_gifts = len(donors[d])
    avg_gift = round(dtotal/num_gifts)
    strLine = "{:20} ${:>18.2f} {:>21} ${:>18.2f}".format(dname, dtotal, num_gifts, avg_gift)
    return strLine

def quit():
    #quit the program
    sys.exit()


def main():
    #generate the menu
    menu = "\n".join((">",
                        "Please choose from the following:",
                        "1 - Send a Thank You to a single donor",
                        "2 - Create a Report",
                        "3 - Send letters to all donors",
                        "4 - Quit",
                        "> "))

    selections = {"1": send_thank_you, "2": create_report,
                    "3": send_letters, "4": quit}

    while True:
        ans = input(menu)
        try:
            selections.get(ans)()
        except TypeError:
            print("Only 1, 2, 3 or 4 is valid!")
            pass

if __name__ == "__main__":
    main()
