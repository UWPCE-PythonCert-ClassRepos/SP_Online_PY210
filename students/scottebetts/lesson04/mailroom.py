#!/usr/bin/env python
from time import strftime

donors = [['Tim Berners-Lee', 120000.00, 3, 40000.00],
          ['Ada Lovelace', 600.00, 2, 300.00],
          ['Marie Curie', 1000.00, 2, 500.00],
          ['Nicola Tesla', 20000.00, 4, 5000.00],
          ['Hans Holbein', 300.00, 3, 100.00]]


def menu_selection(prompt, dispatch_dict):
    while True:
        response = input(prompt)
        if dispatch_dict[response]() == "exit menu":
            break


def thanks_menu():
    menu_selection(thanks_prompt, thanks_dispatch)


def quit():
    print("Quitting this menu now")
    return "exit menu"


def add_donor():
    response = input("What's the donor's name?\n==>")
    names = []
    text_body = "Hello {},\n " \
                "Thanks very much for your generous donation of ${:.2f}"
    for d in donors:
        names.append(d[0])
    if response in names:
        new_donation = donors[names.index(response)]
        amount = float(input("Amount of new donation?\n==>"))
        new_donation[1] += amount
        new_donation[2] += 1
        new_donation[3] = amount
        donors[names.index(response)] = new_donation
    else:
        new_donation = []
        new_donation.append(response)
        new_donation.append(float(input("Amount of new donation?\n==>")))
        new_donation.append(1)
        new_donation.append(new_donation[1])
        donors.append(new_donation)
    print(
        text_body.format(new_donation[0], new_donation[-1])
    )
    return


def send_letters():
    for donor in donors:
        file_date = strftime("%Y%m%d")
        filename_format = "{}_{}.txt"
        donor_name = donor[0].replace(' ', '_')
        donor_file = filename_format.format(donor_name, file_date)
        with open(donor_file, 'w+') as outfile:
            outfile.write(
                "Dear {},\n "
                "Thanks for your recent gift of ${:>.2f}, "
                "you great big gullible maroon.".format(donor[0], donor[1]))
            outfile.close()
    print("Done!")
    return


def report():
    header = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    print('{:20}|{:^15}|{:^15}|{:^15}'.format(*header))
    dashy = "-" * 67
    print(dashy)
    report_donors = sorted(donors, key=sort_key, reverse=True)
    for donor in report_donors:
        print('{:20} ${:>13} {:>15}   ${:>11.2f}'.format(*donor))
    print("")
    return


def sort_key(d):
    return d[1]


def list_donors():
    print("\nDonors\n============")
    for d in donors:
        print(d[0])
    print("============\n")
    return


main_prompt = ("\nYou're in the main menu now!\nChoose an action!\n"
               "1 - run a report\n"
               "2 - list donors\n"
               "3 - thank donors\n"
               "or q to exit\n>>\n"
               )
main_dispatch = {"1": report,
                 "2": list_donors,
                 "3": thanks_menu,
                 "q": quit,
                 }
thanks_prompt = ("\nYou are now in the thanks prompt\n"
                 "1 - list donors\n"
                 "2 - add donors\n"
                 "3 - write letter\n"
                 "4 - return to prompt\n>>"
                 )
thanks_dispatch = {"1": list_donors,
                   "2": add_donor,
                   "3": send_letters,
                   "4": quit,
                   }

if __name__ == '__main__':
    menu_selection(main_prompt, main_dispatch)
