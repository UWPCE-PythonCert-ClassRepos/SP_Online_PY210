
from fuckaround import Donor, Donor_Collection
import sys


def mainy():
    while True:
        try:
            choice = int(input('''
Welcome to the main MAILROOM option menu:
1 - Initiate Grovel Sequence
2 - Data Metrics 3000
3 - Quit
4 - Send thank you notes to all donors
Indicate your choice:'''))
            swit_dic = {1: input_name, 3: exit_program, 2:data_metrics}
            # 2: data_metrics,
            #             3: exit_program, 4: mass_mail}
            swit_dic[choice]()
        except KeyError:
            print("\n"+'You have entered a non-choice'
                  ', please get your life together')
        except ValueError:
            print("\n"+'You have entered a non-number'
                  ', please get your life together')


def input_name():
    while True:
        name = input("Enter donor name or enter 'list' for extant donors: ")
        if name == 'list':
            for x in dc.donor_names:
                print(x)
        else:
            verify_name(name)


# I know this breaks DRY
def verify_name(name):
    names = []
    for obj in dc.donors:
        names.append(obj.name.upper())
    if name.upper() in names:
        while True:
            don = input(f'{name} is a known donor, continue Y/N?')
            if don.upper() == 'Y':
                don_amount = float(input(f"how much is ol' {name} donating?:"))
                name = Donor()
                Donor.add_donation(don_amount)
                mainy()
                if don.upper() == 'N':
                    return
    if name not in names:
        while True:
            don = input(f'{name} is an unknown donor, continue Y/N?')
            if don.upper() == 'Y':
                don_amount = float(input(f"how much is {name} donating?: "))
                Donor(name, [don_amount])
                dc.add_donor(Donor(name, [don_amount]))
                mainy()
            if don.upper() == 'N':
                return


def data_metrics():
    for x in dc.donors:
        print(x.name, x.donations)


# Option 3: get out of this program
def exit_program():
    print("Bye!")
    sys.exit()  # THIS IS TO EXIT THE PROGRAM AND START OVER


if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically
    # if this module is imported
    # collection = load_donors()
    dc = Donor_Collection()
    mainy()
