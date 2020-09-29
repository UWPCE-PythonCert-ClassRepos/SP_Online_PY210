# !/usr/bin/env python3

import sys


def donars():
    return {'Mike': [200, 150, 50],
            'Tony': [150, 50, 250],
            'Sarah': [150, 150, 150],
            }


def menu_options():
    print("\n".join(("Please select from the following options:",
                     "s - Send a Thank You letter to a single donar.",
                     "c - Create a Report.",
                     "sa - Send letters to all donars.",
                     "q - Quit",
                     " >>> ")))
    prompt = input('')
    return prompt.lower()


def thank_you_message(donar):
    message = (f'\nDear {donar},'
               f'\n\nThank you for your generous donation of ${sum(donars_data.get(donar)):,.2f}.'
               '\nWe value your contribution and support.'
               '\n\nSincerely,\n\nNew Horizon Charity Director\n')
    return message


def donations(donar, amount):
    if donar not in donars_data:
        donars_data[donar] = [amount]
    else:
        donars_data[donar] += [amount]


def list_of_donars():
    lod = []
    for name in donars_data:
        lod.append(name)
    return '\n'.join(lod)


def send_thank_you():
    mail_to = input(
        "Enter the full name of a donar or 'list' for current donars ")
    while mail_to.lower() == "list":
        print(list_of_donars())
        mail_to = input("Please enter a  full name of a donar ")
    try:
        amount = float(input("Enter the donation amount "))
    except ValueError:
        print("\n Amount not valid! Please enter a valid number here! \n")
    else:
        donations(mail_to, amount)
        print(thank_you_message(mail_to))


def summation(arg):
    return sum(donars_data.get(arg))


def create_report():
    header = '\n{:<20}|{:^15}|{:^15}|{:>15}'.format(
        "Donar Name", "Total Given", "Num Gifts", "Average Gift")
    print("Donation Report")
    print(header)
    print('-'*len(header))
    donars_sorted = sorted(donars_data, key=summation, reverse=True)
    for donar in donars_sorted:
        total = sum(donars_data.get(donar))
        num = len(donars_data.get(donar))
        avg = total/num
        print('{:<20} ${:>14,.2f}{:>14}  ${:>16,.2f}'.format(
            donar, total, num, avg))
    print('')


def send_letters_to_all():
    for donar in donars_data:
        # print(entry)
        filename = donar + '.txt'
        with open(filename, 'w') as f:
            f.write(thank_you_message(donar))


def quit_now():
    print("Good bye and see you next time!")
    sys.exit()


def main():
    options_dict = {"s": send_thank_you, "c": create_report,
                    "sa": send_letters_to_all, "q": quit_now}
    while True:
        try:
            option = menu_options()
            options_dict.get(option)()
        except TypeError:
            print("Not a valid option. Please select one of the available options!")


if __name__ == "__main__":
    donars_data = donars()
    main()
