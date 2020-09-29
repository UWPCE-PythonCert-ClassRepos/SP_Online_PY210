
from operator import itemgetter
import sys

donors = {'Sandy Pie' : [75],
          'Judy Smith': [75, 100, 1000],
          'Mike Jones': [75, 1000],
          'Joe Smith' : [75, 100, 2000],
          'Kelly Blue': [75, 150, 275]}


def menu():
    while True:
        print()
        print('''Menu:
                    1. Send a Thank You.

                    2. Send all Thank You's

                    3. Create a Report.

                    4. Quit.''')
        print()
        response = int(input("Please enter a number to make your selection. "))-1

        switch_func_dict = {0: ask_donor_name, 1: multi_thanks, 2: totals, 3: quit_now}
        
        switch_func_dict[response]()


def quit_now():
    # sys.exit throws a exception in debug mode in vscode.
    sys.exit()
    

def list_donors():
    for item in donors:
        print(f'{item[0]}')


def ask_donor_name():

    # While collecting user input.
    while True:
        donor_name = input("Enter the full name of the donor. (or q to quit) ")

        if donor_name == 'q':
            return
        # If user types list print donors
        elif donor_name.upper() == "LIST":
            list_donors()
            continue
        else:  # user didn't type list
            donation(donor_name)
            return


def donation(donor_name):
    donation_amount = input("Enter the donation amount (or q to quit) ")
    if donation_amount == 'q':
        return
    else:
        donation_amount = int(donation_amount)
        for name, donations in donors.items():
            if name == donor_name:
                donations.append(donation_amount)
                break
        else:
            donors[donor_name] = [donation_amount]

        send_thank_you(donor_name, donation_amount)


def send_thank_you(donor_name, donation_amount):
    print(f'Thank you {donor_name} for your donation of ${donation_amount}. We appreciate your generous support of our club.')
    print()



def multi_thanks():
    # In order to do the .format(**dict), I converted my dictionary to list of dictionaries. Otherwise refactor everything.
    named_list = []
    for item in donors.items():
        named_list.append({'donor_name': item[0], 'total': str(sum(item[1]))})
    for named_dict in named_list:
        with open('{donor_name}.txt'.format(**named_dict), 'w') as f:
            f.write('Thank you {donor_name}. You have donated a total of ${total}. We appreciate your generous support for our club.'.format(**named_dict))
    print('Created letters')
# Create Report


def totals():
    output_list = []
    for name, donations in donors.items():
        total_given = sum(donations)
        number_gifts = len(donations)
        average_gift = sum(donations)/len(donations)
        output_list.append((name, total_given, number_gifts, average_gift))

    sorted_output = sorted(output_list, key=itemgetter(1), reverse=True)
    create_report(sorted_output)


def create_report(sorted_output):
    print()
    print('Donor Name                | Total Given | Num Gifts | Average Gift')
    print('-'*66)
    for name, total_given, number_gifts, average_gift in sorted_output:
        print(f'{name:<27}${total_given:>11.2f}{number_gifts:>12}  ${average_gift:>11.2f}')
    return


if __name__ == "__main__":
    menu()
