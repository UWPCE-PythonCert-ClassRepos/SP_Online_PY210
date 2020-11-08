# ----------------------------------------------- #
# Title: Mailroom
# Dev: Alex Jehle
# Desc: This script logs and displays donors and
#       their donation histories
# Change Log: Jehle, Alex 11/1/2020 - created
# ----------------------------------------------- #
donor_list = [("Ben Wyatt", [1663.23, 4300.87, 10432.0]),
              ("Ron Swanson", [100000]),
              ("April Ludgate", [10, 1.52]),
              ("Ann Perkins", [100, 100]),
              ("Leslie Knope", [1663.23, 4300.87, 1432.0])]


def add_donation(name, donor_history):
    amount = float(input("What is the donation amount?: $"))
    donor_names = [donor[0] for donor in donor_history]
    if name in donor_names:
        donor = donor_history[donor_names.index(name)]
        donor[1].append(int(amount))
    else:
        donor_add = (name, [amount])
        donor_history.append(donor_add)
    return donor_history


def print_thank_you(name):
    print(f'Dear {name},\n Thank you for your generous donation! Each dollar you donate ends up'
          f'providing endless value for our town. \n We appreciate your gift and hope our '
          f'partnership extends well into the future. \n Regards, \n The Pawnee Restoration Fund')
    return


def print_list(ls):
    for ele in ls:
        print(f'{ele[0]}')
    print("\n")
    return


def sum_donors(donor_ls):
    donor_rep = []
    for donor in donor_ls:
        name = donor[0]
        tot = 0
        num = 0
        for donation in donor[1]:
            tot += donation
            num += 1
        avg = tot/num
        donor_add = [name, tot, num, avg]
        donor_rep.append(donor_add)
    donor_rep.sort(reverse=True, key=lambda x: x[1])
    return donor_rep


def print_report(report):
    print(f"{'Name' :<20}|{'Total Donated' :^20}|{'Number of Donations' :^20}|{'Average Donation' :^20}\n"
          f"-------------------------------------------------------------------------")
    for donor in report:
        print(f"{donor[0] : <20}${donor[1] :^20,.2f}{int(donor[2]) : ^20}${donor[3] : =20.2f}")


if __name__ == "__main__":
    while True:
        # Display a menu of choices to the user
        choice = input('Menu of Options \n 1) Send a Thank You \n 2) Create a Report '
                       '\n 3) Quit \n Which option '
                       'would you like to perform? \n')
        if choice.strip() == '1':
            # Step 2
            # Add a new item to the List(Table) each time the user makes that choice
            entry = input("Input Full Name: ")
            if entry.lower() == 'list':
                print_list(donor_list)
            else:
                add_donation(entry, donor_list)
                print_thank_you(entry)

        elif choice.strip() == '2':
            # Display the data in the donor report each time the user makes that choice
            donor_report = sum_donors(donor_list)
            print_report(donor_report)
        elif choice.strip() == '3':
            # Exit the program
            print('Goodbye!' + '\n')
            break

        else:
            print('Invalid choice entered :(')
            continue
