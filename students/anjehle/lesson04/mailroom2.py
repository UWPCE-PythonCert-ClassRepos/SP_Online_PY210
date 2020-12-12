# ----------------------------------------------- #
# Title: Mailroom
# Dev: Alex Jehle
# Desc: This script logs and displays donors and
#       their donation histories
# Change Log: Jehle, Alex 11/1/2020 - created
# ----------------------------------------------- #
import tempfile
import os
donor_list = {"Ben Wyatt": [1663.23, 4300.87, 10432.0],
              "Ron Swanson": [100000],
              "April Ludgate": [10, 1.52, 0.25],
              "Ann Perkins": [100, 100],
              "Leslie Knope": [1663.23, 4300.87, 1432.0]}


def thank_you(donors):
    entry = input("Input Full Name: ")

    if entry.lower() == 'list':
        print_list(donors)
    else:
        donor_name = entry.split()
        amount = float(input("What is the donation amount?: $"))
        add_donor = {"full_name": entry, "first_name": donor_name[0],
                     "amount": amount}
        add_donation(add_donor, donors)
        thank_you = print_thank_you(add_donor)
        print(thank_you)
    return donors


def create_report(donors):
    donors_summed = sum_donors(donors)
    print_report(donors_summed)
    return donors


def thank_you_dump(donors):
    td = tempfile.gettempdir()
    os.chdir(td)
    for person in donors:
        outfile = person.replace(" ", "_") + ".txt"
        donor_name = person.split()
        print_donor = {"first_name": donor_name[0], "amount": donors[person][-1]}
        thank_you = print_thank_you(print_donor)
        with open(outfile,'w') as f:
            f.write(thank_you)
    print(f'Files can be found at: {td}')
    return donors


def save_exit(donors):
    print('Goodbye!')
    return False


def add_donation(new_donor: dict, donor_history: dict):
    name = new_donor['full_name']
    if name in donor_history.keys():
        donor_history[name].append(int(new_donor['amount']))
    else:
        donor_history[name] = [new_donor['amount']]
    return donor_history


def print_thank_you(donor: dict):
    thank_you = "Dear {first_name},\n\tThank you for your generous donation of ${amount:.2f}! " \
                "Each dollar you donate ends up providing endless value for our town. \n\t" \
                "We appreciate your gift and hope our partnership extends well into the future. \n" \
                "Regards, \n\tThe Pawnee Restoration Fund".format(**donor)
    return thank_you


def print_list(ls):
    for ele in ls:
        print(f'{ele[0]}')
    print("\n")
    return


def sum_donors(donor_dict: dict):
    donor_rep = []
    for donor in donor_dict:
        tot = 0
        num = 0
        for donation in donor_dict[donor]:
            tot += donation
            num += 1
        avg = tot/num
        donor_add = [donor, tot, num, avg]
        donor_rep.append(donor_add)
    donor_rep.sort(reverse=True, key=lambda x: x[1])
    return donor_rep


def print_report(report):
    print(report)
    print(f"{'Name' :<20}|{'Total Donated' :^20}|{'Number of Donations' :^20}|{'Average Donation' :^20}\n"
          f"-------------------------------------------------------------------------")
    for donor in report:
        print(f"{donor[0] : <20}${donor[1] :^20,.2f}{int(donor[2]) : ^20}${donor[3] : =20.2f}")
    return

if __name__ == "__main__":
    arg_dict = {
        1: thank_you,
        2: create_report,
        3: thank_you_dump,
        4: save_exit
    }
    while True:
        # Display a menu of choices to the user
        choice = input('\nMenu of Options \n 1) Send a Thank You \n 2) Create a Report '
                       '\n 3) Send letters to all donors \n 4) Quit'
                       '\nWhich option '
                       'would you like to perform? \n')
        try:
            donor_list = arg_dict.get(int(choice))(donor_list)
        except KeyError:
            print('Invalid choice entered :(')
            continue
        if not donor_list:
            break