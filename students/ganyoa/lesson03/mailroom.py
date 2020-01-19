import sys

#main menu; selection will guide the 'main' function
prompt = "\n".join(("\n""Mailroom options",
          " Please choose from below options:",
          " 1 - Send a Thank You",
          " 2 - Create a Report",
          " 3 - Quit",
          ">>> "))

#list of current donor and donation amounts
donor_list = [("Mouth Devereaux", [4562.58, 3817.39]),
            ("Mikey Walsh", [618.45, 49.20, 542.87]),
            ("Andy Carmichael", [75.28, 99.25]),
            ("Chester Copperpot", [750254.00, 802154.11, 1.75]),
            ]


def average(donor_ave):
    #calculates donation averages per donor
    return (sum(donor_ave) / len(donor_ave))

def total_donated(don_amts):
    #calculates the total donation amount per donor
    return sum(don_amts[1])

def thank_you():
    #input option for the user to enter a new name, add amount to previous donor, or see list of previous donors
    donor_name = input("Enter donors full name (type 'list' to display all names)? > ").title()

    #if user does not enter a name or 'list' they will be brought back to the main menu
    if donor_name == '':
        main()

    #displays previous donor list
    if donor_name == 'List':
        for i in range(len(donor_list)):
            print(donor_list[i][0])
        main()
    match = 0

    #iterate through donor list, add new name and amount, or amount if the name was already on the list
    for i in range(len(donor_list)):
        if donor_name == donor_list[i][0]:
            match = i
            break
    else:
        donor_list.append((donor_name,[]))
        match = i + 1
    donation_amt = input("\n""How much did " + donor_name + " donate? > ")
    amt = round(float(donation_amt),2)
    donor_list[match][1].append(amt)

    #display a default thank you note addressed to the donor
    print('\n'.join(('\n''Dear ' + donor_name + ','+ '\n',
          'Thank you for your generous donation of $' + donation_amt + '.',
          'Your commitment goes a long way in helping us',
          'solve things that need to be solved.' + '\n',
          'Warm regards,' + '\n',
          'Mama Fratelli')))


def create_report():
    #display report of all donor with summed and sorted donation amounts
    print('{:20}{:15}{:15}{:15}'.format('Donor Name', '| Total Given', '| Num Gifts', '| Average Gift'))
    print('-' * 65)
    s_list = sorted(donor_list, key=total_donated, reverse=True)
    for i in range(len(s_list)):
        print(f'{s_list[i][0]:<20} $ {sum(s_list[i][1]):<13.2f} {len(s_list[i][1]):<13} $ {average(s_list[i][1]):<15.2f}')


def quit_program():
    #exit the function
    print("Bye!")
    sys.exit()  # exit the interactive script


def main():
    #the user directed prompt above is used to call the designated function
    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "1":
            thank_you()
        elif response == "2":
            create_report()
        elif response == "3":
            quit_program()
        else:
            print("Not a valid option!")


#confirm file is executed on it's own in the main program, or being imported
if __name__ == "__main__":
    main()