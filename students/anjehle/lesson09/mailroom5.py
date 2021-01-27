# --------------------------------------------------------------------------- #
# Title: Mailroom
# Dev: Alex Jehle
# Desc: This script logs and displays donors and
#       their donation histories
# Change Log: Jehle, Alex 11/1/2020 - created
# Change Log: Jehle, Alex 11/28/2020 - updated w/ dicts and added menu option 3
# Change Log: Jehle, Alex 12/19/2020 - updated w/ excepts and list comprehension
# Change Log: Jehle, Alex 12/20/2020 - refactored to incorporate testing suite
# Change Log: Jehle, Alex 01/17/2021 - updated to incorporate classes
# --------------------------------------------------------------------------- #
import tempfile
import os


class Donor:
    def __init__(self, full_name, donations):
        self.full_name = full_name
        self.donations = donations

    @property
    def first_name(self):
        return self.full_name.split()[0]

    @property
    def name(self):
        donor_name = self.full_name.split()
        donor_name = [name.capitalize() for name in donor_name]
        name_add = ''
        for x in donor_name[0:-1]:
            name_add = name_add + str(x) + " "
        return name_add + donor_name[-1]

    @property
    def donor_report(self):
        num = len(self.donations)
        tot = sum(self.donations)
        avg = tot / num
        return [self.name, tot, num, avg]

    def save_file(self, temp_dir):
        os.chdir(temp_dir)
        thank_you_print = self.generate_thank_you()
        save_name = self.name.replace(" ", "_") + ".txt"
        with open(save_name, 'w') as f:
            f.write(thank_you_print)
        return

    def add_donation(self, amount):
        self.donations.append(int(amount))
        return

    def generate_thank_you(self):
        thank_you_print = f"Dear {self.first_name},\n\tThank you for your generous donation of " \
                          f"${self.donations[-1]:.2f}! Each dollar you donate ends up providing endless value for" \
                          f" our town. \n\t We appreciate your gift and hope our partnership extends well into the " \
                          f"future. \nRegards, \n\tThe Pawnee Restoration Fund"
        return thank_you_print


# --------------------------------------------------------------------------------- #
class DonorCollection:
    def __init__(self, donors):
        self.donors = donors

    def print_list(self):
        for name, donor in self.donors.items():
            print(f'{donor.name}')
        print("\n")
        return

    def check_donor(self, name):
        return name in self.donors.keys()

    def add_donor(self, new_donor):
        self.donors[new_donor.name] = new_donor
        return

    @property
    def printed_report(self):
        reports = [d.donor_report for d in self.donors.values()]
        reports.sort(reverse=True, key=lambda x: x[1])

        print_report = [f"{'Name' :<20}|{'Total Donated' :^20}|{'Number of Donations' :^20}|"
                        f"{'Average Donation' :^20}\n---------------------------------------"
                        f"-------------------------------------------"]
        for donor_report in reports:
            print_report.append(f"{donor_report[0] : <20}${donor_report[1] :^20,.2f}{int(donor_report[2]) : ^20}"
                                f"${donor_report[3] : =20.2f}")
        return print_report

    def print_report(self):
        for line in self.printed_report:
            print(line)

    def thank_you_dump(self):
        td = tempfile.gettempdir()
        for donor in self.donors.values():
            donor.save_file(td)
        print(f'Files can be found at: {td}')
        return


# --------------------------------------------------------------------------------- #
def thank_you():
    entry = input("Input Full Name: ")
    if entry.lower() == 'list':
        ds.print_list()
    else:
        try:
            amount = [float(input("What is the donation amount?: $"))]
            if ds.check_donor(entry):
                d = ds.donors[entry]
                d.add_donation(amount[0])
            else:
                d = Donor(entry, amount)
                print(d)
                ds.add_donor(d)
            print(d.generate_thank_you())
        except (ValueError, TypeError):
            print('Please enter amount as a number\n')
            thank_you()
    return


if __name__ == "__main__":
    ds = DonorCollection({})
    ds.add_donor(Donor("Ben Wyatt", [1663.23, 4300.87, 10432.0]))
    ds.add_donor(Donor("Ron Swanson", [100000]))
    ds.add_donor(Donor("April Ludgate", [10, 1.52, 0.25]))
    ds.add_donor(Donor("Ann Perkins", [100, 100]))
    ds.add_donor(Donor("Leslie Knope", [1663.23, 4300.87, 1432.0]))

    arg_dict = {
        1: thank_you,
        2: ds.print_report,
        3: ds.thank_you_dump,
    }
    while True:
        # Display a menu of choices to the user
        choice = input('\nMenu of Options \n 1) Send a Thank You \n 2) Create a Report '
                       '\n 3) Send letters to all donors \n 4) Quit'
                       '\nWhich option '
                       'would you like to perform? \n')
        try:
            choice = int(choice)
        except TypeError:
            print('Please enter an integer')
        if choice == 4:
            print('Goodbye!')
            break
        else:
            try:
                arg_dict[choice]()
            except KeyError:
                print('Key: Please enter a number 1-4')
        continue
