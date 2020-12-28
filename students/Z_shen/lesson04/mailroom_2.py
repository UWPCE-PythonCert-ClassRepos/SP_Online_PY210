import operator
donor = {'William Gates': [1500.99, 3500, 800.25],
         'Jeff Bezos': [145.72, 1350.25],
         'Paul Allen': [250.00, 57.00],
         'Mark Zuckerberg': [600.00],
         }


def sort_donor_total_given(donor):
    result = {}
    new_donor_order = {}
    for key, value in donor.items():
        result.update({key: sum(value)})
        sort = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
    for name, num in sort:
        new_donor_order[name] = num
    return new_donor_order


def donor_name_list(donor):
    donor_name = []
    print('The current list of names are:')
    for name in donor.keys():
        print(name)



def print_donor_report(donor):
    # sort_donor_total_given(donor)
    row = '| {name:20} | {sign_1:1}  {amount:>15,.2f} | {num_gifts:^10} | {sign_2:1} {avg_gift:>15,.2f} |'.format

    print('| {:20} | {:1}  {:^15} | {:^10} | {:1} {:^15} |'.format('Donor Name', ' ', 'Total Given', 'Num Gifts', '',
                                                                   'Average Gift'))
    print('-' * 78)
    for p in sort_donor_total_given(donor):
        print(row(name=p, sign_1='$', amount=sum(donor.get(p)), num_gifts=len(donor.get(p)), sign_2='$',
                  avg_gift=(sum(donor.get(p)) / len(donor.get(p)))))


def add_new_donor(name, num, donor):
    donor[name] = [num]
    return donor


def add_amount_same_name(name, num, donor):
    donor[name] += [num]
    return donor


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
        elif user_input not in sort_donor_total_given(donor):
            new_donor = input('Do you want to add {} as a new donor? (YES or NO) '.format(user_input.title()))
            if new_donor.lower() == 'back':
                return False
            elif new_donor.upper() == 'NO':
                continue
            else:
                thx_name = user_input
                add_new_donor(thx_name, float(thx_amount), donor)
                break
        else:
            thx_name = user_input
            add_amount_same_name(thx_name, float(thx_amount), donor)
            break
    thx = {'Name': thx_name, 'Donation': float(thx_amount)}
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
    for name in donor.keys():
        first, last = name.split()
        filename = first + '_' + last
        filename = '{}.txt'.format(filename)
        with open(filename, 'w') as file:
            file.write(f'''Dear {name},
        Thank you for your generous donation of ${sum(donor.get(name)):,.2f} to us.
        It will be put to very good use.

                            Sincerely,
                                -The Team
                                      ''')
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
