
from operator import itemgetter
import sys


def menu(donors):
    while True:
        print()
        print('''Menu:
                    1. Send a Thank You.

                    2. Send all Thank You's

                    3. Create a Report.

                    4. Quit.''')
        print()
        try:
            response = int(input("Please enter a number to make your selection. "))-1
            switch_func_dict = {0: ask_donor_name, 1: multi_thanks, 2: totals, 3: quit_now}
            switch_func_dict[response](donors)
        except KeyError:
            print("Please enter a menu option from 1-4.")


def quit_now(ignore):
    print('bye')
    sys.exit(0)


def list_donors(donors):
    result = ''
    for item in donors:
        result += f'{item}\n'
    return result


def ask_donor_name(donors):
    # While collecting user input.
    while True:
        # Did not put a try except here since names can be very short, have spaces, or have dashes. 
        # I wasn't sure how to address that.
        donor_name = input("Enter the full name of the donor. (or q to quit) ")
        if donor_name == 'q':
            return
        # If user types list print donors
        elif donor_name.upper() == "LIST":
            print(list_donors(donors))
            continue
        else:  # user didn't type list
            donation(donor_name, donors)
            return


def donation(donor_name, donors, donation_amount=None):
    try:
        if donation_amount is None:
            donation_amount = input("Enter the donation amount (or q to quit) ")
        if donation_amount == 'q':
            return
        else:
            donation_amount = float(donation_amount)
            for name, donations in donors.items():
                if name == donor_name:
                    donations.append(donation_amount)
                    break
            else:
                donors[donor_name] = [donation_amount]
            send_thank_you(donor_name, donation_amount)
    except ValueError:
        print('Some value error')


def send_thank_you(donor_name, donation_amount):
    result = f'Thank you {donor_name} for your donation of ${donation_amount:.2f}. We appreciate your generous support of our club.\n'
    print(result)
    return result


def multi_thanks(donors):
    for named_dict in [{"donor_name": n, "total": sum(d)} for n, d in donors.items()]:
        with open('{donor_name}.txt'.format(**named_dict), 'w') as f:
            f.write(generate_letter(named_dict))
    print('Created letters')


def generate_letter(values):
    return 'Thank you {donor_name}. You have donated a total of ${total}. We appreciate your generous support for our club.'.format(**values)


# Create Report


def totals(donors):
    # n = name and d = donations   
    output_list = [(n, sum(d), len(d), sum(d) / len(d)) for n, d in donors.items()]
    sorted_output = sorted(output_list, key=itemgetter(2), reverse=True)
    print(create_report(sorted_output))
    return sorted_output


def create_report(sorted_output):
    result = "\n"
    result += 'Donor Name                | Total Given | Num Gifts | Average Gift\n'
    result += '-'*66 + '\n'
    for name, total_given, number_gifts, average_gift in sorted_output:
        result += f'{name:<27}${total_given:>11.2f}{number_gifts:>12}  ${average_gift:>11.2f}\n'
    return result


if __name__ == "__main__":
    donors = {'Sandy Pie': [75],
              'Judy Smith': [75, 100, 1000],
              'Mike Jones': [75, 1000],
              'Joe Smith': [75, 100, 2000],
              'Kelly Blue': [75, 150, 275]}

    menu(donors)
