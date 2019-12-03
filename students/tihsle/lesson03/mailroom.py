#!/usr/bin/env python3

import sys

donors = [  ("William Gates, III", [65000.00,10.00]),
            ("Mark Zuckerberg", [1442.25, 4000.00, 5000.00]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [400.00, 200.0000, 10.00]),
            ("Joe Smithe", [1000.00, 2000.00])
            ]


def send_thank_you():
    #send a thank you

    #which donor
    donor = select_donor()

    #how much is the gift
    get_donation(donor)

    #print thank you email
    print("Dear {},\n"
          "\nThank you for donating!  Your generous donation will be used to fulfill our mission.\n"
          "We look forward to updating you on how your funds are used throughout the year.\n"
          "\nBest Regards,\n"
          "\nCharity1\n".format(donor))


def select_donor():
    #select the donor for the thank you email

    while True:
        answer = input("Which donor to send Thank You to?\n"
                         "(Type 'list' to show list of donors)\n").title()
        if answer.lower() == "list":
            for d in range(len(donors)):
                print("{}".format(*donors[d]))
        else:
            exists = False
            for donor, _ in donors:
                if donor == answer:
                    exists = True
            if exists:
                return answer
            else:

                new_donor = (answer, [])
                donors.append(new_donor)
                return answer

def get_donation(donor):
    # add the donation to the donors
    dnames = []
    donation = input("How much is the gift?\n")
    for d, _ in donors[:]:
        dnames.append(d)
    dindex = dnames.index(donor)
    donors[dindex][1].append(float(donation))


def create_report():
    #print a list of donors, sorted by total donations

    #sorted donors by total of gifts
    def sort_key(d):
        return sum(d[1])

    sdonors = sorted(donors, key=sort_key, reverse=True)

    #formatting
    head_form = "{:^20}|" * 4
    grid_form = "-" * 21 * 4
    print(head_form.format(
          "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print(grid_form)

    #print donors and their gifts
    for d in sdonors:
        dname = d[0]
        dtotal = sum(d[1])
        num_gifts = len(d[1])
        avg_gift = round(dtotal/num_gifts)
        print("{:20} ${:>18.2f} {:>21} ${:>18.2f}".format(
              dname, dtotal, num_gifts, avg_gift))


def quit():
    #quit the program
    sys.exit()


def main():
    #generate the menu
    menu = "\n".join((">>>",
                        "Please choose from the following:",
                        "1 - Send a Thank You",
                        "2 - Create a Report",
                        "3 - Quit",
                        ">>> "))
    while True:
        ans = input(menu)
        if ans == "1":
            send_thank_you()
        elif ans == "2":
            create_report()
        elif ans == "3":
            quit()
        else:
            print("Only 1, 2 or 3 is valid!")

if __name__ == "__main__":
    main()
