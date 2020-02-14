#!/usr/bin/env python3


donors_list = [
    ['Bubbles Trailer',[150, 25, 300]],
    ['Julien Park',[25, 86]],
    ['Ricky Boys',[7, 3, 5]],
    ['Jack Anderson',[1001, 22, 45]],
    ['Lacey Coffin Greene',[750, 325, 1050]]
    ]

def create_email(name, amount):
    print()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f"Hello {name},\n"
          f"Thank you for your gift of ${amount}! \n"
          f"We appreiate your gift to help with costs for our upcoming play! \n"
          f"Thank you for giving!\n"
          f"Best Regards, \n"
          f"The Blanchford Community Center!")
    print()


def donor_names():
    names = []
    for donors in donors_list:
        names.append(donors[0])
    return names


def name_check(x):
    count = len(donor_names())
    current = donor_names()
    start = 0
    while start < count:
        if x == current[start]:
            return(start)
        start = start + 1
    new_donor = [x,[]]
    donors_list.append(new_donor)
    return(count)


def donor_details(x):
    donor = x
    name = donor[0]
    donations = donor[1]
    num_donations = len(donor[1])
    totals = total_donated(donations)
    avg_donation = int(totals) / int(num_donations)
    print(name, totals, num_donations, avg_donation)
  #  return(name, totals, num_donations, avg_donation)



def total_donated(x):
    x = 0
    for i in x:
        x = x + i
        return(x)



def start():

    action = input("Select a number to perform one of the following actions...\n"
               "1. Send a Thank You Email \n"
               "2. Create a Report \n"
               "3. Quit \n")

    if action.isnumeric():
        action = int(action)
        if action > 3 or action < 1:
            print("Please select a number 1, 2 or 3")
            start()

        elif action == 1:
            send_thanks()

        elif action == 2:
            create_report()

        elif action == 3:
            print("Quitting program ....")
            exit()

    else:
        print("Please enter a numerical value")
        start()



def send_thanks():
    name = input("Please enter the full name of the donor or enter 'q' to quit\n")

    if name.upper() == 'Q':
        exit()

    elif name.upper() == "LIST":
        print(donor_names())
        send_thanks()

    donor_index = name_check(name)

    donation = input("Please enter a donation amount for {} or enter 'q' to quit ".format(name))

    if name.upper() == 'Q':
        exit()

    amount = int(donation)

    donor_info = donors_list[donor_index]

    donor_info[1].append(amount)

    create_email(name, amount)
    start()



def report_template(name, total, count, avg):
    x = name
    y = total
    c = count
    a = avg
    z = '{name}\t${total:^}\t{count:>}\t${avg:>}' \
        .format(name=x, total=y, count=c, avg=a)
    print(z)


def create_report():
    print()
    print('Donor Name                | Total Given | Num Gifts | Average Gift')
    print('------------------------------------------------------------------')
    donors = len(donors_list)

    for i in donors_list:
       donor_details(i)
        #print(x)
        #report_template(x[0],x[1],x[2],x[3])
    print()
    start()











start()