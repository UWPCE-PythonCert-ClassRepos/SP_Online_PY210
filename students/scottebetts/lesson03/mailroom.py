#!/usr/bin/env python

donors = [['Tim Berners-Lee', 120000.00, 3, 40000.00],
          ['Ada Lovelace', 600.00, 2, 300.00],
          ['Marie Curie', 1000.00, 2, 500.00],
          ['Nicola Tesla', 20000.00, 4, 5000.00],
          ['Hans Holbein', 300.00, 3, 100.00]]

def prompt():
    while True:
        response = input("What would you like to do?\n1. Send a Thank You\n2. Create Report\n3. Quit\n==>")

        if response == "1":
            thanks()
            break
        elif response == "2":
            report()
        elif response == "3":
            break
        else:
            print("Invalid response, please try again...")
            prompt()
    return

def add_donor():
    response = input("What's the donor's name?\n==>")
    names = []
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
    print("Hello {},\n Thanks very much for your generous donation of ${:.2f}".format(new_donation[0], new_donation[-1]))
    return

def report():
    header = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    print('{:20}|{:^15}|{:^15}|{:^15}'.format(*header))
    dashy = "-"*67
    print(dashy)
    report_donors = sorted(donors, key=sort_key, reverse=True)
    for donor in report_donors:
        print('{:20} ${:>13} {:>15}   ${:>11.2f}'.format(*donor))
    print("")
    return

def sort_key(d):
    return d[1]

def thanks():
    while True:
        response = input("1. List donors\n2. Select Donor\n3. Return to prompt\n4. Quit\n==>")
        if response == "1":
            list_donors()
        elif response == "2":
            add_donor()
        elif response == "3":
            prompt()
            break
        elif response == "4":
            break
        else:
            print("Invalid response, please try again...")
    return

def list_donors():
    print("\nDonors\n============")
    for d in donors:
        print(d[0])
    print("============\n")
    return

if __name__ == '__main__':
    prompt()
