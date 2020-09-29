#!/usr/bin/env python
# PY210 Lesson 3 Mailroom Assignment
# Jonathan Vu
#
# Properties
donor_donations = [("Bill Gates", [85, 100]),
                   ("Jeff Bezos", [65, 25, 55]),
                   ("Elon Musk", [15, 25]),
                   ("The Rock", [250, 125, 55]),
                   ("Kevin Hart", [30])]


# Support Functions
def get_donor_names():
    return tuple(x[0] for x in donor_donations)


def get_donor_donation():
    return tuple(x[1] for x in donor_donations)


def send_a_thank_you():
    print('\n----- Send a Thank You -----')
    prompt = "\n".join(('Please select from the options:',
                        '1: Type in the full name of a donor.',
                        '2: Type in ''list'' to see donors.',
                        '3: Type in a new donor name',
                        '>> '))
    user_action_TY = input(prompt)
    donor_list = get_donor_names()
    donation_list = get_donor_donation()

    if user_action_TY == 'list':
        print(donor_list)
        send_a_thank_you()
    else:
        donation = input('Donation Amount ($): ')
        try:
            donation = int(donation)
        except ValueError:
            print('Enter a numeric value!')
            donation = int(donation)

        if user_action_TY in donor_list:
            for donors in donor_donations:
                if donors[0] == user_action_TY:
                    donors[1].append(donation)
        elif user_action_TY not in donor_list:
            donor_donations.append((user_action_TY, [donation]))

        Email_Thanks = '{}, your donation of ${:.2f} is greatly appreciated.'
        print('\n----- Thank YOU! -----')
        print(Email_Thanks.format(user_action_TY, donation))


def create_a_report():
    donor_donations.sort(key=lambda x: -sum(x[1]))
    report = ["\nDonor Name        | Total Given | # Gifts | Average Gift\n" +
              "------------------------------------------------------------------"]
    for donor in donor_donations:
        sumation = sum(donor[1])
        length = len(donor[1])
        report.append(f"{donor[0]:<15}   ${sumation:>9.2f}   {length:>9d}     ${sumation / length:>10.2f}")
    report = '\n'.join(report)
    print(report)
    return report


# Main Function
if __name__ == '__main__':
    while True:
        print('\n----- Welcome to the Mailroom -----')
        user_prompt = "\n".join(('Please select from the options:',
                                 '1: Send thank you note',
                                 '2: Create report',
                                 '3: Quit',
                                 '>> '))

        user_action = input(user_prompt)

        if user_action == '1':
            send_a_thank_you()
        elif user_action == '2':
            create_a_report()
        elif user_action == '3':
            quit()
        else:
            print('Invalid input. Please choose 1, 2 or 3.')
