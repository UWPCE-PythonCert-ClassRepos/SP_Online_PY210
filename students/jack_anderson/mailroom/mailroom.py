#!/usr/bin/env python3


donors_list = [
    ['Bubbles Trailer',[150, 25, 300]],
    ['Julien Park',[25, 86]],
    ['Ricky Boys',[7, 3, 5]],
    ['Jack Anderson',[1001, 22, 45]],
    ['Lacey Coffin Greene',[750, 325, 1050]]
    ]


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
    prompt_name = input("Please enter the full name of the donor \n")

    if prompt_name.upper() == "LIST":
        print(donor_names())
        send_thanks()

    donorIndex = name_check(prompt_name)
    donation = input("Please enter a donation amount for {}  ".format(prompt_name))
    amount = int(donation)
    donorInfo = donors_list[donorIndex]
    donorInfo[1].append(amount)
    totalDonations = len(donorInfo[1])
    print()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f"Hello {prompt_name},\n"
          f"Thank you for your gift of ${amount}! \n"
          f"We have received a total of {totalDonations} donations from you so far! Thanks for your kindness!\n"
          f"Best Regards, \n"
          f"The Blanchford Community Center!")
    print()

    start()




def create_report():
    print("this is report option")
    print(donors_list)
    start()


start()