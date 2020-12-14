donor = [
    {'Name': 'William Gates', 'Donation': 653772.32, 'number_don': 2},
    {'Name': 'Jeff Bezos', 'Donation': 163960000.10, 'number_don': 3},
    {'Name': 'Paul Allen', 'Donation': 877.33, 'number_don': 1},
    {'Name': 'Mark Zuckerberg', 'Donation': 708.42, 'number_don': 3},
]


def sort_donor_total_given(donor):
    donor.sort(key=lambda x: x['Donation'], reverse=True)
    return donor


def donor_name_list(donor):
    donor_name = []
    print('The current list of names are:')
    for i in donor:
        row = i['Name']
        print(row)
        donor_name.append(row)
    return donor_name


def print_donor_report(donor):
    sort_donor_total_given(donor)
    row = '| {name:20} | {sign_1:1}  {amount:>15,.2f} | {num_gifts:^10} | {sign_2:1} {avg_gift:>15,.2f} |'.format

    print('| {:20} | {:1}  {:^15} | {:^10} | {:1} {:^15} |'.format('Donor Name', ' ', 'Total Given', 'Num Gifts', '',
                                                                   'Average Gift'))
    print('-' * 78)
    for p in donor:
        print(row(name=p['Name'], sign_1='$', amount=p['Donation'], num_gifts=p['number_don'], sign_2='$', avg_gift=int(p['Donation']) / int(p['number_don'])))


def add_new_donor(name, amount, times, donor):
    new_donor = {'Name': name, 'Donation': amount, 'number_don': times}
    donor.append(new_donor)
    return donor


def count_times(thx_name, donor):
    for i in range(0, len(donor)):
        if thx_name == donor[i]['Name']:
            donor[i]['number_don'] = int(donor[i]['number_don']) + 1
            number = donor[i]['number_don']
    return number

def total_given(thx_name, thx_amount, donor):
    for i in range(0, len(donor)):
        if thx_name == donor[i]['Name']:
            donor[i]['Donation'] = float(donor[i]['Donation']) + float(thx_amount)
            thx_amount = donor[i]['Donation']
    return thx_amount


def thank_you_letter(donor):
    while True:
        user_input = str(input('''What is the name of donor? or type 'list' to see the current list: ''')).title()
        if user_input.lower() == 'back':
            return False
        elif user_input.lower() == 'list':
            donor_name_list(donor)
            continue
        thx_amount = input('How much did ' + user_input + ' donate? $ ')
        if str(thx_amount.lower()) == 'back':
            return False
        elif user_input not in donor_name_list(donor):
            new_donor = input('Do you want to add {} as a new donor? (YES or NO) '.format(user_input.title()))
            if new_donor.lower() == 'back':
                return False
            elif new_donor.upper() == 'NO':
                continue
            else:
                thx_name = user_input
                times = 1
                add_new_donor(thx_name, float(thx_amount), times, donor)
                break
        else:
            thx_name = user_input
            count_times(thx_name, donor)
            total_given(thx_name, thx_amount, donor)
            break
    thx={'Name': thx_name, 'Donation': float(thx_amount)}
    print('\nEMAIL CONTENT: \n')
    print('''Dear {Name}, 
    Thank you for your generous donation of ${Donation:,.2f} to us.
    It will be put to very good use.
        
                        Sincerely,
                            -The Team
                                      '''.format(**thx))


def print_menu_task():
    print('''
    Menu of Options
    1) Send a Thank You letter to a single donor
    2) Create a Report
    3）Send letters to all donors
    4) Quit
    Note: You can type 'back' to return to Main Menu
    ''')
    print()


def input_menu_choice():
    choice = int(input('Which choice would you to perform? [1 to 4]: '))
    print()
    return choice


def exit_program():
    print('Exit the Program')


def send_letters_to_all(donor):
    for i in range(0, len(donor)):
        first, last = donor[i]['Name'].split()
        filename = first + '_' + last
        filename = '{}.txt'.format(filename)
        with open(filename, 'w') as file:
            file.write('''Dear {Name},
        Thank you for your generous donation of ${Donation:,.2f} to us.
        It will be put to very good use.

                            Sincerely,
                                -The Team
                                      '''.format(**donor[i]))
    print('Thank you letter(s) sent')


while __name__ == '__main__':
    print_menu_task()
    number = input_menu_choice()
    if number == 1:
        thank_you_letter(donor)
    elif number == 2:
        print_donor_report(donor)
    elif number == 3:
        send_letters_to_all(donor)
    elif number == 4:
        exit_program()
        break
